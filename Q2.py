leapYear = int(input("Leap year:"))
if leapYear % 4 == 0:
    if leapYear % 100 == 0:
        if leapYear % 400 == 0:
            print(leapYear,"is a leap year")
        else:
            print(leapYear,"is not a leap year")
    else:
        print(leapYear,"is a leap year")
else:
    print(leapYear,"is not a leap year")
    
