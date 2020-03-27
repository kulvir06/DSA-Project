import travel_db
import employees
import member_list
import cars_db
names=member_list.name
phno=member_list.number
email=member_list.email_id
passwords=member_list.password


while True:
    p = input("enter phone number\n")
    flagvar = 0
    if p in phno:
        pas = input("enter password\n")
        x = phno.index(p)
        if pas == passwords[x]:
            print("welcome to Karpool", names[x])
            flagvar = 99
        else:
            print("please try again")
    else:
        print("you are not a member")
        print("to access our services you need to become a member first")
        print("press 1 to become a Karpooler")
        print("press 0 to exit")
        choice = int(input())
        if choice == 1:
            print("enter your name")
            newmemname = (member_list.name).append(input())
            print("enter a valid mobile number")
            newmemphno = (member_list.number).append(input())
            print("enter a valid email")
            newmememail = (member_list.email_id).append(input())
            print("create a password")
            newmempass = (member_list.password).append(input())
            print("-----------------------------------------------relogin----------------------------------------------------")
        elif choice == 98:
            print("sorry to see you going")
            break;

    if flagvar == 99:
        print("please select the type of journey")
        print("1.Cab/Taxi")
        print("2.Inter-City")
        print("3.Rental")
        print("To know more about each type of journey please press 0")
        journey = int(input())
        if journey == 1:
            print("please wait while we check the availability")

            print("your driver for the ride will be ",employees.pop())
            print("the car alloted to you is ",cars_db.pop())
            while True:
                print("press 0 on completion of the journey")
                anoin = input()
                if anoin=="0":
                    break




        elif journey == 3:
            print("please wait while we check the availability")
            print("your ride will be delivered by : ", employees.pop())
            print("the car alloted to you is ", cars_db.pop())
            while True:
                print("press 0 on completion of the journey")
                anoin = input()
                if anoin=="0":
                    break


        elif journey == 2:
            print("Please view our travel map")
            for ite in travel_db.destinations:
                print(ite)
            choicetravel1 = int(input())
            print("you have selected your travel plan as ", travel_db.destinations[choicetravel1 - 1])
            print("please wait while we check the availability")
            print("your driver for the ride will be ", employees.pop())
            print("the car alloted to you is ", cars_db.pop())
            while True:
                print("press 0 on completion of the journey")
                anoin = input()
                if anoin=="0":
                    break

        elif journey == 0:
            print("-------------------description of each type--------")
            print("1>Cab/Taxi :-")
            print("This will allot you a car along with a chauffer.")
            print("Please tell the chauffer your destination of choice and you will be droped at your destination.")
            print("Rates will be applied based on the meter fitted in the car")
            print("2>Inter-City :-")
            print("This will allot you a car along with a chauffer.")
            print("This ride will take you across cities.")
            print("Rates will be applied according to the distance between the two cities")
            print("3>Rental")
            print("This is drop off a car for you and will be collected back by our employee after completion of ride")
            print("You will have the car at your liberty")
            print("Any damage done to the car will be added on to the price")
            print("Rates will be applied according to the meter fitted in the car")
            print("please select the type of journey")
            print("1.Cab/Taxi")
            print("2.Inter-City")
            print("3.Rental")
            journey1 = int(input())
            if journey1 == 1:
                print("please wait while we check the availability")
                print("your driver for the ride will be ", employees.pop())
                print("the car alloted to you is ", cars_db.pop())
                while True:
                    print("press 0 on completion of the journey")
                    anoin = input()
                    if anoin == "0":
                        break

            elif journey1 == 3:
                print("please wait while we check the availability")
                print("your car will be dropped by : ", employees.pop())
                print("the car alloted to you is ", cars_db.pop())
                while True:
                    print("press 0 on completion of the journey")
                    anoin = input()
                    if anoin == "0":
                        break

            elif journey1 == 2:
                print("Please view our travel map")
                for ite in travel_db.destinations:
                    print(ite)
                choicetravel1=int(input())
                print("you have selected your travel plan as ",travel_db.destinations[choicetravel1-1])
                print("please wait while we check the availability")
                print("your driver for the ride will be ", employees.pop())
                print("the car alloted to you is ", cars_db.pop())
                while True:
                    print("press 0 on completion of the journey")
                    anoin = input()
                    if anoin == "0":
                        break

            else:
                print("invalid choice please re-login")

        else:
            print("invlaid choice please re-login")
    print("thank you for choosing KarPool\n\n\n\n\n")
    print("we are logging you out automatically for safety reasons")
    print("press 1 to re-login")
    finalcheck = int(input())
    if finalcheck != 1 :
        print("you have pressed the wrong button and hence all unsaved data has been deleted for safety reasons")
        break

