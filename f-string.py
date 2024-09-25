import math as mt

coords =[]
Input = True

while Input:
    coordString = input("Enter two coordinates separated by spaces (x.x y.y x.x y.y): ")
    coords = coordString.split()
    print(coords)
    if len(coords) == 4:
        Input = False
    else:
        print("Not 4 numbers")
    

