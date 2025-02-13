# task 1 

def mx(a, b):
    if a > b:
        print(a)
    else:
        print(b)

mx(8, 9)

# task 2 

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz" 
    elif number % 5 == 0:
        return "Buzz" 
    else:
        return number

fizz_buzz(11)

# task 3 

def speedometer(speed):
    mx_speed = 70
    points = 0
    if speed < mx_speed:
        print("Ok")
    else:
        over_speed = speed - mx_speed
        points = over_speed // 5
        print(f"points: {points}")
        if points > 12:
            print("License suspended")

speedometer(130)

# task 4 

def showNumbers(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            print(f"{i} EVEN")
        else:
            print(f"{i} ODD")
            
showNumbers(10)
        
# task 5 

def multiplyers(limit):
    for i in range(1, limit + 1):
        if i % 3 == 0 or i % 5 == 0:
            print(i)

multiplyers(30)

# task 6

def show_stars(rows):
    star = "*"
    for i in range(1, rows + 1):
        print(i * star)

show_stars(5)

# task 7

def prime(limit):
    for i in range(2, limit + 1):
        if i == 2 or i == 3 or i == 5 or i == 7:
            print(i)
        elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            print(i)

prime(100)