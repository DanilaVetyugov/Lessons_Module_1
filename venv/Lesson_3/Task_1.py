
num_translate_adv = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять","eleven": "одиннадцать"}

def num(eng):
  return num_translate_adv(eng)

rus = input("Введите число на английском от 0 до 10: \n")

print(num_translate_adv.get(rus))