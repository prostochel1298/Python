spisok = ["тополь","дуб","секвоя","береза","осина","баобаб"]
def all_eq(lst):
    sp = []
    spisok2 = []
    for i in lst:
        sp.append(len(i))
    a=max(sp)
    for i in lst:
        if len(i)<a:
            while len(i)<a:
                i+="_"
        spisok2.append(i)
    print(spisok2)
all_eq(spisok)                    
                 
                

        