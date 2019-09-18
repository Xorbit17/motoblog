# type:str  UNICODE gegevens

# Encoding is mapping tussen bytes en karakters
# ASCII encoding: Bevat 127 tekens. 32 -> SPACE
# ANSI (heel oud, microsoft) 256 tekens (1 byte)
# 'latin-1' 256 tekens
# UNICODE Encoding
# UTF-8: Twee bytes na elkaar kunnen 1 karakter zijn.
# UTF-16

f = open("c:\\Users\\denni\\test.txt", "r")  #Stiekem omgezet

string = f.read()

print(string)  # Print roept implictiet en automatisch de '__str__' methode aan van het bytes object

f.close()

