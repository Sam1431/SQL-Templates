def register():
        Sno = []
        DrugName = []
        Desc = []
        Dose = []
        Qty = []
        Cost = []

        entries = int(input("Total Entries : "))
        for x in range(entries):
            sno = int(input("S.no number : "))
            Sno.append(sno)

            drugname = input("Medicine name : ")
            DrugName.append(drugname)
                
            desc = input("Medicine Desciption : ")
            Desc.append(desc)

            dose = input("For how much days is the medicin prescribed for : ")
            Dose.append(dose)

            qty = input("Quantity : ")
            Qty.append(qty)

            cost = input("Price : ")
            Cost.append(cost)
        
        dict = {
            "Sno": Sno,
            "Medicine Name": Name,
            "Description": Desc,
            "Dosage": Dose,
            "Quantity": Qty,
            "Cost": Cost,
        }
        phrdf = pd.DataFrame(dict)
        print(phrdf, "\n")
        save = input("Would You like to save : ")
        if save == "y" or "Y":
            fil_name = input("Enter Patient Name : ")
            phrdf.to_csv("csv/" + fil_name + ".csv")
        else:
            print("Not Saving")
