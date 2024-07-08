# Take 2 strings and return 1 string with the elements in every other order.
# John Kowal  -  WALTER$
def mix():
    print()
    print('Enter the first string, then a comma with no spaces, then enter the second string.')
    stringA, stringB = input('Enter stringA,stringB:').split(',')

    i = j = 0
    result = ""
    while i < len(stringA) or j < len(stringB):
        if i < len(stringA):
            result += stringA[i]
            i += 1
        if j < len(stringB):
            result += stringB[j]
            j += 1
    return result

print(mix())