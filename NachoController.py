import pygame, time

pygame.init()
pygame.joystick.init()

js = pygame.joystick.Joystick(0)
js.init

print("Controller Found:", pygame.joystick.get_count())

for i in range(pygame.joystick.get_count()):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    print(f"Controller {i}: {joystick.get_name()}")


while True:
    pygame.event.pump() #update controller status

    left_x = js.get_axis(0)
    left_y = js.get_axis(1)

    right_x = js.get_axis(2)
    right_y = js.get_axis(3)

    left_trigger = js.get_axis(4)
    right_trigger = js.get_axis(5)

    dpad_x, dpad_y = js.get_hat(0)

    a_button = js.get_button(0)
    b_button = js.get_button(1)
    c_button = js.get_button(2)
    d_button = js.get_button(3)

    print(a_button)
    if dpad_y == 1:
        print("up")
    elif dpad_y == -1:
        print("down")
    elif dpad_x == 1:
        print("right")
    elif dpad_x == -1:
        print("left")

    #print(str(left_trigger) + " " + str(right_trigger))

    pygame.event.pump()
    time.sleep(0.1)
