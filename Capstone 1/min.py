
def FindMin(numbers):
    smallest_int = 0
    smallest_index=0

    for i in range(0, len(numbers)):
        smallest_int = min(numbers)
        smallest_index = numbers.index(smallest_int)

    return smallest_int, smallest_index


def main():
    # variables
    numbers = [22, 46, 78, 15, 98, 101]
    smallest_int = int()
    smallest_index = int()
    smallest_index=FindMin(numbers)
    smallest_int=FindMin(numbers)
    print(smallest_int, "\t", smallest_index)


main()