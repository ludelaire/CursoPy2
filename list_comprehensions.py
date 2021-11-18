# LAS primeras 2 funciones son ejemplos anteriores al concepto de list comprehension

def ciclo():
    sq_list = []
    for i in range(1, 101):
        sq_list.append(i**2)

    print(sq_list)

def no_div_entre_3():
    sq_list = []
    for i in range(1, 101):
        if i%3 != 0:
            sq_list.append(i**2)
    
    print(sq_list)

def main():
    my_list = [i for i in range(1, 100000) if i%4==0 and i%6==0 and i%9==0]
    print(my_list)

if __name__ == '__main__':
    main()