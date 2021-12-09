PIN_DOOR_1 = "0123"
PIN_DOOR_2 = "4321"


pin_door_1  =  input("Enter PINCODE 1: ") # "1234" str
lock_1_open =  pin_door_1 == PIN_DOOR_1   # bool

if lock_1_open:
    print("Entered the building")

    pin_door_2  =  input("Enter PINCODE 2: ")
    lock_2_open =  pin_door_2 == PIN_DOOR_2

    if lock_2_open:
        print("Entered the FLAT!")
    else:
        print("Incorrect PINCODE 2. You did not entered the FLAT!")
else:
    print("Incorrect PINCODE 1. You did not entered the building.")