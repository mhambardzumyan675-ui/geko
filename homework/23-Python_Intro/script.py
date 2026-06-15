#Անձնական այցեքարտ

name=input("Անուն:")
lastname=input("Ազգանուն:")
age=int(input("Տարիք:"))


print("\033[31m", name, "\033[0m")
print("\033[32m", lastname, "\033[0m")
print("\033[34m", age, "\033[0m")


#Աշխատավարձի հաշվիչ

sallary=int((input("Մեկ օրվա աշխատավարձը:")))
quantity=int((input("Օրերի քանակը:")))

print(sallary*quantity)


#Wi-Fi գաղտնաբառի ստուգում

password=input("Password:")

if len(password)>=8:
   print("Վավեր գաղտնաբառ")
else: 
   print("Անվավեր գաղտնաբառ")


#Մուտքի համակարգ

login=input("Enter your login:")
password=input("Enter your password:")

if login=="admin" and password=="123":
     print("Welcome",login)
else:print("Wrong login or password")



#Զեղչի հաշվիչ

price=int(input("Գին:"))

if price>10000:
   print(price-price*0.1)
else:print(price)


#Ֆուտբոլային միավորներ

win=int(input("win:"))
tie=int(input("tie:"))

print(win*3+tie)


#Վառելիքի հաշվիչ

distance=int(input())
consumption=(int(input()))

print((distance*consumption)/100)


# Օնլայն խանութ

price=int(input("Enter price:"))
quantity=int(input("Enter quantity:"))

print(price*quantity)

#Todo ցուցակ

list=[
    "Python",
    "React",
    "Sport",
    "Read",
    "Sleep"
]

for i in list:
   print(i)


#Վաճառքի հաշվետվություն

vacharq=[12000, 15000, 8000, 22000]
total=sum(vacharq)

print(total)