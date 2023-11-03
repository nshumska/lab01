symbol = input("Введіть символ для відображення літери И: ")
letter_n = [
    f"{symbol}   {symbol}",
    f"{symbol}  {symbol}{symbol}",
    f"{symbol} {symbol} {symbol}",
    f"{symbol}{symbol}  {symbol}",
    f"{symbol}   {symbol}"
]
for line in letter_n:
    print(line)
