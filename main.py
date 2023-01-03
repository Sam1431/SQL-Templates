import os
import platform
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def airways():
    def register():
        sno = []
        custname = []
        address =[]
        jr = []
        src =[]
        dest = []
        airline = []
        fa = []
        cls = []


        entries = int(input("Total Entries : "))
        for x in range(entries):
            custno=input('Enter customer no : ')
            sno.append(custno)
            name=input('Enter name : ')
            custname.append(name)
            custaddr=input('Enter address : ')
            address.append(custaddr)
            jr_date=input('Enter date of journey : ')
            jr.append(jr_date)
            source=input('Enter source : ')
            src.append(source)
            destination=input('Enter destination : ')
            dest.append(destination)
            weight = int(input("Enter Luggage weight(in grams) : "))
            fa.append(weight)
            dom = int(input("1. Domestic\n2. International\n3. Other"))
            print("Airlines Available")
            if dom==1:
                line = int(input("1. Air India\n2. Indigo\n3. Vistara\n4. GoAir\n5. Spicejet\6. JetAirways"))
                airline.append(line)
            elif dom==2:
                line = int(input("1. Air India\n2. India\n3. Vistara\n4. GoAir\n5. Spicejet\n6. JetAirways\n5. Ethihad\n6. Emirates\n7. Lufthansa\n8. Thai Airways\n9. Qatar\n10. Air France\n11. British Airways\n12. Singapore Airlines\n13. Cathay"))
                airline.append(line)
            else:
                line = input("Enter Airline Name : ")
                airline.append(line)

            print("Choose Airline class\n1. First Class\n2. Business Class\n3. Economy Class\n")
            aclass=input('Enter Class : ')
            cls.append(aclass)



        dict = { "S.No":sno, "Name": custname, "Address": address, "Date Of Journey": jr, "Source": src, "Destination": dest }
        airdf = pd.DataFrame(dict)
        print(airdf,"\n")
        save = input("Would You like to save")
        if save == "y" or "Y":
            fil_name = input("Enter File Name")
            airdf.to_csv(fil_name+".csv")
        else:
            print("Not Saving")
    register()

def carrental():
    CA = []
def railways():
    RW = []
def cruise():
    CR = []



print("Transportation Management System")
print("================================")
print("1. Airway\n2. Car Rental\n3. Railways\n4. Cruise\n")

mode = int(input("Enter Tranportation method : "))
if mode==1:
       airways()
elif mode==2:
       print("heh")
elif mode==3:
       print("heh")
elif mode==4:
       print("heh")
else:
       print("heh")
