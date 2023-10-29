# TODO Напишите функцию find_common_participants
def find_common_participants(f, s, mark="|"):
    k = set(f.split(mark))
    j = set(s.split(mark))
    need = k.intersection(j)
    result = sorted(list(need))
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
both = find_common_participants(participants_first_group, participants_second_group)
print(sorted(both))


# TODO Проверьте работу функции с разделителем отличным от запятой
def find_common_participants2(f, s, mark="?"):
    k = set(f.split(mark))
    j = set(s.split(mark))
    need = k.intersection(j)
    result = sorted(list(need))
    return result

both2 = find_common_participants2(participants_first_group, participants_second_group)
print(sorted(both2))
