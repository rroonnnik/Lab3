# TODO  Напишите функцию count_letters
def count_letters(text):
  letters_count = {}
  for char in text:
    if char.isalpha():       # проверяем, что это буква
      char_lower = char.lower()  # переводим в нижний регистр
      if char_lower in letters_count:
        letters_count[char_lower] = letters_count[char_lower] + 1
      else:
        letters_count[char_lower] = 1
  return letters_count

# TODO Напишите функцию calculate_frequency
def calculate_frequency(letters_count):
    total_letters = 0
    for count in letters_count:
        total_letters = total_letters + letters_count[count]

    frequency = {}
    for letter in letters_count:
        frequency[letter] = round(letters_count[letter] / total_letters, 2)
    return frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
letters_count = count_letters(main_str)
letters_frequency = calculate_frequency(letters_count)
for letter in letters_frequency:
  print(letter,":",letters_frequency[letter])
# TODO Распечатайте в столбик букву и её частоту в тексте
