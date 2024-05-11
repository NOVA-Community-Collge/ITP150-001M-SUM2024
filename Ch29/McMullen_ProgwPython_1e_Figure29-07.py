# WET code
if hazard.moving == "right":
    if speed > 30:
        swerve("left")
    else:
        brake_lights = True
        alarm.sound()
        accelerate = False
        brake(hazard)

if hazard.moving == "left":
    if speed > 30:
        swerve("right")
    else:
        brake_lights = True
        alarm.sound()
        accelerate = False
        brake(hazard)

# DRY code

if hazard.moving == "right":
    if speed > 30:
        swerve("left")
    else:
        stop_car()

if hazard.moving == "left":
    if speed > 30:
        swerve("right")
    else:
        stop_car()
        
def stop_car():
    brake_lights = True
    alarm.sound()
    accelerate = False
    brake(hazard)