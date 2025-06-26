if __name__== '__main__':
    #outer of try is what?
    try:
        name = eval(input("Enter your name: "))
        if name >3:
            print("Hello")
    except:
        print("An error was detected in your code")