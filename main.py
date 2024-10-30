my_list = [42,69,322,13,0,99,-5,9,8,7,-6,5]
a = 0
b = len(my_list)
while a != b:
    c = my_list[a]
    if c >= 0:
        if c > 0:
            print(c)
            a = a + 1
            continue
        else:
            a = a + 1
            continue

    else:
        break

