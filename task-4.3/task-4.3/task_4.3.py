def is_anagram(a1, b2):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    s1 = ''.join(c for c in a1.lower() if c in alphabet)
    s2 = ''.join(c for c in b2.lower() if c in alphabet)
    return sorted(s1) == sorted(s2)
sentence1 = input("Введите первое предложение: ")
sentence2 = input("Введите второе предложение: ")
result = is_anagram(a1, b2)
print(f" {result}")

