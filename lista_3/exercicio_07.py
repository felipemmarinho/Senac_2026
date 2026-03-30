N = int(input('Digite um número inteiro positivo : '))

# A = N + (N - 1) / 2 + (N - 2) / 3 + ... + 1/N 
a = 0

for i in range(N):
    a = a + ((N + (N - (i+1)))/2)

print(f'O valor de A é : {a:.2f}')