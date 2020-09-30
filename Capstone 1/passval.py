
def ValidatePassword(myword, mycharacter):
    search=0
    myfound = False
    while search < len(myword) and not myfound:
        if myword[search] == mycharacter:
            myfound = True
        else:
            search = search + 1
    return myfound



def main():
    myword = ["" * 9]
    mycharacter = str()
    myfound = bool()

    myword = ["P", "a", "s", "s", "&", "W", "o", "r", "d"]
    mycharacter = "&"
    myfound = ValidatePassword(myword, mycharacter)
    print(myfound)
main()