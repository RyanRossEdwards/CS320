def main():
    print("Enter Amount in dollars $ (0 to exit)")

    try:
        # Without rounding
        # amount = int(float(input()) * 100)

        # With rounding
        amount = round(float(input())*10)*10

        if amount == 0:
            return False
        
        change = cashier(amount)

        if type(change) == list:
            change = [(lambda x: x/100)(i) for i in cashier(amount)]

        print(amount/100, change)

    except ValueError:
        print("Invalid input")

    return True


# Takes amount (as cents / integer) as input
def cashier(amount):
    # NZ Denominations
    denominations = [10,20,50,100,200,500,1000,2000,5000,10000]
    change = []

    try:
        while amount > 0:
            largest_coin = None

            for coin in denominations:
                if coin <= amount:
                    largest_coin = coin
                elif largest_coin == None:
                    raise ValueError
                else:
                    break

            amount = amount - largest_coin
            change += [largest_coin]

    except ValueError:
        change = "No Exact Change"

    return change



run = True
while run:
    run = main()



# Some Notes:
    # There is an issue with handling floats
    # run 1.3 - 1.0 and get 0.300000...4???

    # change = cashier(amount)
    # lambda notes:
    # >>> a = lambda x: x*2
    # >>> b = [1,2,3]
    # >>> [a(i) for i in b]
    # [2, 4, 6]
    # >>> [(lambda x: x*2)(i) for i in b]
