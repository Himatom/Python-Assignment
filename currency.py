amount = int(input("Enter amount: "))
denomination = int(input("Enter denomination: "))
denominations = [100,50,20,10,5,2,1]

match denomination:
    case 100: 
        count100 = amount/100
        var = amount - (count100*100)
        