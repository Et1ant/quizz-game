score=0
question_1=input("Столица Франции? ")
question_2=int(input("Сколько дней в неделе? (ответ введите числом) "))
question_3=input("Какой язык программирования больше всего используем? ")
question_4=input("Какая планета ближе всего к Солнцу? ")
question_5=input("Какая страна самая большая по территории? ")
question_6=int(input("Сколько будет 2+2*2? (ответ введите числом) "))
question_7=int(input("Какой год сейчас? (ответ введите числом) "))
question_8=input("Какая страна из них самая мальенькая?"
" Выберите один из вариантов: Ватикан, Монако, Науру, Тувалу, Сан-Марино ,Лихтенштейн ")
question_9=int(input("Сколько будет 10x900000? (ответ введите числом) "))
question_10=input("Какой самый высокий водопад в мире? ")
if question_1.lower().strip()=="париж":
    print("Правильно!")
    score+=1
else:    
    print("Неправильно! Правильный ответ: париж")
if question_2==7:
    print("Правильно!")
    score+=1
else:    
    print("Неправильно! Правильный ответ: 7")
if question_3.lower().strip()=="python" or question_3.lower().strip()=="питон" or question_3.lower().strip()=="пайтон":
    print("Правильно!")
    score+=1
else:    
    print("Неправильно! Правильный ответ: python(питон, пайтон)")
if question_4.lower().strip()=="меркурий":
    print("Правильно!")
    score+=1
else:    
    print("Неправильно! Правильный ответ: меркурий")
if question_5.lower().strip()=="россия":
    print("Правильно!")
    score+=1
else:    
    print("Неправильно! Правильный ответ: россия")
if question_6==6:
    print("Правильно!")
    score+=1
else:    
    print("Неправильно! Правильный ответ: 6")
if question_7==2026:
    print("Правильно!")
    score+=1
else:    
    print("Неправильно! Правильный ответ: 2026")
if question_8.lower().strip()=="ватикан":
    print("Правильно!")
    score+=1
else:    
    print("Неправильно! Правильный ответ: ватикан")
if question_9==9000000:
    print("Правильно!")
    score+=1
else:    
    print("Неправильно! Правильный ответ: 9000000")
if question_10.lower().strip()=="анхель":
    print("Правильно!")
    score+=1
else:    
    print("Неправильно! Правильный ответ: анхель")
print(f"\nВаш счет: {score} из 10, Спасибо за игру!")

