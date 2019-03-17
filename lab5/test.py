katt = 4
print(katt)
katt += 1
print(katt)

print("å">"ä")

alphabet = list('abcdefghijklmnopqrstuvwxyzåäö')
alphabet.sort()
print(alphabet)
a = ["a","c","b","å","ä","ö"]
a.sort()

print("Det här tycker python är sorterat i bokstavsordning", a)
print(ord("å"))
print(ord("ä"))
print(ord("ö"))


"""
def rek(l):
    if len(l) > 0:
        print(l)
        rek(l[1:])          #först skickar denna 5 -> 1, sen bara 1 -> tänk igenom alla rekursioner - > Blir lite kaos i huvudet




l = [3, 5, 1]

rek(l)
"""