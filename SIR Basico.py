""" Librerias """
from matplotlib import pyplot as plt
import numpy as np

''' cargar datos '''
from datos import data_acumulada as dt_acu
from datos import data_diaria as dt_dia

''' formulas sir'''
import formulas as fs

''' datos '''
data_cum = np.array(dt_acu.data_acumulada)
data_dia = np.array(dt_dia.data_diaria)
poblacion = 32625948  # poblacion del Perú proyección INEI

''' datos acumulados '''
cuarentena = np.array(data_cum[:, 2], dtype=np.int16)
PR_Pos = np.array(data_cum[:, 5], dtype=np.int64)
PM_Pos = np.array(data_cum[:, 6], dtype=np.int64)
fall_cum = np.array(data_cum[:, 7], dtype=np.int64)
recup_cum = np.array(data_cum[:, 8], dtype=np.int64)

conf_cum = PR_Pos + PM_Pos
act_cum = conf_cum - (fall_cum + recup_cum)

'''datos diarios'''
PR_Neg_dia = np.array(data_dia[:, 3], dtype=np.int64)
PM_Neg_dia = np.array(data_dia[:, 4], dtype=np.int64)
PR_Pos_dia = np.array(data_dia[:, 5], dtype=np.int64)
PM_Pos_dia = np.array(data_dia[:, 6], dtype=np.int64)
fall_dia = np.array(data_dia[:, 7], dtype=np.int64)
recup_dia = np.array(data_dia[:, 8], dtype=np.int64)

PR_total_dia = PR_Pos_dia + PR_Neg_dia
PM_total_dia = PM_Pos_dia + PM_Neg_dia
Total_prueba_dia = PR_total_dia + PM_total_dia

conf_dia = PM_Pos_dia + PR_Pos_dia
por_pos = []
for x1 in range(0, len(recup_cum)):
    pp = conf_dia[x1]*100 / Total_prueba_dia[x1]
    por_pos.append(pp)

''' Datos extras '''
dia_cua = cuarentena[len(recup_cum) - 1]
suscep = poblacion - act_cum[dia_cua - 1] - fall_cum[dia_cua - 1] - recup_cum[dia_cua - 1]

''' modelamiento '''
# tasa de recuperacion = [(R(t+1)-R(t))/I(t)]
tasa_recup = []
for t in range(10, len(recup_cum)):
    fs.cal_tasa_recu(t, recup_cum, act_cum, tasa_recup)

# tasa de contagio = [(S(t)-S(t+1))*N]/(S(t)*I(t))
tasa_cont = []
for t in range(10, len(recup_cum)):
    fs.cal_tasa_cont(t, act_cum, tasa_recup, recup_cum, fall_cum, poblacion, tasa_cont)

''' Tendencias '''
# tendencia tasa de contagio
tend_cont = np.polyfit(cuarentena[10:], tasa_cont, 6)
ecu_cont = np.poly1d(tend_cont)
alfa = ecu_cont(dia_cua + 1)

# tendencia tasa de recuperación
tend_recup = np.polyfit(cuarentena[10:], tasa_recup, 6)
ecu_recup = np.poly1d(tend_recup)
gamma = ecu_recup(dia_cua + 1)

''' Calculo final '''
# I(t+1) = I(t)*(1-gamma)+[alfa*S(t)*I(t)]/N
pro_act = int(act_cum[dia_cua - 1 + 10] * (1 - gamma)) + ((alfa * suscep * act_cum[dia_cua - 1 + 10]) / poblacion)

# R(t+1) = R(t)+ gamma * I(t)
pro_recup = int(recup_cum[dia_cua - 1 + 10] + (gamma * act_cum[dia_cua - 1 + 10]))

# Contagiados_acum(t+1) = pronost_activ + pronost_recup + pronost_fallecidos*
pro_cont_acum = int(pro_act + pro_recup + fall_cum[dia_cua - 1 + 10])  # cambiar por pronostico de fallecidos

# r0 = tasa_cont / tasa_recup
r0 = []
for i in range(14, len(tasa_recup)):
    r_aux = tasa_cont[i] / tasa_recup[i]
    r0.append(r_aux)

print(pro_cont_acum)
print(pro_recup)

''' visualizacion '''
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from plotly import io

# Grafica Principal Acum Contagiados, Activos, Recuperados vs tiempo
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=cuarentena[10:],
        y=conf_cum[10:],
        mode='lines',
        name='Contagiados',
        # showlegend= False
    )
)
fig.add_trace(
    go.Scatter(
        x=cuarentena[10:],
        y=act_cum[10:],
        mode='lines',
        name='Activos'
    )
)
fig.add_trace(
    go.Scatter(
        x=cuarentena[10:],
        y=recup_cum[10:],
        mode='lines',
        name='Recuperados'
    )
)

fig.update_layout(
    margin=dict(l=20, r=50, b=20, t=30),
    title='Casos Acumulados',
)

