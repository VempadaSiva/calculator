def calculator(start):
    
    while start:
        operation = input('enter which type of operation you need: add/sub/mul/div/stop: ')
        if operation == 'stop':
            start = False
            continue
        input1 = int(input('enter a number:'))
        input2 = int(input('enter other number: '))
        if operation == 'add':
            print('Add of given numbers: ', input1+input2)
        elif operation == 'sub':
            print('substract of given numbers: ', input1-input2)
        elif operation == 'mul':
            print('Multiply of given numbers: ', input1*input2)
        elif operation == 'div':
            print('division of given numbers: ',input1/input2)
        
        else:
            return ' onvalid operaton'
if __name__ == '__main__':
    calculator(start=True)