from datetime import date

# la fecha de hoy
hoy = date.today()
anio_actual = hoy.year

# la fecha de Navidad de este año
navidad = date(anio_actual, 12, 25)

# si ya pasó Navidad, calculamos para el próximo año
if hoy > navidad:
    navidad = date(anio_actual + 1, 12, 25)

# se calculan los días restantes
dias_restantes = (navidad - hoy).days
print(f"Faltan {dias_restantes} días para Navidad! :D")
