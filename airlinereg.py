def register():
        sno = []
        custname = []
        address = []
        jr = []
        src = []
        dest = []
        airline = []
        fa = []
        cls = []

        entries = int(input("Total Entries : "))
        for x in range(entries):

            custno = input('Enter customer contact no : ')
            sno.append(custno)

            name = input('Enter name : ')
            custname.append(name)

            custaddr = input('Enter address : ')
            address.append(custaddr)

            jr_date = input('Enter date of journey : ')
            jr.append(jr_date)

            source = input('Enter source : ')
            src.append(source)

            destination = input('Enter destination : ')
            dest.append(destination)

            weight = int(input("Enter Luggage weight(in grams) : "))
            fa.append(weight)

            dom = int(input("1. Domestic\n2. International\n3. Other"))
            print("Airlines Available")
            if dom == 1:
                line = int(
                    input(
                        "\n1.Air India\n2.Indigo\n3.Vistara\n4.GoAir\n5.Spicejet\6.JetAirways\nEnter Airline Name : "
                    ))
                if line == 1:
                    aline = "Air India"
                elif line == 2:
                    aline = "Indigo"
                elif line == 3:
                    aline = "Vistara"
                elif line == 4:
                    aline = "GoAir"
                elif line == 5:
                    aline = "SpiceJet"
                elif line == 6:
                    aline = "JetAirways"
                else:
                    aline = input("Enter Airline Name")
                airline.append(aline)
            elif dom == 2:
                line = int(
                    input(
                        "\n1.Air India\n2.India\n3.Vistara\n4.GoAir\n5.Spicejet\n6.JetAirways\n7.Ethihad\n8.Emirates\n9.Lufthansa\n10.Thai Airways\n11.Qatar\n12.Air France\n13.British Airways\n14.Singapore Airlines\n15.Cathay\nEnter Airline : "
                    ))
                if line == 1:
                    aline = "Air India"
                elif line == 2:
                    aline = "Indigo"
                elif line == 3:
                    aline = "Vistara"
                elif line == 4:
                    aline = "GoAir"
                elif line == 5:
                    aline = "SpiceJet"
                elif line == 6:
                    aline = "JetAirways"
                elif line == 7:
                    aline = "Ethihad"
                elif line == 8:
                    aline = "Emirates"
                elif line == 9:
                    aline = "Lufthansa"
                elif line == 10:
                    aline = "Thai Airways"
                elif line == 11:
                    aline = "Qatar"
                elif line == 12:
                    aline = "Air France"
                elif line == 13:
                    aline = "British Airways"
                elif line == 14:
                    aline = "Singapore"
                elif line == 15:
                    aline = "Cathay"
                else:
                    aline = input("Enter Airline Name")
                airline.append(aline)
            else:
                aline = input("Enter Airline Name")
                airline.append(alike)

            print("Choose Airline class\n1. First Class\n2. Business Class\n3. Economy Class\n")
            saclass = input('Enter Class : ')
            if saclass == 1:
                aclass = "First Class"
            elif saclass == 2:
                aclass = "Business Class"
            elif saclass == 2:
                aclass = "Economy Class"
            else:
                aclass = input("Enter Class name : ")
            cls.append(aclass)

        dict = {
            "S.No": sno,
            "Name": custname,
            "Address": address,
            "Date Of Journey": jr,
            "Source": src,
            "Destination": dest,
            "Load": fa,
            "Airline": airline,
            "Class": cls
        }
        airdf = pd.DataFrame(dict)
        print(airdf, "\n")
        save = input("Would You like to save")
        if save == "y" or "Y":
            fil_name = input("Enter File Name")
            airdf.to_csv("csv/" + fil_name + ".csv")
        else:
            print("Not Saving")

