
def FindToys(toys, search_item):
    pos = 0
    found = False
    while pos < len(toys) and not found:
        if toys[pos] == search_item:
            found = True
        else:
            pos = pos + 1
    return found

def main():
    toys = ["ball", "doll", "bat", "puzzle", "legos", "Barbie", "truck"]
    search_item = "bat"
    found_item = bool
    # call search function
    found_item = FindToys(toys, search_item)
    print(found_item)
main()


