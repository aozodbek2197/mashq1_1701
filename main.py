# 1-mashq
n = (input("Raqam kiriting: "))

if len(n) == 12:
    if n[:3] == "998":
        if n[3:5] == "99" or n[3:5] == "95":
            print("Uztelecom")
        elif n[3:5] == "97" or n[3:5] == "88":
            print("MobiUz")
        elif n[3:5] == "90" or n[3:5] == "91":
            print("Beeline")
        elif n[3:5] == "94" or n[3:5] == "93":
            print("Ucel")
        else:
            print("Bunday kampaniya yoq!")
    else:
        print("Bu O'zbekiston raqami emas!")
else:
    print("Bunday raqam mavjud emas!")

# 2-mashq
karta = input("karta raqam kiriting")
k = ""

for i in karta:
    if i != " ":
        k += i

print(karta)
print(k)

# 3-mashq
def unformatted_card_number(card_number):
    res = card_number.replace(' ', '')
    if res.isdigit() and len(res) == 16:
        return res
    return res

card_number = input("Karta raqam kiriting: ")
print(unformatted_card_number(card_number))


# 4-mashq
def qoshish(a, b):
    return a + b


def ayirish(a, b):
    return a - b

def kopaytirish(a, b):
    return a * b

def bolish(a, b):
    return a / b

def kalkulyator(num1, amal, num2):
    if amal == '+': return qoshish(a=num1, b=num2)

    elif amal == "-": return ayirish(a=num1, b=num2)

    elif amal == "*": return kopaytirish(a=num1, b=num2)

    elif amal == "/": return bolish(a=num1, b=num2)

    else:
        return "Bunday amal yo'q!"

num1 = int(input("1-sonni kiriting: "))
num2 = int(input("2-sonni kiriting: "))
amal = input("Amalni kiriting (+, -, *, /): ")
res = kalkulyator(num1=num1, num2=num2, amal=amal)
print(res)
