import math

def binlog(x):
    return math.log(x) / math.log(2)

"""
aperture is the size of the camera lens opening basically, 
f/2.8 eq to 2.8, f/16 eq to 16 etc

shutter is the duration of time the camera shutter is open,
60 eq to 1/60 sec, 1000 eq to 1/1000 sec etc

so an EV for f/2.8 at 1/1000 shutter would be, 
EV(2.8, 1000) """
def EV_camera(aperture, shutter):
    return binlog(\
            aperture**2 / shutter**-1 \
            )

def EV_light(lux, iso):
    # we assume an incident light coefficient of C=330
    C = 330
    return binlog(\
            lux * iso / C \
            )

def main():
    print("exposure value @ f/8, shutter = 60")
    print("EV_camera(2.8, 60) =", EV_camera(2.8, 60) )

    print("\nexposure value @ f/2, shutter = 48")
    print("EV_camera(2, 48) =", EV(2, 48) )


if __name__ == "__main__":
    main()

