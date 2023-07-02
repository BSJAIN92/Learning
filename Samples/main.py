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
                print("Incorrect value")
                quit()

        case "max":
            print(function_to_run)


if __name__ == '__main__':
    print_hi('PyCharm')

    function_name = input('Tell me you want string to int ')
    basics(function_name, "one")
