def count_sum_avg_of_input():
    print("Hi")

    count = 0
    total = 0
    average = 0

    while True:
        try:
            num = input("Please enter a number: \n")
            if num != "Done":
                num = int(num)
                count = count + 1
                total = total + num
            else:
                break
        except:
            print("Please input a valid number. \n")
            continue

    average = total / count

    print("The count is: ", count)
    print("The total is: ", total)
    print("The average is: ", average)
