def fibonacci(x):
  n1 = 0
  n2 = 1
  soma = 1
  for i in range(0, 22):
    if n1 == x:
        return 'Pertence'
    soma = n2 + n1
    n1 = n2
    n2 = soma
  return 'Não pertence'

print(fibonacci(2))