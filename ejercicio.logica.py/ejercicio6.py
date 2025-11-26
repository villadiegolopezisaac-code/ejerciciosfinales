notas = [float(input()) for _ in range(5)]
p = sum(notas)/5
if p<60: nivel="Bajo"
elif p<80: nivel="Medio"
else: nivel="Alto"
print("Promedio:", p, nivel)
