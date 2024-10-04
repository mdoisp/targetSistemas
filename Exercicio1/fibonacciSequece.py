userNumber = int(input("Digite um numero: "));

a, b = 0, 1
while b < userNumber:
    a, b = b, a + b
if userNumber == b:
    print(f"O número {userNumber} pertence à sequência de Fibonacci.")
else:
    print(f"O número {userNumber} NÃO pertence à sequência de Fibonacci.")
