G0 X0 Y0 Z2
#1 = 0 ; Profundidade inicial
#2 = -15 ; Profundidade final
#3 = 30 ; Avanço
#4 = 2 ; Incremento
N1( TESTE)
G1 Z#1 F#3
#5 = #1 + 0.5
G0 Z#5
#1 = #1 - #4
IF[#1GT#2]THEN GOTO1
G1 Z#2 F#3
