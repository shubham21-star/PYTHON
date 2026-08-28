# Election Commision System
age = int(input("Enter your age:"))
has_ID = str(input("Enter Yes or No:")).lower()

if(age>=18 and has_ID == "yes"):
    print("Your are eligiable to VOTE")
else:
    print("You are not eligiable to VOTE")


#Game
TP = int(input("Enter Total No. of Player:"))

if( TP % 2 == 0):
    print("Able to play Game (TP = Even)")
else:
    print("Not able to play Game (TP = Odd)")

#Leap
year = int(input("Enter year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# DAY
day = str(input("Enter Today DAY:")).lower() 
 
if(day == "staurday" and day == "sunday"):
    print("Today is Weekend")
else:
    print("Today is Weekday")

#CGPA
cgpa = float(input("Enter Today DAY:")) 
 
if(cgpa >= 2.0):
    print("Your are graduate")
else:
    print("Improve your grade")

#saving
money = int(input("Enter your saving $:")) 
 
if(money >= 10 and money <= 100):
    print("Your Saving are within range")
else:
    print("Your Saving are not within range")

#assisment
score = int(input("Enter your score:")) 
 
if(score % 2 == 0 and score % 3 == 0 and 9 != score >= 5):

    print("Your are Eligiable for extra CREDIT")
else:
    print("Doesn't Eligiable for extra CREDIT")

#Shopping mall
spend = int(input("Enter your Spending Amount $:")) 
age = int(input("Enter your age:"))
 
if(spend >= 100 or age >= 60):

    print("Your are Eligiable for 20% Discount") 
else:
    print("Doesn't Eligiable for 20% Discount")

#Password checker
password = input("Enter your Password :")

if(len(password) >= 8 and password[0].isupper() and password[-1].islower()):
    print("Strong Password! Your Account is Secure") 
else:
    print("Weak Password! Your Account is not Secure")

