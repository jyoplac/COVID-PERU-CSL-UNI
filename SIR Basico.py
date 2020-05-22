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
PR_Pos_dia = np.array(data_dia[:, 5], dtype=np.int64)
PM_Pos_dia = np.array(data_dia[:, 6], dtype=np.int64)
recup_dia = np.array(data_dia[:, 8], dtype=np.int64)

conf_dia = PM_Pos_dia + PR_Pos_dia

''' Datos extras '''
dia_cua = cuarentena[len(recup_cum)-1]
suscep = poblacion - act_cum[dia_cua-1] - fall_cum[dia_cua-1] - recup_cum[dia_cua-1]

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
alfa = ecu_cont(dia_cua+1)

# tendencia tasa de recuperación
tend_recup = np.polyfit(cuarentena[10:], tasa_recup, 6)
ecu_recup = np.poly1d(tend_recup)
gamma = ecu_recup(dia_cua+1)

''' Calculo final '''
# I(t+1) = I(t)*(1-gamma)+[alfa*S(t)*I(t)]/N
pro_act = int(act_cum[dia_cua-1+10]*(1-gamma))+((alfa*suscep*act_cum[dia_cua-1+10])/poblacion)

# R(t+1) = R(t)+ gamma * I(t)
pro_recup = int(recup_cum[dia_cua-1+10]+(gamma*act_cum[dia_cua-1+10]))

# Contagiados_acum(t+1) = pronost_activ + pronost_recup + pronost_fallecidos*
pro_cont_acum = int(pro_act + pro_recup + fall_cum[dia_cua-1+10])  # cambiar por pronostico de fallecidos

# r0 = tasa_cont / tasa_recup
r0 = []
for i in range(14, len(tasa_recup)):
    r_aux = tasa_cont[i] / tasa_recup[i]
    r0.append(r_aux)

print(pro_cont_acum)
print(pro_recup)
print(r0)

''' visualizacion '''
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


# CSL = plt.imread('CSL LOGO.png')
# .imread('https://scontent.ftru3-1.fna.fbcdn.net/v/t1.0-9/14729329_1222514917815216_3988353329269364560_n.png?_nc_cat=101&_nc_sid=85a577&_nc_eui2=AeF7tHM08ezc-oAQPZzRcAOxQKxrlWxLIK9ArGuVbEsgrxTwEGSgcEIRu012HBqxQdarfJvc5WkuhPAP0JFNH1F2&_nc_oc=AQmAZxIZlpF1cpws3MdmNA4h0NcYBMBN4zm5O2Pq14B0xydOWRckLyfdHOzO1RS8TdqnGKfBITxrOwZfdOVuRhQr&_nc_ht=scontent.ftru3-1.fna&oh=434b671dade264969e6ba79a35111d9f&oe=5EEB2722')

fig = make_subplots(rows=2, cols=3,
                    column_widths=[0.4, 0.3, 0.3],
                    row_heights=[0.5, 0.5],

                    )

fig.add_trace(
    go.Scatter(
        x=cuarentena[10:],
        y=conf_cum[10:],
        mode='lines+markers',
        name='Contagiados',
        # showlegend= False
    ),
    1, 2
)
fig.add_trace(
    go.Scatter(
        x=cuarentena[10:],
        y=recup_cum[10:],
        mode='lines+markers',
        name='Recuperados'
    ),
    1, 2
)
fig.add_trace(
    go.Scatter(
        x=cuarentena[10:],
        y=act_cum[10:],
        mode='lines+markers',
        name='Activos'
    ),
    1, 2
)

fig.add_trace(
    go.Scatter(
        x=cuarentena[10:],
        y=conf_dia[10:],
        mode='lines+markers',
        name='Confirmados Diario'
    ),
    1, 3
)


# plt.plot(cuarentena[24:], r0)
# plt.show()
'''
print(recup_dia[10:], act_cum[10:])
plt.plot(cuarentena[10:], tasa_recup[10:])
plt.show()
'''







# fig = px.scatter(x=cuarentena, y=conf_cum)
# fig.write_html('Conf_cum vs Cuarentena.html', auto_open=True)
fig.write_html('prueba.html', auto_open=True)
