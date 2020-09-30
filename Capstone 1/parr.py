def FindHighest(names, calls):
  highest_calls = 0
  highest_name=0


  for i in range(0, len(calls)):
      highest_calls = max(calls)
      n = calls.index(highest_calls)
      highest_name = names[n]

  return highest_name, highest_calls


def main():
    #variables
    names = ["Bob", "Mary", "Sue", "John", "Mike", "Becky"]
    calls = [20, 11, 15, 32, 17, 28]
    highest_name = str()
    highest_calls = int()

    highest_name, highest_calls = FindHighest(names, calls)
    print(highest_name, "\t", highest_calls)
main()