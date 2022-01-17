def menuDisplay():
    print('<><><><><><><><><><><><><><><><>')
    print('$$ bending and max stress in a rectangular beam $$')
    print('<><><><><><><><><><><><><><><><>')
    print('(1) Calculate Area')
    print('(2) Calculate Moment of Inertia')
    print('(3) Calculate Max Sheer Stress')
    print('(4) Calculate Max Bending Strength')
    CHOICE = int(input("Enter choice: "))
    menuSelection(CHOICE)


def menuSelection(CHOICE):
    if CHOICE == 1:
        Area()
    elif CHOICE == 2:
        momentofInertia()
    elif CHOICE == 3:
        maxSheerStress()
    elif CHOICE == 4:
        maxBendingStress()
    elif CHOICE == 6:
        exit()

       # calculating the area
def Area():
    width = int(input("what is the width?: "))
    thickness = int(input("what is the thickness?: "))
    print(width * thickness)

        # calculating the moment of inertia
def momentofInertia():
    width = int(input("what is the width?: "))
    thickness = int(input("what is the thickness?: "))
    print((1 / 12) * (width * thickness ** 3))

        # calculating the max sheerstress
def maxSheerStress():
    width = int(input("what is the width?: "))
    thickness = int(input("what is the thickness?: "))
    sheerstress = int(input("what is the sheer stress?: "))
    print((3 / 2) * (sheerstress / (width * thickness)))

        # calculating the max bending stress
def maxBendingStress():
    bendingMoment = int(input("what is the bending moment?: "))
    thickness = int(input("what is the thickness?: "))
    width = int(input("what is the width?: "))
    print(-bendingMoment * (thickness / 2) / (1 / 12) * (width * thickness ** 3))

print(menuDisplay())
