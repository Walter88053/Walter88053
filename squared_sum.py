# Take an array of numbers as a parameter and return the sum of each number in the array squared.
# John Kowal  -  WALTER$

def squared_sum():
    PROMPT = ("Enter numbers that get squared and then added to return the sum. "
              "Input 0 when finished: ")
    total = 0
    ele = 0
    num_list = []
    response = eval(input(PROMPT))
    while response != 0:
        num_list.append(response)
        response = eval(input(PROMPT))
    for num in num_list:
        total += num ** 2

    print("The sum of the squared numbers is", total)
squared_sum()