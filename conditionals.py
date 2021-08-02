command=""
started =False
stopped=False

while True:
    command= input("<").lower()
    if command == "start":
        if started :
          print("Car is already started")
        else:
            started=True
            print("start the car")
    elif command =="stop":
        if stopped:
            print("The car is already stopped")
        else:
            stopped =True
            print("Stop the car")
    elif command== "help":
        print("Start to start the car")
        print("Stop to stop the car")
        print("Quit to exit")
    elif command  == "quit":
        break
    else:
        print("I donot know what you did")






