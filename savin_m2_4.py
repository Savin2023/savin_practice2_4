def binary(e,tmp):
    if e!=0:
        tmp.insert(0,e%2)
        e=e//2
        binary(e,tmp)
    return(tmp)
def multipl(a,b):
    if b!=0:
        return (a+multipl(a,b-1))
    else:
        return 0
def power(c,d):
    if d!=1:
        return (c*power(c,d-1))
    else:
        return c
# --------------------------------------
command=""
while command!="stop":
    print("Введите команду:")
    print("b - перевод в бинарный вид")
    print("m - умножение")
    print("p - возведение в степень")
    print("stop - выход")
    command=input()
    if command=="m":
        print("Введите множители через пробел")
        print("Рассматриваются только неотрицательные целые числа")
        a,b=map(int,input().split())
        if a<0 or b<0:
            print("Ошибка ввода\n")
        else:
            print("Результат умножения:",(multipl(a,b)),"\n")
    elif command=="p":
        print("Введите основание и степень через пробел")
        print("Рассматриваются только натуральные числа")
        c,d=map(int,input().split())
        if c<1 or d<1:
            print("Ошибка ввода\n")
        else:
            print("Результат возведения в степень:",(power(c,d)),"\n")
    elif command=="b":
        print("Введите неотрицательное целое число")
        e=int(input())
        if e<0:
            print("Ошибка ввода\n")
        else:
            tmp=[]
            print("Результат конвертации в двоичный формат:",(binary(e,tmp)),"\n")
