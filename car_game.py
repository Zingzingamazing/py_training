## Car game
## Help for getting info
## Option: Start, Stop, Quit.
## Can't understand for other words.

input = input("")

if input.upper == "HELP":
    print("info")
elif input.upper == "START":
    print("Car started... Ready to go!")
elif input.upper == "STOP":
    print("Car stopped.")
elif input.upper == "QUIT":
    quit
else:
    print("I don't understand that...")
