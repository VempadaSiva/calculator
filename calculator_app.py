import sys

def calculator(start, input1=None, input2=None, operation=None):
    while start:
        if not operation:
            operation = input('Enter which type of operation you need: add/sub/mul/div/stop: ')

        if operation == 'stop':
            start = False
            continue

        if input1 is None:
            input1 = int(input('Enter a number: '))  # First number

        if input2 is None:
            input2 = int(input('Enter another number: '))  # Second number

        if operation == 'add':
            print('Addition of given numbers:', input1 + input2)
        elif operation == 'sub':
            print('Subtraction of given numbers:', input1 - input2)
        elif operation == 'mul':
            print('Multiplication of given numbers:', input1 * input2)
        elif operation == 'div':
            print('Division of given numbers:', input1 / input2)
        else:
            print('Invalid operation')
            return

        # Ask for operation again or stop
        operation = input('Enter which type of operation you need: add/sub/mul/div/stop: ')

if __name__ == '__main__':
    # Check if there are command-line arguments
    if len(sys.argv) > 1:
        # Extract values from command-line arguments
        try:
            operation = sys.argv[1]  # First argument
            input1 = int(sys.argv[2])  # Second argument
            input2 = int(sys.argv[3])  # Third argument
            calculator(start=True, input1=input1, input2=input2, operation=operation)
        except IndexError:
            print("Please provide operation, input1, and input2 as arguments.")
        except ValueError:
            print("Please ensure input1 and input2 are integers.")
    else:
        # Default case: Run interactively
        calculator(start=True)
