
#Fonction which allow to create the list with the differents category
def Create_List_Budget(Current_List = None):

    Month = None #récupération du mois

    if Current_List != None:
        Current_List[0] = Month
        return Current_List

    Budget = [Month]
    Control = True
    Choice = "A"

    while Control :
        
        print("\nSaisissez ce que vous voulez faire : \n Si vous voulez supprimer la dernière catégorie tapez D \n si vous voulez arrêtez la saisie tapez S \n Si voulez ajouter une autre catégorie tapez autre chose\n")
        Choice = input("Votre choix : ")

        if Choice == "D" or Choice == "d":
            Budget.pop()
        elif Choice =="S" or Choice == "s": 
            Control = False
        else :
            New_Category = input("\nSaisie de la nouvelle catégorie : ")
            New_Price = float(input("\nMettre un prix (la virgule se fait à l'aide d'un point) :  ")) 
            Budget.append([New_Category,New_Price])

        print("\nVoici votre budget pour l'instant : \n\n -----\n")
        for i in range(1,len(Budget)):
            print("Catégorie : {}, Budget : {}".format(Budget[i][0],Budget[i][1]))
        print("\n ----- \n")

    Spending = [Month]

    return Budget, Spending


#Fonction which allow to modify the Budget list
def Manage_budget(Current_list)

    Control = True
    
    while Control:
        print("\nSaisissez ce que vous voulez faire : \n Si vous voulez ajouter une catégorie tapez A \n Si vous voulez changer le prix d'une catégorie tapez C \n si vous voulez supprimer une catégorie tapez S \n Si voulez arreter tapez autre chose\n")




        



