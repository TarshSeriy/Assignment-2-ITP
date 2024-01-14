def task_1():
    color1 = input().strip().lower()
    color2 = input().strip().lower()

    if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
        result = "purple"
    elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
        result = "orange"
    elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
        result = "green"
    else:
        result = "color error"

    print(result)


def task_2():
    pocket_number = int(input())
    if pocket_number == 0:
        print("green")
    elif 1 <= pocket_number <= 10 and pocket_number % 2 == 0:
        print("black")
    elif 1 <= pocket_number <= 10 and pocket_number % 2 != 0:
        print("red")
    elif 11 <= pocket_number <= 18 and pocket_number % 2 == 0:
        print("red")
    elif 11 <= pocket_number <= 18 and pocket_number % 2 != 0:
        print("black")
    elif 19 <= pocket_number <= 28 and pocket_number % 2 == 0:
        print("black")
    elif 19 <= pocket_number <= 28 and pocket_number % 2 != 0:
        print("red")
    elif 29 <= pocket_number <= 36 and pocket_number % 2 == 0:
        print("red")
    elif 29 <= pocket_number <= 36 and pocket_number % 2 != 0:
        print("black")
    elif pocket_number < 0 or pocket_number > 36:
        print("input error")


def task_3():
    col1, row1, col2, row2 = map(int, input().split())
    if abs(col1 - col2) == abs(row1 - row2):
        print("YES")
    else:
        print("NO")


def task_4():
    a1 = int(input())
    b1 = int(input())
    a2 = int(input())
    b2 = int(input())
    intersection_start = max(a1, a2)
    intersection_end = min(b1, b2)
    if intersection_start <= intersection_end:
        if intersection_start == intersection_end:
            print(intersection_start)
        else:
            print(intersection_start + intersection_end)
    else:
        print("Empty set")


def task_7():
    a = "hello"
    result = a.capitalize()
    print(result)

    b = "HellO"
    result1 = b.capitalize()
    print(result1)

    c = "hello"
    result3 = c.title()
    print(result3)

    d = "Hello"
    result4 = d.lower()
    print(result4)

    f = "Hello world"
    result5 = f.startswith("Hello")
    print(result5)

    g = "Hello world"
    result6 = g.rfind("o")
    print(result6)

    h = "hello world"
    result7 = h.index
    print(result7)

    j = "hello world"
    result8 = j.lstrip()
    print(result8)

    i = "hello world"
    result9 = i.isalnum()
    print(result9)

    k = " "
    result10 = k.isspace()
    print(result10)


def task_11():
    n = int(input())
    for i in range(n, 0, -1):
        print('*' * i)


def task_12():
    n = int(input())
    m = int(input())
    if m < n:
        for i in range(m, n + 1):
            print(i)
    else:
        for i in range(m, n - 1, -1):
            print(i)


def task_13():
    n = int(input())
    largest = second_largest = 0
    for _ in range(n):
        num = int(input())
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    print(largest)
    print(second_largest)


def task_14():
    n = int(input())
    fibonacci = [0, 1]
    for _ in range(2, n):
        next_number = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_number)
    print(fibonacci)


def task_15():
    count_of_fives = 0
    while True:
        num = int(input())
        if num <= 0 or num > 5:
            break
        if num == 5:
            count_of_fives += 1
    print(count_of_fives)


def task_16():
    price = int(input())
    coins = [25, 10, 5, 1]
    total_coins = 0
    index = 0
    while price > 0 and index < len(coins):
        num_coins = price // coins[index]
        total_coins += num_coins
        price %= coins[index]
        index += 1
    print(total_coins)


def task_17():
    num = int(input("Enter a natural number: "))
    num_str = str(num)
    reversed_num_str = num_str[::-1]

    if num_str == "".join(sorted(reversed_num_str)):
        print("YES")
    else:
        print("NO")


def task_18():
    find = 5
    for i in range(6):
        if i == find:
            break
        print(i)


def task_19():
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i)


def task_20():
    num = 1
    for i in range(10):
        print(num)
        num += 1
    while num <= 10:
        print(num)
        if num == 5:
            print("break")
            break
        num += 1


def task_21():
    num = 1
    while num <= 10:
        if num % 3 == 0:
            num += 1
            continue
        print(num)
        num += 1
