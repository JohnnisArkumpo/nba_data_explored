import avr

# functionallity user side

def main():
    print(f"Welcome to your NBA data center!\n\nTo use a data center function, enter the corresponding number code. Type 0 to exit  ")
    print(f"1 - Find statistical averages of any decade")
    print(f"2 - Compare the statistical averages of any two decades")
    print(f"3 - Find the best player of any decade by stats")
    oper1 = int(input())

    if oper1 == 0:
        print(f"Thank you for using the NBA data center!")
    elif oper1 == 1:
        print(f"What decade would you like to see the averages for?\n\nThis dataset starts in the 50s, type 50 for the 50s, 60 for the 60s, etc. until the 2000s, then type 00 for the 2000s, 10 for the 2010s, etc.  ")
        udec = int(input())
        avr.average(udec)
    elif oper1 == 2:
        print(f"")

main()
