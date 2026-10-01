#1
n = int(input())
sum = 0
count = 0
avarage = 0

for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
        count += 1
        avarage += i/n + 1
print(sum)
print(count)
print(avarage)

#2
n = int(input())

if  n == 0:
    count = 0
    total_sum = 0
    max_digit = 0
    min_digit = 0
else:
    count = 0
    total_sum = 0
    max_digit = 0
    min_digit = 9
    while n > 0:
        digit = n % 10

        count += 1
        total_sum += digit

        if digit > max_digit:
            max_digit = digit

        if digit < min_digit:
            min_digit = digit
        n = n // 10
print(count)
print(total_sum)
print(max_digit)
print(min_digit)

#3
n = int(input())

for i in range(1, n + 1):
    t = True

    while i > 0:
        digit = i % 10
        if digit != 0:
            if num % digit != 0:
                t = False
                break
        i = i // 10
    if y:
        print(i, end=" ")
print()

#4
width = int(input())
height = int(input())
border = input()
fill = input()

if width < 3 or height < 3:
    print("Помилка")
else:
    for row in range(height):
        for col in range(width):
            if row == 0 or row == height - 1 or col == 0 or col == width - 1:
                print(border, end=" ")
            else:
                print(fill, end=" ")
        print()
