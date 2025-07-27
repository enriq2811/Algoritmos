
#Aquí en esta parte puedes ingresar las distintas actvididades que tengas:

actividades = [
    (9.00, 10.5, 'gym'),
    (9.5, 10.5, 'almuerzo'),
    (11.5, 12.5, 'clase'),
    (12.5, 13.5, 'super'),
    (11.00, 13.5, 'comida'),
    (14.00, 15.5, 'yoga'),
    (13.00, 14.5, 'estudio')
]

#aqui organizamos las actividades
actividades_ordenadas = sorted(actividades, key=lambda x: x[1])

agenda = []
hora_actual = 0

for inicio, fin, nombre in actividades_ordenadas:
    if inicio >= hora_actual:
        agenda.append((inicio, fin, nombre))
        hora_actual = fin


#recuerda ejecutar el codigo en la consola para ver el resultado
print("agenda ideal:")
for inicio, fin, nombre in agenda:
    print(f"{nombre}: {inicio} - {fin}")
