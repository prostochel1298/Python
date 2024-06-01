
def find_divisors():
    n = int(input("Введите числитель: "))
    p = int(input("Введите знаменатель: "))
    
    divisors_n = []
    divisors_p = []
    new_devisors = []
    super_new_devisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors_n.append(i)
    for z in range(1,p+1):
        if p % z == 0:
             divisors_p.append(z)
    drob = divisors_n + divisors_p
    for i in drob:
        if i in divisors_n and i in divisors_p:
            new_devisors.append(i)

    for b in new_devisors:
        if b not in super_new_devisors:
            super_new_devisors.append(b)
        else:
            continue
    x=n/super_new_devisors[1]
    c=p/super_new_devisors[1]
    while x%super_new_devisors[1] == 0 and c%super_new_devisors[1] == 0:
        if x%super_new_devisors[1] != 0 and c%super_new_devisors[1] !=0:
            break
        n=x
        p=c
        x=n/super_new_devisors[1]
        c=p/super_new_devisors[1]
    
    print(int(x),'/',int(c))
find_divisors()
    
        



