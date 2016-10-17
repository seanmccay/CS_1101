def three_lines():
    print()
    print()
    print()


def nine_lines():
    print("Now printing 9 lines...")
    three_lines()
    three_lines()
    three_lines()


def clear_screen():
    print("Now printing 25 lines...")
    for x in range(0,24):
        print()


def main():
    print("Running script: tryme3...")
    nine_lines()
    nine_lines()
    clear_screen()

main()
