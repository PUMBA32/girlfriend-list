menu = (
    "Добавить девушку",
    "Показать Девушек из списка",
    "Удалить девушку",
    "Показать статистику",
    "Выход"
)

filename = "путь до файла data.txt"

print("Добро пожаловать в мою темницу, Казанова!", end="")

while True:
    print("\n")
    for i in range(len(menu)):
        print(f"[{i+1}] - {menu[i]}")
    print()

    choice = input(">>> ")
    if choice not in "1234567890":
        print("Ошибка ввода!")
        continue
    else:
        choice = int(choice)

    if choice == 1:  # Add Girl
        name = input("Введите имя и фамилию (если фамилии нет то -): ").strip().title()       # Имя
        age = input("Введите возраст: ").strip()            # Возраст
        city = input("Введите город: ").strip().title()     # Город
        tg = input("Введите телеграм: ").strip()            # Телеграм
        phone = input("Введите номер телефона: ").strip()   # Номер телефона
        
        print("Теперь дай оценку по нескольким параметрам [0-5]")
        try:
            g_communication = int(input("Коммуникация: "))  # Коммуникация
        except TypeError:
            print("Ты должен ввести цифру от 0 до 5!")
            continue

        try:
            g_appearance = int(input("Внешность: "))               # Внешность
        except TypeError:
            print("Ты должен ввести цифру от 0 до 5!")

        try:
            g_forms = int(input("Формы: "))                         # Формы
        except TypeError:
            print("Ты должен ввести цифру от 0 до 5!")
        
        try:
            g_hobbies = int(input("Увлечения: "))                     # Увлечения
        except TypeError:
            print("Ты должен ввести цифру от 0 до 5!")
        
        try:
            g_iq = int(input("Интеллект: "))                               # Интеллект     
        except TypeError:
            print("Тоесть первые 4 ввода были корректным, а на этом решил обосраться..")              

        stroke = f"{name} {age} {city} {tg} {phone} {g_communication} {g_appearance} {g_forms} {g_hobbies} {g_iq}\n"
        
        try:
            file = open(filename, "a+", encoding="utf-8")
            file.write(stroke)
        except:
            print("\nЧерт, какая-то неизвестная ошибка!")
        else:
            file.close()
            print("\nДанные были записаны успешно!")

    elif choice == 2:  # Show Girls
        file = open(filename, "r", encoding="utf-8")
        lines = file.readlines()

        print("\n----------------------------------------------------------------------------------------------------")
        print("| № | Имя\t| Фамилия\t| Возраст |  Город\t|   Телеграм\t| Номер телефона  | Оценка |")
        print("----------------------------------------------------------------------------------------------------")
        
        for i in range(len(lines)):
            print(f"| {i+1} |", end="")
            
            line = lines[i].split()

            communication = int(line[6])
            appearance = int(line[7])
            forms = int(line[8])
            hobbies = int(line[9])
            iq = int(line[10])

            if(line[0] == '-'):  
                print("    None    ", end="\t|")
            else:
                print(f"  {line[0]}", end="\t|")  # Имя
            
            if(line[1] == '-'):
                print("    None    ", end="\t|")
            else:
                print(f"  {line[1]}", end="\t|")  
            
            print(f"   {line[2]}", end="\t  |")  # возраст
            
            if(line[3] == '-'):
                print(f"  None  ", end="\t|")
            else:
                print(f"  {line[3]}", end="\t|")  # город

            if(line[4] == '-'):
                print("    None    ", end="\t|")
            else:
                print(f"  {line[4]}", end="\t|")  # телеграм
            
            if(line[5] == '-'):
                print("      None       ", end="|")
            else:
                print(f"  {line[5]}", end="\t|")  # номер телефона

            print(f"  {(communication+appearance+forms+hobbies+iq)/5}   ", end="|\n")
        print("----------------------------------------------------------------------------------------------------")

    elif choice == 3:  # Delete Girl
        try:
            number = int(input("Введи номер девушки, которую хотите удалить из списка: "))
        except:
            print("Вот дерьмо, какая то ошибка!")
            continue
        
        file = open(filename, "r+", encoding="utf-8")
        lines = file.readlines()
        file.close()
        
        file = open(filename, "w+", encoding="utf-8")
        if len(lines) > 0:
            for i in range(len(lines)):
                if i+1 != number:
                    file.write(lines[i])
                else:
                    deleted_file = lines[i]
            file.close()
        print("Девушка была успешно удалена из статистики!")

    elif choice == 4:  # Show statistic
        file = open(filename, "r", encoding="utf-8")
        lines = file.readlines()
        file.close()

        if len(lines) > 0:
            dictionary = {}
            i = 1
            for line in lines:
                line = line.split()

                name = line[0]
                communication = int(line[6])
                appearance = int(line[7])
                forms = int(line[8])
                hobbies = int(line[9])
                iq = int(line[10])

                middle_grade = (communication+appearance+forms+hobbies+iq)/5
                dictionary[i] = [name, communication, appearance, forms, hobbies, iq, middle_grade]
                i += 1

                dictionary = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
                
            print("Статистика------------------------------------")
            print("| № |     Ммя     | К | В | Ф | У | И | Балл |")
            print("----------------------------------------------")

            i = 1
            for key, value in dictionary.items():
                print(f"| {i} | {value[0]}\t  | {value[1]} | {value[2]} | {value[3]} | {value[4]} | {value[5]} | {value[6]}  |")
                i += 1

            print("----------------------------------------------")
        else:
            print("Список пуст")
            
    else:  # Exit
        break