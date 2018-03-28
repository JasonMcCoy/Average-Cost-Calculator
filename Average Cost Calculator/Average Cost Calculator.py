'''
Here is a Average Cost Calculator which takes your current crypto coin purchases and produces an average cost.

Inspired from this website:
http://www.bullsandthebears.com/vipmember/Average-Down-Calculator.html
'''

OriginalShares = 9.5396
OriginalShares2 = 18.8
PurchasePrice = 187.17
PurchasePrice2 = int(input("Please enter your target LTC $ Price: "))



AveragedPricePerShare = ((OriginalShares * PurchasePrice) + (OriginalShares2 * PurchasePrice2)) / (OriginalShares + OriginalShares2)

print(AveragedPricePerShare)