
input_string = input("Введіть рядок: ")
words = input_string.split()
if len(words) > 0:
    print(words[0])
else:
    print("Рядок не містить жодного слова.")
