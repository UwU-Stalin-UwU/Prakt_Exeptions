class Person():
    def __init__(self, name, surname, age, email):
        #Name into class
        try:
            name = name.lower()
            for i in range (0, len(name)):
                if ord(name[i]) > 122 or ord(name[i]) < 97:
                    raise ValueError("How is this fucking possible?!")
                else:
                    self.__name = name
        except:
            print("Write your name right, you bastard")
        #Surname into class
        try:
            surname = surname.lower()
            for i in range (0, len(surname)):
                if ord(surname[i]) > 122 or ord(surname[i]) < 97:
                    raise ValueError("How is this fucking possible?!")
                else:
                    self.__surname = surname
        except:
            print("Write your surname right, you bastard")
        #Age into class
        try:
            if age < 0:
                raise ValueError("Age couldn't be negative")
            else:
                self.__age = age
        except:
            print("Age couldn't be negative. PLEASE INSERT THE FUCKING CORRECT AGE, YOU LITTLE PIECE OF SHIT")
        #Email into class
        try:
            d = email.split('@')
            if len(d[0]) != 0 and len(d[1]) != 0:
                try:
                    d1 = d[1].split('.')
                    if len(d1[0]) != 0 and len(d1[1]) != 0:
                        self.__email = email
                    else:
                        raise ValueError("Not email, you stupid")
                except:
                    print("Not email, you stupid")
            else:
                raise ValueError("Not email, you stupid")
        except:
            print("Not email, you fool")
        self.settings()
    
    def set_age(self):
        new_age = input("Введите новый возраст: ")
        try:
            if new_age < 0:
                raise ValueError("Age couldn't be negative")
            else:
                self.__age = new_age
        except:
            print("New age is incorrect, you stupid nigga")
    
    def set_name(self):
        new_name = input("Введите новое имя: ")
        try:
            new_name = new_name.lower()
            for i in range (0, len(new_name)):
                if ord(new_name[i]) > 122 or ord(new_name[i]) < 97:
                    raise ValueError("How is this fucking possible?!")
                else:
                    self.__name = new_name
        except:
            print("Write your name right, you bastard")
    
    def set_surname(self):
        new_surname = input("Введите новую фамилию: ")
        try:
            new_surname = new_surname.lower()
            for i in range (0, len(new_surname)):
                if ord(new_surname[i]) > 122 or ord(new_surname[i]) < 97:
                    raise ValueError("How is this fucking possible?!")
                else:
                    self.__surname = new_surname
        except:
            print("Write your surname right, you bastard")
    
    def set_email(self):
        new_email = input("Введите новую почту: ")
        try:
            d = new_email.split('@')
            if len(d[0]) != 0 and len(d[1]) != 0:
                try:
                    d1 = d[1].split('.')
                    if len(d1[0]) != 0 and len(d1[1]) != 0:
                        self.__email = new_email
                    else:
                        raise ValueError("Not email, you stupid")
                except:
                    print("Not email, you stupid")
            else:
                raise ValueError("Not email, you stupid")
        except:
            print("Not email, you fool")
    
    def settings(self):
        user_choice = int(input("Для изменения имени нажмите 1 \n" \
        "Для изменения фамилии нажмите 2 \n" \
        "Для изменения возраста нажмите 3 \n" \
        "Для изменения почты нажмите 4 \n"
        "Для выхода нажмите 5 \n"))
        if user_choice == 1:
            self.set_name()
            self.settings()
        elif user_choice == 2:
            self.set_surname()
            self.settings()
        elif user_choice == 3:
            self.set_age()
            self.settings()
        elif user_choice == 4:
            self.set_email()
            self.settings()
        elif user_choice == 5:
            print("Программа завершена успешно")


name = input("Введите имя: ")
surname = input("Введите фамилию: ")
age = int(input("Введите возраст: "))
email = input("Введите адрес электронной почты: ")
person = Person(name, surname, age, email)