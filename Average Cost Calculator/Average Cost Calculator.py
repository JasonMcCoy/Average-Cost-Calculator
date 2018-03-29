'''
Here is a Average Cost Calculator which takes your current crypto coin purchases and produces an average cost.
Inspired from this website:
http://www.bullsandthebears.com/vipmember/Average-Down-Calculator.html
'''

OriginalShares = 9.5396
OriginalShares2 = 20  # How much LTC do you plan on purchasing?
PurchasePrice = 187.17
PurchasePrice2 = int(input("Please enter your target LTC $ Price: "))



AveragedPricePerShare = ((OriginalShares * PurchasePrice) + (OriginalShares2 * PurchasePrice2)) / (OriginalShares + OriginalShares2)


print("Assuming you originally bought {0} LTC at ${1} and plan on buying '{2}' more LTC, \nif you buy at the price inputted, you must sell your LTC at: ${3} to break-even:".format(OriginalShares, PurchasePrice, OriginalShares2, AveragedPricePerShare))
