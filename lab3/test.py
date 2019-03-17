def rek(l):
    if len(l) > 0:
        print(l)
        rek(l[1:])          #först skickar denna 5 -> 1, sen bara 1 -> tänk igenom alla rekursioner - > Blir lite kaos i huvudet




l = [3, 5, 1]

rek(l)