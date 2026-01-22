# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, separator=","):
    first_list = first.split(separator)
    second_list = second.split(separator)
    common_list = []
    for item in first_list:
      if item in second_list and item not in common_list:
        common_list.append(item)
    return common_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(
    participants_first_group,
    participants_second_group,
    "|"
)

print(result)

# TODO Провеьте работу функции с разделителем отличным от запятой

