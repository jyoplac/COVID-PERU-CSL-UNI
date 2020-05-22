def cal_tasa_recu(t, recuperados_cum, activos_cum, tasa_recup_out):
    # gamma = [R(t+1)-R(t)]/I(t)
    gamma = recuperados_cum[t] - recuperados_cum[t-1]
    gamma = gamma / activos_cum[t-1]
    tasa_recup_out.append(gamma)
    return tasa_recup_out


def cal_tasa_cont(t, activos_cum, gamma, recuperados, fallecidos, poblacion, tasa_cont_out):
    susceptibles = poblacion - fallecidos[t-1] - activos_cum[t-1] - recuperados[t-1]
    # alfa =  [I(t)-I(t-1)+gamma*I(t-1)]*N/[S(t-1)*I(t-1)]
    alfa = activos_cum[t] - activos_cum[t-1] + (gamma[t-10] * activos_cum[t-1])
    alfa = alfa * poblacion
    alfa = alfa / (activos_cum[t-1]*susceptibles)
    tasa_cont_out.append(alfa)
    return tasa_cont_out
