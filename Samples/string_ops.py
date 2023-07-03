def basics(function_to_run, input_set):

    match function_to_run:
        case "printing":
            return print(input_set)

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

        case "type_dir":
            print(type(input_set))
            print(dir(input_set))

        case "while_countdown":
            i = input_set
            while i > 0:
                print(i)
                i = i - 1

        case "for_count_list":
            for i in [1, 2, 3, 4, 5]:
                print(i)

        case "for_largest_list":
            largest_num = 0
            for num in [10, 20, 50, 21, 34]:
                if num > largest_num:
                    largest_num = num
            print(largest_num)

        case "count_sum_avg_of_input":
            count_sum_avg_of_input()

        case "for_string":
            for letter in "letter":
                print(letter)

        case "slicing":
            s = "your name is"
            print(s[4:8])
            print(s[:8])
            print(s[8:])

        case "string_concat":
            a = input("Enter the first string: \n")
            b = input("Enter the second string: \n")
            print(a + b)

        case "string_search_letter":
            a = input("Enter the string: \n")
            b = input("Enter the search letter: \n")
            print(b in a)