# fig.write_html('grafica1.html', auto_open=True)
io.write_json(fig, 'grafica1.json', pretty=True)
fs.json_js(arch_json='grafica1.json', arch_js='grafica1.js', nombre='grafica1')

# Grafica diario nuevos contagiados vs cuarenten
fig2 = go.Figure()
fig2.add_trace(
    go.Scatter(
        x=cuarentena[10:],
        y=conf_dia[10:],
        mode='lines',
        name='Nuevos casos',
        showlegend=False
    )
)
fig2.update_layout(
    margin=dict(l=20, r=20, b=20, t=30),
    title='Nuevos Casos Diarios',
)

# fig2.write_html('grafica2.html', auto_open=True)
io.write_json(fig2, 'grafica2.json', pretty=True)
fs.json_js(arch_json='grafica2.json', arch_js='grafica2.js', nombre='grafica2')

# Grafica diaria pruebas nuevas vs dia cuarentena
fig3 = go.Figure()
fig3.add_trace(
    go.Scatter(
        x=cuarentena[10:],
        y=Total_prueba_dia[10:],
        mode='lines',
        name='Total',
        showlegend=True
    )
)
fig3.add_trace(
    go.Scatter(
        x=cuarentena[10:],
        y=PM_total_dia[10:],
        mode='lines',
        name='Moleculares',
        showlegend=True
    )
)
fig3.add_trace(
    go.Scatter(
        x=cuarentena[10:],
        y=PR_total_dia[10:],
        mode='lines',
        name='P.Rápidas',
        showlegend=True
    )
)
fig3.update_layout(
    margin=dict(l=20, r=20, b=20, t=30),
    title='Nuevas Pruebas Diarias'
)
# fig3.write_html('grafica3.html', auto_open=True)
io.write_json(fig3, 'grafica3.json', pretty=True)
fs.json_js(arch_json='grafica3.json', arch_js='grafica3.js', nombre='grafica3')

'''tablas'''

# tabla 1
aux = 'Día ' + data_cum[-1][2] + ' de cuarentena'
tabla1 = [
    ['Datos Oficiales', 'Fecha', 'Contagiados', 'Recuperados', 'Fallecidos'],
    [aux, data_cum[-1][0], conf_cum[-1], data_cum[-1][8], data_cum[-1][7]]
]
fig4 = go.Figure(
    data=go.Table(
        header=dict(values=tabla1)
        # cells=dict(values=tabla1[1:])
    ),
)
fig4.update_layout(
    width=409.8, height=190,
    margin=dict(l=10, r=10, b=5, t=20),
)

# fig4.write_html('tabla1.html', auto_open=True)
io.write_json(fig4, 'tabla1.json', pretty=True)
fs.json_js(arch_json='tabla1.json', arch_js='tabla1.js', nombre='tabla1')

# tabla 2
import statistics as st
aux_mue = st.mean(Total_prueba_dia[-8:-1])
aux_por = round(st.mean(por_pos[-8:-1]), 2)
aux_rec = st.mean(recup_dia[-8:-1])
aux_fall = st.mean(fall_dia[-8:-1])
tabla2 = [
    [' ',            'Muestras Proc.', '% de Posit.', 'Recuperados', 'Fallecidos'],
    [data_cum[-1][0], Total_prueba_dia[-1], round(por_pos[-1], 2), recup_dia[-1], fall_dia[-1]],
    ['Media Ult. 7 días', aux_mue, aux_por, aux_rec, aux_fall]
]
fig5 = go.Figure(
    data=go.Table(
        header=dict(values=tabla2)
        # cells=dict(values=tabla2[1:])
    ),
)
fig5.update_layout(
    width=409.8, height=190,
    margin=dict(l=10, r=10, b=5, t=20),
)

# fig5.write_html('tabla1.html', auto_open=True)
io.write_json(fig5, 'tabla2.json', pretty=True)
fs.json_js(arch_json='tabla2.json', arch_js='tabla2.js', nombre='tabla2')

# tabla 3
aux_dia = str(1 + cuarentena[-1])
aux_2 = 'Día ' + aux_dia + ' de cuarentena'
aux_fec = '06-jul'
aux_pro_con = '308235'+' ± '+'0.391'+'%'
aux_pro_recup = '199240'+' ± '+'0.937'+'%'
tabla3 = [
    ['Pronóstico', 'Fecha', 'Contagiados', 'Recuperados'],
    [aux_2, aux_fec, aux_pro_con, aux_pro_recup]
]
fig5 = go.Figure(
    data=go.Table(
        header=dict(values=tabla3)
    ),
)
fig5.update_layout(
    width=341.5, height=190,
    margin=dict(l=10, r=10, b=5, t=25),
)

# fig5.write_html('tabla3.html', auto_open=True)
io.write_json(fig5, 'tabla3.json', pretty=True)
fs.json_js(arch_json='tabla3.json', arch_js='tabla3.js', nombre='tabla3')

