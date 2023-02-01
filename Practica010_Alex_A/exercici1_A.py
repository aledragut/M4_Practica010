import datetime

def calculate_age(birth_year):
    current_year = datetime.datetime.now().year
    return current_year - birth_year
