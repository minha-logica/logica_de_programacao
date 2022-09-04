#tempo total em segundos ou o valor de n
tempo = 2*86400 + 2*3600 + 0*60 + 30

segundo = 1
minuto  = 60*segundo
hora    = 60*minuto
dia     = 24*hora


dias,    tempo = divmod(tempo, dia)
horas,   tempo = divmod(tempo, hora)
minutos, tempo = divmod(tempo, minuto)
segundos       = tempo


msg = "{} dia(s), {} hora(s), {} minuto(s) e {} segundo(s)"                    
msg = msg.format(dias, horas, minutos, segundos)
print(msg)