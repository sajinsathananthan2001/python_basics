try:
    age = int(input('Age: '))
    income = 2000
    risk = income / age 
    print(age)
    print(risk)

except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:
    print('Invalid Value')