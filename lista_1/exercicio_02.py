import math
cateto_1 = float(input('informe o valor do primeiro cateto : '))
cateto_2 = float(input('informe o valor do segundo cateto : '))
hipotenusa = math.sqrt((cateto_1*cateto_1)+(cateto_2*cateto_2))

print(f"A hipotenusa do triângulo é : {hipotenusa:.2f}")