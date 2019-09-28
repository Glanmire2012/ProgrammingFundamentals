#Script: ProjectR00038222
#Author: Owen Sheehan (R00038222)
#Description: Studio Booking form

#Declare constants
day1Rate=260
day2to4Rate=240
day5to8Rate=210
day9PlusRate=200
creditCardLevy=1.05
cashReduction=0.95
sessMusicianDay=100
#Declare variables
totalCost=0
okay=True



try:
    while okay:
        #Request user to give Contact details
        groupName=input("Please enter the name of your Group:")
        #Create a file with the bands name
        bookingConf = open("booking"+groupName+".txt",'w')
        test = True
        while test:
            try:
            #Test group size to make sure its a number

                groupSize=int(input("Please enter the size of your Group (1 to 8):"))
                if groupSize <= 0:
                    print("Please only enter numbers greater than 0!")
                elif groupSize >= 9:
                    print("Please enter only numbers between 1 and 8!")
                else:
                    test=False
            except:
                print("Error please only use numbers!")
        #Write the start of the booking confirmation
        bookingConf.write("Booking Application\n-------------------\nBand Name:"+groupName+"\n")
        managerName=input("Please enter the Name of the Group Manager:")
        managerEmail=input("Please enter the Managers Email:")
        try:
            #test the phone number with a while and for loop to make sure its all numbers
            test=True
            while test:
                managerPhone=input("Please enter the Contacts Mobile phone number:")
                phoneLenght=len(managerPhone)
                for digit in range(phoneLenght):
                    testDigit=managerPhone[digit].isdigit()
                    if testDigit==False:
                        print("Please enter only Numbers for the mobile phone number!")
                        break
                    else:
                        test=False
        except:
            print("Error with Phone number!")
        test=True
        digit=0
        while test:
            try:
                #Test that only numbers used in date
                startDate=input("What start date are you looking for (ddmmyyyy)")
                startDateLenght=len(startDate)
                for digit in range(startDateLenght):
                    testDigit=startDate[digit].isdigit()
                    if testDigit==False:
                        print("Please enter the date only in numeric format dates (ddmmyyyy)!")
                        break
                    else:
                        test=False
            except:
                print("Please enter only numbers!")
        bookingLenght=int(input("Please enter the number of days you want to book for:"))
        bookingConf.write("Requested By:"+managerName+"(Contact:"+managerEmail+" and "+managerPhone+")\nDate Requested "+startDate+"\nBand Members\n------------\n")
        #For loop to Request and write band member names to file
        for member in range(groupSize):
            memberNum=member+1
            memberName=input(f"What is the name of member {member+1}?")
            memberInstrument=input("What is "+memberName+"'s instrument?")
            bookingConf.write(str(memberNum)+":"+memberName+"-"+memberInstrument+"\n")

        test=True
        while test:
            try:
                # Request the number of Session musicians required.
                sessMusicianNo = int(input(f"There is room for {8-groupSize} session musicians - how many do you want?"))
                if sessMusicianNo<0:
                    print("Please do not enter negative numbers")
                elif sessMusicianNo>8-groupSize:
                    print("You may only request a maximum of ",8-groupSize," session musicians")
                else:
                    test=False
            except:
                print("Please only enter numbers!!")

        test=True
        while test:
            #test for valid input for payment type. 
            try:
                print("Please Select a payment method:\t(1)Credit card (5% levy)")
                print("\t\t\t\t\t\t\t\t(2)Cheque")
                print("\t\t\t\t\t\t\t\t(3)Cash (5% discount)")
                paymentMethod = int(input("\t\t\t\t\t\t\t\t:"))
                if paymentMethod<=0 or paymentMethod>=4:
                    print("Please only enter Numbers between 1 and 3!")
                else:
                    test=False
            except:
                print("Plaese enter only numbers!!!")
        #For loop to calculate the cost of the entered amount of days and session musicians
        for days in range(bookingLenght):
            dayCount=days+1
            if dayCount>bookingLenght:
                continue
            elif dayCount==1:
                totalCost=totalCost+day1Rate+sessMusicianDay*sessMusicianNo
            elif dayCount<=4:
                totalCost=totalCost+day2to4Rate+sessMusicianDay*sessMusicianNo
            elif daycount<=8:
                totalCost=totalCost+day5to8Rate+sessMusicianDay*sessMusicianNo
            elif dayCount>=9:
                totalCost=totalCost+day9PlusRate+sessMusicianDay*sessMusicianNo
            else:
                break


        bookingConf.write("Price includes "+str(sessMusicianNo)+" session musicians Per day.\nThe total payment will be ")
        # Calculate final cost based on payment method
        if paymentMethod == 1:
            totalCost = totalCost * creditCardLevy
            bookingConf.write(str(totalCost)+" which includes a 5% credit card levy.")
        elif paymentMethod == 3:
            totalCost = totalCost * cashReduction
            bookingConf.write(str(totalCost)+ " which includes a 5% reduction for paying in cash.")
        else:
            bookingConf.write(str(totalCost)+ " which will be paid by Cheque")
        bookingConf.close()
        bookingConf = open("booking" + groupName + ".txt")
        nextLine=bookingConf.readline()
        while nextLine != '':
            print(nextLine.rstrip())
            nextLine = bookingConf.readline()
        bookingConf.close()
        okay=False

except IOError as err:
    print("Could not find file\n\t", err)
    bookingConf.close()  # Closes the file in the event of an error
except ZeroDivisionError:
    print("File", newfile.name, "did not contain any values")
    bookingConf.close()  # Closes the file in the event of an error
except:
    print("Error while running program.")
    bookingConf.close()  # Closes the file in the event of an error