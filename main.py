# Main (Alex):

import exercici1_A
import exercici2_A

# Llama a la función de calcular la edad
birth_year = int(input("Enter birth year: "))
age = exercici1_A.calculate_age(birth_year)
print("Age:", age)

# Llama a la función del diccionario
print("Dictionary length:", exercici2_A.d.__len__())
print("Values:", exercici2_A.d.values())
print("Last item:", list(exercici2_A.d.items())[-1])

# Main (Fede)
