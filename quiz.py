from dictionaries import words_easy, words_medium, words_hard, levels


difficulty = input("Выберите уровень сложности (легкий, средний, тяжелый): ").strip().lower()

if difficulty == "легкий":
    words = words_easy
elif difficulty == "средний":
    words = words_medium
elif difficulty == "тяжелый":
    words = words_hard
else:
    print("Неверный ввод. Уровень сложности установлен на легкий.")
    words = words_easy


answers = {}

for english_word, russian_word in words.items():
    print(f"Слово: {english_word}")
    print(f"Длина слова: {len(russian_word)} букв")
    print(f"Начинается на: {russian_word[0]}...")

    user_answer = input("Ваш ответ: ").strip().lower()
    correct_answer = russian_word.lower()

    if user_answer == correct_answer:
        print(f"Верно! {english_word.capitalize()} — это {russian_word}.")
        answers[english_word] = True
    else:
        print(f"Неверно. {english_word.capitalize()} — это {russian_word}.")
        answers[english_word] = False


correct_answers = [word for word, correct in answers.items() if correct]
incorrect_answers = [word for word, correct in answers.items() if not correct]

print("\nПравильно отвеченные слова:")
for word in correct_answers:
    print(word)

print("Неправильно отвеченные слова:")
for word in incorrect_answers:
    print(word)


score = sum(1 for correct in answers.values() if correct)
rank = levels.get(score, "Нулевой")

print(f"\nВаш ранг: {rank}")
