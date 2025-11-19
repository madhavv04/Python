i=0
def main():
    
    # global variable i is used outside the function
    global i
    print("Enter in function")
    if i < 5:
        i+=1
        main()
    print("Exit from function")
main()