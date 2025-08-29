#Automatic Pizza Order Program.
#Price Menu:
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_small = 2
pepperoni_large = 3
extra_chez = 1
#User order and recipient:
print("Welcome to Kashmiri Food Point.")
pizza = input("Which size you should prefer for pizza, S, M, L:\n").lower()
if pizza == "s" or pizza == "m" or pizza == "l":
# For Regular size pizza.
    if pizza == "s":
        pepperoni = input("Do You Want to Add Pepperoni? (y/n):\n").lower()
        chezz = input("Do you want to add extra chezz? (y/n):\n").lower()
        if pepperoni == "y" and chezz == "y":
            print(f"Your Tottal Bill is {small_pizza + pepperoni_small + extra_chez}$.")
        elif pepperoni == "n" and chezz == "y":
            print(f"Your Tottal bill is {small_pizza + extra_chez}$.")
        elif pepperoni == "y" and chezz == "n":
            print(f"Your Tottal bill is {small_pizza + pepperoni_small}$")
        elif pepperoni == "n" and chezz == "n":
            print(f"Your tottal Bill is {small_pizza}$.")
        else:
            print("Please Choose a Valid Choice")
#For Medium size pizza
    elif pizza == "m":
        pepperoni = input("Do You Want to Add Pepperoni? (y/n):\n").lower()
        chezz = input("Do you want to add extra chezz? (y/n):\n").lower()
        if pepperoni == "y" and chezz == "y":
            print(f"Your Tottal Bill is {medium_pizza + pepperoni_large + extra_chez}$.")
        elif pepperoni == "n" and chezz == "y":
            print(f"Your Tottal bill is {medium_pizza + extra_chez}$.")
        elif pepperoni == "y" and chezz == "n":
            print(f"Your Tottal bill is {medium_pizza + pepperoni_large}$")
        elif pepperoni == "n" and chezz == "n":
            print(f"Your tottal Bill is {medium_pizza}$.")
        else:
            print("Please Choose a Valid Choice")
#for Large size pizza
    elif pizza == "l":
        pepperoni = input("Do You Want to Add Pepperoni? (y/n):\n").lower()
        chezz = input("Do you want to add extra chezz? (y/n):\n").lower()
        if pepperoni == "y" and chezz == "y":
            print(f"Your Tottal Bill is {large_pizza + pepperoni_large + extra_chez}$.")
        elif pepperoni == "n" and chezz == "y":
            print(f"Your Tottal bill is {large_pizza + extra_chez}$.")
        elif pepperoni == "y" and chezz == "n":
            print(f"Your Tottal bill is {large_pizza + pepperoni_large}$")
        elif pepperoni == "n" and chezz == "n":
            print(f"Your tottal Bill is {large_pizza}$.")
        else:
            print("Please Choose a Valid Choice")

else:
    print("""Choose A Valid Choice.
    Good By..""")



#Asadaf Writes...