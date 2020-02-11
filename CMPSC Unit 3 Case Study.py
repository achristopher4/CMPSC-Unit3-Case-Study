#Case Study 2/11/20 CMPSC 101
#Input 
askInvest = float(input("Enter the amount: "))
askYears = int(input("Enter the number of years: "))
askRate = float(input("Enter the rate as a %: "))

#algorithm
years = list(range(1,6))
rate = askRate / 100
findNew = 0

for numbers in range(1, askYears + 1):
    startBalance = askInvest
    interest = rate * askInvest 
    askInvest = interest + askInvest
    findNew = interest + findNew
    print(numbers, "%0.2f" % startBalance, "%0.2f" % interest, "%0.2f" % askInvest) 
    

#output
endBalance = print("$%0.2f" % askInvest)
totalInterest = print("$%0.2f" % findNew)
