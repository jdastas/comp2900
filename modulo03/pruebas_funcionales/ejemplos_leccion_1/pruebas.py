from ejemplo01 import calcular_promedio
from ejemplo02 import clasificar_numero
  
# Prueba ejemplo 1
assert calcular_promedio(4, 6) == 5, "El promedio calculado no es correcto."

# Prueba ejemplo 02
assert clasificar_numero(5) == "Positivo", "La clasificación no es correcta."
assert clasificar_numero(-3) == "Negativo", "El valor NO es negativo."
assert clasificar_numero(0) == "Cero", "La clasificación no es correcta."