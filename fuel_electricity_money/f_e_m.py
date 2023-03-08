
# fuel and electricity
# =====================


def redo():
    rerun = "y"
    while rerun == "y":
        rerun = input("rerun? (y/n) ")
        if rerun == "y":
            fuel()

        else:
            exit()


#1 fuel price
# start of function ======================
def fuel(money, litre_cost):
    # cost = 24
    litres_of_fuel = (money // litre_cost)

    conclusion =  f"\nYou can purchase roughly {litres_of_fuel} litres of fuel for R{money}, at R{litre_cost} per litre"
    return conclusion

# end of function ======================
# print(fuel(1000, 23))

# a = int(input("Enter an amount in rands: "))
# b = int(input("Enter the amount per litre: "))
# print(fuel(a, b))





#1.1 fuel price ======================
def fuel():
    print("\n")
    print("Amount of fuel")
    print("==============")

    litre_cost = float(input("Enter the cost per litre of fuel: "))
    money = int(input("Enter an amount in rands for purchasing fuel: "))

    litres_of_fuel = (money // litre_cost)

    conclusion =  f"\nYou can purchase roughly {litres_of_fuel} litres of fuel for R{money}, at R{litre_cost} per litre"
    print(conclusion)

    # redo()
# end of function ======================



#2 kpl and cost for a trip
# start of function ======================
def kpl(litres):
    print("\n")
    print("With", litres, "L of fuel")
    print("------------------")

    cpl = 24
    cost = litres * cpl
    # big car - 7kpl, 70L max capacity
    big = 7
    # small car - 14kpl, 40L max capacity
    small = 14

    km1 = litres * big
    if km1 > 490:
        exit()
    else:
        print(f"vehicle with ~70L tank:\n travel for {km1}km,\n for a total cost of R{cost},\n if it's R{cpl} per litre\n")


    km2 = litres * small
    if km2 > 560:
        exit()
    else:
        print(f"vehicle with ~40L tank:\n travel for {km2}km,\n for a total cost of R{cost},\n if it's R{cpl} per litre\n")

# end of function ======================
# maybe add a feature/ parameter where the user enters the price per litre of fuel
# instead of using a predefined on
# kpl(30)




#2.1 kpl and cost for a trip
# start of function ======================
def kpl():
    print("\n")
    print("Kilometers per litre")
    print("====================")

    litres = int(input("Enter an amount, in litres of fuel: "))

    # cpl - cost per litre
    # cpl = 24
    cpl = float(input("Enter the cost per litre of fuel: "))
    cost = litres * cpl

    print("\n")
    print("With", litres, "L of fuel")
    print("------------------")

    # big car - 7kpl, 70L max capacity
    big = 7
    # small car - 14kpl, 40L max capacity
    small = 14

    km1 = litres * big
    if km1 > 490:
        exit()
    else:
        print(f"vehicle with ~70L tank:\n travel for {km1}km,\n for a total cost of R{cost},\n if it's R{cpl} per litre\n")


    km2 = litres * small
    if km2 > 560:
        exit()
    else:
        print(f"vehicle with ~40L tank:\n travel for {km2}km,\n for a total cost of R{cost},\n if it's R{cpl} per litre\n")

# end of function ======================




#3 electricity Rands to KW
# start of function ======================
def randsToPower(money):
    # ppKW - price per KW of power
    ppKW1 = 2.5
    ppKW2 = 3.5

    # aop - amount of power
    aop = money / ppKW1
        
    if aop > 600:
        aop = 1500 / ppKW1
        aop600 = (money - 1500) / ppKW2 
        aop = aop + aop600

    print(f"\nFor R{money}, you can purchase {aop}KW of power")

# end of function ======================
# randsToPower(5000)




#3.1 electricity Rands to KW
# start of function ======================
def randsToPower():
    print("")
    print("Electricity calculator")
    print("======================")
    money = int(input("Enter a value in rands: "))
    # ppKW - price per KW of power
    ppKW1 = 2.5
    ppKW2 = 3.5

    # aop - amount of power
    aop = money / ppKW1
        
    if aop > 600:
        aop = 1500 / ppKW1
        aop600 = (money - 1500) / ppKW2 
        aop = aop + aop600

    print(f"\nFor R{money}, you can purchase {aop}KW of power")

# end of function ======================


# === the end ===============================================================
