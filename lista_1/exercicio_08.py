a = float(input('Digite o valor de A : '))
b = float(input('Digite o valor de B : '))
c = float(input('Digite o valor de C : '))
d = float(input('Digite o valor de D : '))
e = float(input('Digite o valor de E : '))
f = float(input('Digite o valor de F : '))

y = (a*f) - (c*d) / (a*e) - (b*d)

x = (c*e) - (b*f) / (a*e) * (b*d) 

f = d*x + e*y

print(f'O valor de y é {y:.2f}, e o valor de X é : {x:.2f}')
