def price():
    intenger = list()
    pr = input("Введите цену товара(стоп - закончить): ")
    while pr != "стоп":
        while True:
            try:
                pr = int(pr)
            except ValueError:
                continue
        intenger.append(pr)
        pr = input("Введите цену товара(стоп - закончить): ")

    print(intenger)  
price()

    
       


    



    
   


  