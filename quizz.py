def ask_question(question_data):
    """Задаёт вопрос и проверяет ответ"""
    user_answer = input(question_data["text"])
    
    # Обработка ответа в зависимости от типа
    if question_data["type"] == "number":
        user_answer = int(user_answer)
    else:
        user_answer = user_answer.lower().strip()
    
    # Проверка (поддерживает несколько вариантов ответа)
    correct_answers = question_data["answers"]
    if user_answer in correct_answers:
        print("Правильно!")
        return 1
    else:
        print(f"Неправильно! Правильный ответ: {correct_answers[0]}")
        return 0


# Все вопросы в одной структуре
questions = [
    {
        "text": "Столица Франции? ",
        "answers": ["париж"],
        "type": "text"
    },
    {
        "text": "Сколько дней в неделе? (число) ",
        "answers": [7],
        "type": "number"
    },
    {
        "text": "Какой язык программирования больше всего используем? ",
        "answers": ["python", "питон", "пайтон"],
        "type": "text"
    },
    {
        "text": "Какая планета ближе всего к Солнцу? ",
        "answers": ["меркурий"],
        "type": "text"
    },
    {
        "text": "Какая страна самая большая по территории? ",
        "answers": ["россия"],
        "type": "text"
    },
    {
        "text": "Сколько будет 2+2*2? (число) ",
        "answers": [6],
        "type": "number"
    },
    {
        "text": "Какой год сейчас? (число) ",
        "answers": [2026],
        "type": "number"
    },
    {
        "text": "Какая страна самая маленькая? (Ватикан, Монако, Науру...) ",
        "answers": ["ватикан"],
        "type": "text"
    },
    {
        "text": "Сколько будет 10*900000? (число) ",
        "answers": [9000000],
        "type": "number"
    },
    {
        "text": "Какой самый высокий водопад в мире? ",
        "answers": ["анхель"],
        "type": "text"
    }
]

# Основная игра
score = 0
for question in questions:
    score += ask_question(question)

# Результат
print(f"\nВаш счёт: {score} из {len(questions)}")
print("Спасибо за игру!")

