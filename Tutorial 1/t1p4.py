lightColour = input("What is the colour of the traffic lightColour? ")
distance = input("What is the distance between you and the intersection in metres? ")
speed = input("What is your current speed in metres per second? ")
seconds = int(distance)/int(speed)
if(lightColour == "green") or (lightColour == "yellow" and seconds<=5) or (lightColour == "red" and seconds <= 3):
    print("Go")
else:
    print("stop")
   