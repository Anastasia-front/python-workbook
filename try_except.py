while True:
    age = input("How old are you? ")
    try:
        age = int(age)
        if age >= 18:
            print("Access allowed")
            break
        else:
            print("Access denied")
            break
    except ValueError:
        print(f"{age} is not a number. Please enter a number")
    finally:
        print("-" * 30)

print('.'*50)


while 1:
    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))

    try:
        if a==0 or \
                b==0:
            print("Please do not use zero")
        else:
            print(f'a/b={a}/{b}={a/b}')
            break
    except Exception as error:
        print(f'Error: {error}')
    finally:
        print('Program is finished')