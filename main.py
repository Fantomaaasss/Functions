def square_or_fourth_power(a, b, c):
    def process_number(n):
        if n >= 0:
            return n ** 2
        else:
            return n ** 4

    a, b, c = map(process_number, [a, b, c])
    print("Results of calculating : ", a, b, c)

def closer_to_origin(x1, y1, x2, y2):
    distance_A = (x1**2 + y1**2) ** 0.5
    distance_B = (x2**2 + y2**2) ** 0.5

    if distance_A < distance_B:
        print("Point A closer to start of coordinates.")
    else:
        print("Point B closer to start of coordinates.")

def triangle_angles(angle1, angle2):
    angle3 = 180 - (angle1 + angle2)

    if angle1 > 0 and angle2 > 0 and angle3 > 0:
        print("This triangle already exist")
        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            print("A triangle is right-angled.")
        else:
            print("A triangle is not a right triangle.")
    else:
        print("This triangle does not exist.")

def modify_numbers(x, y):
    if x < y:
        x = (x + y) / 2
        y = x * y * 2
    else:
        y = (x + y) / 2
        x = x * y * 2

    print("Changed values: x =", x, ", y =", y)

def point_location(x, y):
    if x == 0 and y == 0:
        print("The point is at the origin of coordinates.")
    elif x == 0:
        print("The point is on the axis Y.")
    elif y == 0:
        print("The point is on the axis X.")
    elif x > 0 and y > 0:
        print("The point is located in the first coordinate corner.")
    elif x < 0 and y > 0:
        print("The point is located in the second coordinate corner.")
    elif x < 0 and y < 0:
        print("The point is located in the third coordinate corner")
    else:
        print("The point is located in the fourth coordinate corner.")

def replace_numbers(a, b):
    if a != b:
        max_val = max(a, b)
        a = max_val
        b = max_val
    else:
        a = 0
        b = 0

    print("Changed values: a =", a, ", b =", b)

def count_negative(a, b, c):
    negative_count = sum(1 for x in [a, b, c] if x < 0)
    print("Number of negative numbers:", negative_count)

def count_positive(a, b, c):
    positive_count = sum(1 for x in [a, b, c] if x > 0)
    print("Number of positive numbers:", positive_count)

def count_integers(a, b, c):
    integer_count = sum(1 for x in [a, b, c] if x.is_integer())
    print("Number of integers:", integer_count)

def divisor_check(a, b, c, k):
    for number in [a, b, c]:
        if number % k == 0:
            print(f"Number {k} is a divisor of the number {number}")

def main():
    # 1
    a = float(input("type in first number: "))
    b = float(input("type in second number: "))
    c = float(input("type in third number: "))
    square_or_fourth_power(a, b, c)

    # 2
    x1 = float(input("Enter the x1 coordinate  for point A: "))
    y1 = float(input("Enter the y1 coordinate  for point A: "))
    x2 = float(input("Enter the x2 coordinate  for point A: "))
    y2 = float(input("Enter the y2 coordinate  for point A "))
    closer_to_origin(x1, y1, x2, y2)

    # 3
    angle1 = float(input("Enter first angle (in degrees): "))
    angle2 = float(input("Enter second angle (in degrees): "))
    triangle_angles(angle1, angle2)

    # 4
    x = float(input("type in first number: "))
    y = float(input("type in second number: "))
    modify_numbers(x, y)

    # 5
    x = float(input("Enter the x coordinate for point A: "))
    y = float(input("Enter the y coordinate for point A: "))
    point_location(x, y)

    # 6
    a = int(input("Type in first integer number: "))
    b = int(input("Type in second integer number: "))
    replace_numbers(a, b)

    # 7
    a = float(input("type in first number: "))
    b = float(input("type in second number: "))
    c = float(input("type in thirth number: "))
    count_negative(a, b, c)

    # 8
    a = float(input("type in first number: "))
    b = float(input("type in second number: "))
    c = float(input("type in thirth number: "))
    count_positive(a, b, c)

    # 9
    a = float(input("type in first number: "))
    b = float(input("type in second number: "))
    c = float(input("type in thirth number: "))
    count_integers(a, b, c)

    # 10
    a = float(input("type in first number: "))
    b = float(input("type in second number: "))
    c = float(input("type in thirth number: "))
    k = float(input("type in number k: "))
    divisor_check(a, b, c, k)

if __name__ == "__main__":
    main()