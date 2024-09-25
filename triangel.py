while True:
    try:
        n = int(input("Skriv ett positivt udda heltal: "))
        if n%2 and n > 0:
            break
        else:
            print("\033[91m"+"Inte ett positivt udda tal!"+"\033[0m")
    except ValueError:
        print("\033[91m"+"Inte ett heltal!"+"\033[0m")

def RightTriangle(n):
    print("\nDetta är en rätvinklig triangel:\n")
    for i in range(n):
        print(" "*i + "*"*(n-i))

def IsoscelesTriangle(n):
    print("\nDetta är en likbent triangel:\n")
    for i in range(0,n,2):
        print(" "*(n//2-i//2) + "*"*(i+1))

RightTriangle(n)
IsoscelesTriangle(n)