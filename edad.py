from datetime import datetime

nacimiento = input("Ingrese su año de nacimiento: ")

actual = datetime.now().year

edad = actual - int(nacimiento)

print("Tu edad es:", edad)