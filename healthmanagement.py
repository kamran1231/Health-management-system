

import datetime

def get_date():
    return datetime.datetime.now()

def take_data(k):
    if k == 1:
        print(' 1. for exercise: \n 2. for food: ')
        c = int(input('Enter your choice: '))
        if c == 1:
            value = input('enter your exercise name: ')
            with open('kamran-ex.txt','a') as op:
                op.write(str([str(get_date())]) +': '+value)
            print('Successfully Exercise Added')
        elif c == 2:
            value = input('Enter the food name: ')
            with open('kamran-food.txt','a') as op:
                op.write(str([str(get_date())]) +': '+value)
            print('Successfully Food Added')

    elif k == 2:
        print(' 1. for exercise: \n 2. for food: ')
        c = int(input('Enter your choice: '))
        if c == 1:
            value = input('Enter your exercise name: ')
            with open('aisha-ex.txt','a') as op:
                op.write(str([str(get_date())]) + ': ' + value)
                print('Successfully Exercise Added')
        elif c == 2:
            value = input('Enter your food name: ')
            with open('aisha-food.txt','a') as op:
                op.write(str([str(get_date())]) + ': ' + value)
                print('Successfully food Added')
    elif k == 3:
        print(' 1. for exercise: \n 2. for food: ')
        c = int(input('Enter your choice: '))
        if c == 1:
            value = input('Enter the exercise name: ')
            with open('abrar-ex.txt','a') as op:
                op.write(str([str(get_date())]) + ': '+ value)
                print('Successfully Exercise Added')

        elif c == 2:
            value = input('Enter the Food name: ')
            with open('abrar-food.txt', 'a') as op:
                op.write(str([str(get_date())]) + ': ' + value)
                print('Successfully food Added')

def retrieve(k):
    if k == 1:
        print(' 1. for exercise: \n 2. for food: ')
        c = int(input('Enter your choice: '))
        if c == 1:
            with open('kamran-ex.txt') as op:
                for i in op:
                    print(i,sep='\n')
        elif c == 2:
            with open('kamran-food.txt') as op:
                for i in op:
                    print(i,sep='\n')

    if k == 2:
        print(' 1. for exercise: \n 2. for food: ')
        c = int(input('Enter your choice: '))
        if c == 1:
            with open('aisha-ex.txt') as op:
                for i in op:
                    print(i, end=' ')
        elif c == 2:
            with open('aisha-food.txt') as op:
                for i in op:
                    print(i,end=' ')
    if k == 1:
        print(' 1. for exercise: \n 2. for food: ')
        c = int(input('Enter your choice: '))
        if c == 1:
            with open('abrar-ex.txt') as op:
                for i in op:
                    print(i, end=' ')
        elif c == 2:
            with open('abrar-food.txt') as op:
                for i in op:
                    print(i,end=' ')







while 1:
    print('Welcome to my Health management system: ')
    print(' 1. for Add value: \n 2. for Retrieve value:')
    ch = input('Enter your choice: ')

    if ch == '1':
        print(' 1. for Kamran: \n 2. for Aisha: \n 3. for Abrar: ')
        ch = int(input('Enter you choice: '))
        take_data(ch)

    elif ch == '2':
        print(' 1. for Kamran: \n 2. for Aisha: \n 3. for Abrar: ')
        ch = int(input('Enter your choice: '))
        retrieve(ch)
