print("Estructura Condicionales")

# Condicional Simple
notaTBI= 17

if notaTBI >= 10.51:
    print("Aprobado")

# Condicional Doble
edad= 17
if edad >= 18:
    print("Tomar bebidas en exceso no es bueno") 
else:
    print("No apto para menores")

#Condicional Anidado
nota = 20
if nota >17 & nota <=20:
    print("Alumno Brillante")
elif nota >=15 & nota <17:
    print("Alumno Excelente")
elif nota >=13 & nota <15:
    print("Alumno Bueno")
elif nota >=10.5 & nota <13:
    print("Alumno Regular")
else:
    print("Alumno con bajo rendimiento")

# Condicional Multiple
"""
Python 3.9.0 a versiones anteriones no existe condiconal multiple. Todo se trabajaba con IF-ELIF-ELSE.

Python 3.10 a superior se trabaja con MATCH
"""

num=4
match num:
    case 1: print("Vocal A")
    case 2: print("Vocal E")
    case 3: print("Vocal I")
    case 4: print("Vocal O")
    case 5: print("Vocal U")
    case _: print("Numero no corresponde a una vocal")