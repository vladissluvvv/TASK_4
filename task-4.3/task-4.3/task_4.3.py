def is_anagram(a1, b2):
    alphabet = 'àáâãäå¸æçèéêëìíîïðñòóôõö÷øùúûüýþÿ'
    s1 = ''.join(c for c in a1.lower() if c in alphabet)
    s2 = ''.join(c for c in b2.lower() if c in alphabet)
    return sorted(s1) == sorted(s2)
a1 = input("Ââåäèòå ïåðâîå ïðåäëîæåíèå: ")
b2 = input("Ââåäèòå âòîðîå ïðåäëîæåíèå: ")
result = is_anagram(a1, b2)
print(f" {result}")

