def open_file():
    fhand = open("test.txt")
    print(fhand)

    text = fhand.read()
    print(len(text))

    fhand.close()

    fhand = open("test.txt")

    for line in fhand:
        line = line.rstrip()
        print(line.upper())

    print(fhand)

