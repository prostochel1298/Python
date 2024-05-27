def check_pass(pswd):
    symbol = "*-#"
    if len(pswd) > 8:
        for i in pswd:
            if i.isupper() == False:
                print("пароль не подходит, тип ошибки:",{pswd:"В пароле нет заглавной буквы"})
                break   
            elif i.isupper() == True:
                for b in pswd:
                    
                    if b in symbol:
                        print("Вы создали хороший пароль!")
            
                    else:
                        print("пароль не подходит, тип ошибки:",{pswd:"В пароле нет специльных символов"})                         
    else:
        print("пароль не подходит, тип ошибки:",{pswd:"Количество символов меньше 8"})        
print()
check_pass("xbxdr8372")
