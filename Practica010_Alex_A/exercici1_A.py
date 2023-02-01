import datetime

def calculate_age(birth_year):
    # Obtenemos el año actual utilizando la biblioteca datetime
    current_year = datetime.datetime.now().year
    # Calculamos la edad restando el año actual con el año de nacimiento
    age = current_year - birth_year
    # Retornamos el resultado
    return age
