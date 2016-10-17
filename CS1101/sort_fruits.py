import os


def main():
    # get infile
    if os.path.exists("unsorted_fruits.txt"):
        infile = open("unsorted_fruits.txt", "r")
    else:
        print("Cannot find infile to sort...")
        print("Ending program...")
        exit()

    outfile = open("sorted_fruits.txt", "w")

    # parse infile and build array
    print("Parsing infile...")
    fruits = infile.readlines()

    # remove empty lines
    for item in fruits:
        if item == '\n':
            fruits.remove(item)

    print("Sorting list...")
    fruits.sort()

    print("Writing list to outfile...")
    for fruit in fruits:
        outfile.write(fruit)

    infile.close()
    outfile.close()

    print("Done")


main()
