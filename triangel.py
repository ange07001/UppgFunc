while True:
    try:
        n = int(input("Skriv ett positivt udda heltal: "))
        if n%2 == 1 and n > 0:
            break
        else:
            print("Inte ett positivt udda tal!")
    except ValueError:
        print("Inte ett heltal!")

def RightTriangle(n):
    print("\nDetta är en rätvinklig triangel:\n")
    for i in range(n):
        print(" "*i + "*"*(n-i))

def IsoscelesTriangle(n):
    print("\nDetta är Isoscelers triangel:\n")
    for i in range(0,n,2):
        print(" "*(n//2-i//2) + "*"*(i+1))

RightTriangle(n)
IsoscelesTriangle(n)