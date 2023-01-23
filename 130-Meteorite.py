'''Rocket goes zooms'''


def rocket(mass, spilt, safe):
    '''Let's go'''
    rocket_first = True
    times = 0
    rocket_count = 0
    while mass >= safe:
        mass /= spilt
        if rocket_first:
            rocket_count += 1
            rocket_first = False
        else:
            rocket_count += spilt ** times
        times += 1
    print(rocket_count)


rocket(float(input()), int(input()), float(input()))
