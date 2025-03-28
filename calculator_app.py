import sys

def calculator(start, operation=None, input1=None, input2=None):
    while start:
        if not operation:
            print("Operation is required.")
            break

        if operation == 'stop':
            start = False
            continue

        if input1 is None or input2 is None:
            print("Both input1 and input2 are required.")
            break

        # Perform the requested operation
        if operation == 'add':
            print(f'Addition of {input1} and {input2}:', input1 + input2)
        elif operation == 'sub':
            print(f'Subtraction of {input1} and {input2}:', input1 - input2)
        elif operation == 'mul':
            print(f'Multiplication of {input1} and {input2}:', input1 * input2)
        elif operation == 'div':
            if input2 != 0:
                print(f'Division of {input1} and {input2}:', input1 / input2)
            else:
                print("Cannot divide by zero!")
        else:
            print("Invalid operation!")
            break

        start = False  # End the loop after one operation for this example.

if __name__ == '__main__':
    # Ensure the user has provided enough arguments
    if len(sys.argv) < 4:
        print("Please provide operation, input1, and input2 as command-line arguments.")
    else:
        operation = sys.argv[1]
        input1 = int(sys.argv[2])
        input2 = int(sys.argv[3])
        calculator(start=True, operation=operation, input1=input1, input2=input2)
