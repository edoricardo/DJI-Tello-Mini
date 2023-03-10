from djitellopy import Tello
from time import sleep

tello = Tello()
tello.connect()
print(tello.get_battery())

print("takeoff? y/n")
takeoffinput = "input"
if takeoffinput == 'y':
    tello.takeoff()
    sleep(5)
    '''
    Send RC control via four channels
    send_rc_control(self, left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity)
    '''
    tello.send_rc_control(0,0,0,0)
    sleep(2)
    tello.send_rc_control(0,50,0,0)
    sleep(2)
    tello.send_rc_control(0,0,0,0)
    sleep(2)

    print("land? y/n")
    landinput = "input"
    if landinput == 'y':
        tello.land()
    else:
        tello.rotate_clockwise(360)
        tello.land()
else:
    quit()
