
h = abs(int(input("Введіть висоту жердини (h): ")))
a = abs(int(input("Введіть висоту підняття за день (a): ")))
b = abs(int(input("Введіть висоту спуску за ніч (b): ")))
print((h - 2 * b + a - 1) // (a - b))
