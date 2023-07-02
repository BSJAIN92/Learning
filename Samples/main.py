def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def basics(function_to_run, input_set):

    match function_to_run:
        case "printing":
            return print(input_set)

        case "addition":
            return print(input_set[0] + input_set[1])

        case "str_to_int":
            try:
                return print(int(input_set))
            except:
                print("Incorrect value", input_set)
                quit()

        case "max":
            print(max(input_set))

        case "min":
            print(min(input_set))

        case "type":
            print(type(input_set))

        case "while_countdown":
            i = input_set
            while i > 0:
                print(i)
                i = i - 1


if __name__ == '__main__':
    print_hi('PyCharm')

    function_name = input('What function do you want to run??? ')
    basics(function_name, 5)
