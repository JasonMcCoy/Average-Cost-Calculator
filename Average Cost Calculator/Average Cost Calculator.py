'''
Here is a Average Cost Calculator which takes your current crypto coin purchases and produces an average cost.
Inspired from this website:
http://www.bullsandthebears.com/vipmember/Average-Down-Calculator.html
'''

x = float(input("How much $ will you be investing?:"))
currentLtcPrice = float(input("What price do you plan on buying LTC?:"))
y = float(input("How much LTC did you originally buy?:"))
z = float(input("What was the price of the LTC you originally bought?:"))

OriginalShares = y
OriginalShares2 = x/currentLtcPrice  # How much LTC do you plan on purchasing?
PurchasePrice = z
PurchasePrice2 = currentLtcPrice



AveragedPricePerShare = ((OriginalShares * PurchasePrice) + (OriginalShares2 * PurchasePrice2)) / (OriginalShares + OriginalShares2)


print("Assuming you originally bought {0} LTC at ${1} and plan on buying '{2}' more LTC, \nif you buy at the price inputted, you must sell your LTC at: ${3} to break-even.".format(OriginalShares, PurchasePrice, OriginalShares2, AveragedPricePerShare))
