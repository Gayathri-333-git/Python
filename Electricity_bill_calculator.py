units = int(input("Enter a number of units: "))
if units >= 0 and units <= 100:
    bill = units * 2
    print(bill)
elif units <= 200:
    bill1 = (100 * 2) + (units - 100) * 3
    print(bill1)
elif units <=300:
    bill2 =(units - 100) * 5
    print(bill2)
else:
    bill3 =(units - 100) * 7
    print(bill3)


