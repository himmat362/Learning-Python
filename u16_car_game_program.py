startcount=0
stopcount=0
while True:
    instruction=input("> ").lower()
    if instruction=="help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif instruction=="start":
        if startcount==1:
            print("Car already started!")
        else:
            print("Car started...Ready to go!")
            stopcount=0
            startcount=1
    elif instruction=="stop":
        if stopcount==1:
            print("Car already stopped!")
        else:
            print("Car stopped.")
            stopcount=1
            startcount=0
    elif instruction=="quit":
        break
    else:
        print("I don't understand that...")