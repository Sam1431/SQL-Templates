 def register():
        Name = []
        Pname = []
        Tnum = []
        Pnum = []
        Snum = []
        Age = []
        TrainNo = []
        Tclass = []
        Amt = []

        entries = int(input("Total Entries : "))
        for x in range(entries):
            name = input("enter train name :")
            Name.append(name)

            tnum = int(input("enter train number :"))
            Tnum.append(tnum)

            snum = int(input("Enter number of seats : "))
            Snum.append(snum)

            pnum = int(input("Enter number of passengers : "))
            Pnum.append(pnum)

            pname = input("enter passenger name : ")
            Pname.append(pname)

            age = input("enter passenger age : ")
            Age.append(age)

            tcls = int(input("1.AC First Class\n2.AC Second Class\n3.AC Third Class\n4.Sleeper Class\nEnter your choice:"))
            if tcls == 1:
                tclass = 'ac1'
            elif tcls == 2:
                tclass = 'ac2'
            elif tcls == 3:
                tclass = 'ac3'
            else:
                tclass = input("Enter Class")
            Tclass.append(tclass)
        
        dict = {
            "Train Number": Tnum,
            "Name": Pname,
            "Number of seats ": Snum,
            "Train Name": Name,
            "Age": Age,
            "Train Class": Tclass,
        }
        traindf = pd.DataFrame(dict)
        print(traindf, "\n")
        save = input("Would You like to save : ")
        if save == "y" or "Y":
            fil_name = input("Enter File Name : ")
            traindf.to_csv("csv/railway/" + fil_name + ".csv")
        else:
            print("Not Saving")
