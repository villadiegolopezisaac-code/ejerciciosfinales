#Aprobado o Reprobado con mención especial
nota =float(int(input("ingrese la nota del estudiante:")))
if nota < 0 or nota > 60:
    print("el estudiante esta aprobado")
elif nota >=0 and nota < 60:
    print("el estudiante esta reprobado")
elif nota < 90:
    print("el estudiante esta aprobado con mencion especial")