command = ""
started = False
# we can add while True for the same logic
# while True (Method 2)
while command != 'quit':
    command = input(">").lower()
    if command == "start":
        if started:
          print("Car started..")
        else:
         started = True
         print("Hey!It's already started")
    elif command == "stop":
         if not started:
             print("Car already stopped")
         else:
          started = False
          print("car stopped")
    elif command == "help":
          print("""
start - to start the caer
stop - to stop the car
quit - to quit the car
    """)
    elif command == "quit":
        break
    else:
        print("sorry i dont understand")