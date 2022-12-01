# Radha is planning to buy a house that costs $1260000. She is consedring two options:
# Option 1: Make an immidiate downpayment of $300000 and take a loan for 8 years with an interest rate of 10% for ramaing amount.
# option 2: Take a 10 year loan with an interest rate of 10% for entire amount.

#Both the lones are to be paid back in EMI Calculate which loan_Emi is lower.


def emi1(p,r,n):
    pr=p
    ra=r/12
    ti=n
    EMI1=pr * ra * ((1+ra)**ti)/((1+ra)**ti - 1)
    print(EMI1)
    return EMI1
a=emi1(960000,10/100,8)
b=emi1(1260000,8/100,10)
if a<b: 
    print("\n Option 1 is The Best")
else:
    print("Option 2 is the best")


#shyam is currently paying back a home loan for a house he bought few years ago
#  cost of house: 800000
# down payment: 25% of amount
# intrest rate: 7%/annum
#shyam is now buying a car :
# price: 60000
#interest rate: 12%/annum
# time: 1year
# Total Emil for Loan payment

# def emi1(p,r,n):
#     EMI1=p * r * ((1+r)**n)/((1+r)**n - 1)
#     print(EMI1)
#     return EMI1
# a=emi1(600000,7/100,6)
# b=emi1(60000,12/100,1)
# print(a+b)

# You are planning for a trip & you need to decide which city you want to visit. You have shortlisted 4 cities:
# City                 Return flight($)               Hotel/day($)                 weekly Car Rental($)
# Paris                   200                             20                              200
# London                  250                             30                              120
# Dubai                   370                             15                              80
# Mumbai                  450                             15                              70

# (1) If you are planning a week long trip, which city should you visit to spend the least amount of money.



# def emi1(r,h,c):
#     a=r+h*7+c
#     print(a)
#     return a
# b=emi1(200,20,200)
# c=emi1(250,30,120)
# d=emi1(370,15,80)
# e=emi1(450,15,70)
# if b<c:
#     print("Paris is Best")
# elif c<d:
#     print("London is best")
# elif d<e:
#     print("Dubai is best")
# else:
#     print("Mumbai is Best")

# (2) How does your answer change if you change the trip duration to 4days, 10days, 15days.

# def emi1(r,h,c):
#     a=r+h*4+c
#     f=r+h*10+c
#     g=r+h*14+c
#     print(a,f,g)
#     return (a,f,g)
# b=emi1(200,20,200)
# c=emi1(250,30,120)
# d=emi1(370,15,80)
# e=emi1(450,15,70)
# if b<c:
#     print("Paris is Best")
# elif c<d:
#     print("London is best")
# elif d<e:
#     print("Dubai is best")
# else:
#     print("Mumbai is Best")

#(4) If your total budget is 1500$ which city should you visit if you want t minimize the duration of your trip

# def emi1(r,h,c):
#     a=1000/r+h*7+c
#     print(a)
#     return a
# b=emi1(200,20,200)
# c=emi1(250,30,120)
# d=emi1(370,15,80)
# e=emi1(450,15,70)
# if b<c<d<e:
#     print("Paris is Best")
# elif c<d<e:
#     print("London is best")
# elif d<e:
#     print("Dubai is best")
# else:
#     print("Mumbai is Best")

