try:
    age=int(input('Age: '))
    income=2000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:
    print('Invalide datatype: age should be a number ')
