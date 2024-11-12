def to_decimal(num,sys):
    l = "0123456789ABCDEF"
    l = l[0:sys]
    new_num = 0
    len_num = len(num)-1
    while len_num > -1:
        for i in range(len(num)):
            for j in range(len(l)):
               if num[i] == l[j]:
                  n = j
                  new_num = new_num + n*pow(sys,len_num)
                  len_num -= 1
    return new_num

def to_system(num_dec,sys):
    end = num_dec
    new_num = ""
    l = "0123456789ABCDEF"
    while end > sys:
        n = end%sys
        for i in range(len(l)):
            if n == i:
                new_num += l[i]
        end = end//sys
    if end != 0:
        for i in range(len(l)):
            if end == i:
                new_num += l[i]
    return new_num[::-1]

def dani():
    l = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    l1 = "0123456789ABCDEF"
    num = "num"
    sys = 1
    while (sys not in l) or [i for i in num if i not in l1[0:sys]]:
        a = input("Enter the numeric and the system in which it (example: 3456x4): ")
        for i in range(0,len(a)):
            if a[i] == "x":
                num = a[0:i]
                sys = int(a[i+1:])
    sys_to = int(input("Enter the system which you want (example: 5): "))
    while sys_to not in l:
        sys_to = int(input("Enter the system which you want (example: 5): "))
    return num,sys,sys_to

stop = ""
while stop != "St":
    numeric,sys,sys_to = dani()
    dec = to_decimal(numeric,sys)
    new = to_system(dec,sys_to)
    print(f"Numeric in new system: {new}")
    stop = input("If you want to stop, enter St, else push Entr: ")