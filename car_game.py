## Car game
## Help for getting info
## Option: Start, Stop, Quit.
## Can't understand for other words.

command = ""

while True:
    command = input("> ").lower
    if command == "start":
        print("Started...")
    elif command == "stop":
        print("Stopped.")
    elif command == "quit":
        break
    elif command == "help":
        print("info")
    else:
        print("errror77")



'''
给个容器存放输入的内容；
循环的输入内容：
    if start:
        print 
    elif stop:
        print
    elif quit:
        break
    elif help:
        print
    else:
        print
'''
