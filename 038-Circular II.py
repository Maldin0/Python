"""Hi"""
def main():
    """Hello"""
    numx = float(input())
    numy = float(input())
    numr = float(input())
    numxn = float(input())
    numyn = float(input())
    numrn = float(input())
    if ((numx-numxn)**2+(numy-numyn)**2)**(1/2) < numr+numrn:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)
main()
