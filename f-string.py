import math as mt

coords =[]

while True:
    try:
        coordString = input("Enter two coordinates separated by spaces (x1 y1 x2 y2): ")
        coords = coordString.split()
        coords = [float(i) for i in coords]
        if len(coords) == 4:
            break
        else:
            print("\033[91m"+"You did not enter 4 values!"+"\033[0m")
    except ValueError:
        print("\033[91m"+"Enterd values are not numbers!"+"\033[0m")


def CoordDist(x1,y1,x2,y2):
    return round(mt.sqrt(mt.pow(x2-x1,2) + mt.pow(y2-y1,2)),2)

print(f"The distance between the points ({coords[0]}, {coords[1]}) and ({coords[2]}, {coords[3]}) is \033[92m{CoordDist(coords[0],coords[1],coords[2],coords[3])}\033[0m")