class Vehicle():

    def __init__(stuf,max_speed,milage):
        stuf.max_speed = max_speed
        stuf.milage = milage

    def display(stuf):
        print(stuf.max_speed)
        print(stuf.milage)

asf = Vehicle(70,20)
asf.display()