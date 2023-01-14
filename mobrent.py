def register():
        sno = []
        driver = []
        numPlt = []
        carType = []
        driverAddr = []
        rent = []
        days = []

        entries = int(input("Total Entries : "))
        for x in range(entries):

            driverno = input('Enter driver contact no : ')
            sno.append(driverno)

            drivername = input('Enter driver name: ')
            driver.append(drivername)

            numberplate = input('Enter number plate of vehicle rented : ')
            numPlt.append(numberplate)

            cinput = int(
                input(
                    "1.SUV (6 people)\n2.Hatchback ( 4 People )\n3.Nano ( 4 people )\n4.Bike/Scooty ( 2 people )\n5.Van ( 14 people )\n==========\nEnter Vehicle rented : "
                ))
            if cinput == 1:
                cartype = "SUV"
            elif cinput == 2:
                cartype = "Hatchback"
            elif cinput == 3:
                cartype = "Nano"
            elif cinput == 4:
                cartype = "Bike/Scooty"
            elif cinput == 5:
                cartype = "Van"
            else:
                print("invalid input")
            carType.append(cartype)

            address = input('Enter address of driver : ')
            driverAddr.append(address)

            fee = input('Enter rent owed by driver : ')
            rent.append(address)

            dur = input('Enter how many days is the vehicle rented for')
            days.append(address)

        dict = {
            "Contact Number": sno,
            "Name": drivername,
            "Address": driverAddr,
            "Journey Duration": days,
            "Rent Amt": rent,
            "Vehicle Type": carType,
            "Number Plate": numPlt
        }
        vehidf = pd.DataFrame(dict)
        print(vehidf, "\n")
        save = input("Would You like to save : ")
        if save == "y" or "Y":
            fil_name = input("Enter File Name : ")
            vehidf.to_csv("csv/roadway/" + fil_name + ".csv")
        else:
            print("Not Saving")
