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

def to_bin(dec):
    l = "01"
    new_num = ""
    while dec > 2:
        n = dec%2
        for i in range(len(l)):
            if n == i:
                new_num += l[i]
        dec = dec//2
    if dec != 0:
        for i in range(len(l)):
            if dec == i:
                new_num += l[i]
    return new_num[::-1]

def to_hex(dec):
    l = "0123456789ABCDEF"
    new_num = ""
    while dec > 16:
        n = dec%16
        for i in range(len(l)):
            if n == i:
                new_num += l[i]
        dec = dec//16
    if dec != 0:
        for i in range(len(l)):
            if dec == i:
                new_num += l[i]
    return new_num[::-1]

def check(num, sys):
    if num[0] == "0" and num[1] == "b":
        num = num[2:]
        bins = "01"
        for i in num:
            if i not in bins:
               return "er"
            else:
                if sys == "dec":
                    return to_decimal(num,2)
                elif sys == "hex":
                    return to_hex(to_decimal(num,2))
                elif sys == "bin":
                    return num
                else:
                    return "er"
    elif num[0] == "0" and num[1] == "x":
        hexas = "0123456789ABCDEF"
        num = num[2:]
        for i in num:
            if i not in hexas:
                return "er"
            else:
                 if sys == "dec":
                     return to_decimal(num,16)
                 elif sys == "hex":
                      return num
                 elif sys == "bin":
                      return to_bin(to_decimal(num,16))
                 else:
                      return "er"
    elif num.isdecimal():
        if sys == "bin":
           return to_bin(int(num))
        elif sys == "hex":
            return to_hex(int(num))
        elif sys == "dec":
            return int(num)
        else:
            return "er"
    else:
        return "er"

ask_num = input("Enter the numeric(examples: binary 0b1010, decimal 3456, hexadecimal 0x3A5): ")
ask_sys = input("Enter the system(binary - bin, decimal - dec, hexadecimal - hex): ")
while ask_num != "St":
    a = check(ask_num,ask_sys)
    if a == "er":
        ask_num = input("If you want continue enter next number, else enter St: ")
        ask_sys = input("Enter the system(binary - bin, decimal - dec, hexadecimal - hex): ")
    else:
        print(f"The result: {a}")
        ask_num = input("If you want continue enter next number, else enter St: ")
        ask_sys = input("Enter the system(binary - bin, decimal - dec, hexadecimal - hex): ")