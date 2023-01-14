import os
import platform
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def register():
        Sno = []
        Name = []
        Id = []
        Bookname = []
        Duration = []
        Amt = []

        entries = int(input("Total Entries : "))
        for x in range(entries):
            sno = int(input("Enter serial number : "))
            Sno.append(sno)

            name = input("Enter member name  : ")
            Name.append(name)

            mid = input("Enter member ID : ")
            Id.append(mid)

            bname = input("Enter name of the Book : ")
            Bname.append(bname)

            dur = input("Enter duration for Borrowing : ")
            Duration.append(dur)

            amt = input("Enter amount : ")
            Amt.append(amt)
        
        dict = {
            "Sno": Sno,
            "Name": Name,
            "ID": Id,
            "Book name": Bname,
            "Duration": Duration,
            "Amount": Tclass,
        }
        libdf = pd.DataFrame(dict)
        print(libdf, "\n")
        save = input("Would You like to save : ")
        if save == "y" or "Y":
            fil_name = input("Enter File Name : ")
            libdf.to_csv("csv/" + fil_name + ".csv")
        else:
            print("Not Saving")
