PIN_DOOR_1 = "0123"
PIN_DOOR_2 = "4321"


pin_door_1  =  input("Enter PINCODE 1: ") # "1234" str
lock_1_open =  pin_door_1 == PIN_DOOR_1   # bool

pin_door_2  =  input("Enter PINCODE 2: ")
lock_2_open =  pin_door_2 == PIN_DOOR_2


if lock_1_open and lock_2_open:
    print("Entered the FLAT!")
else:
    print("You did not entered the FLAT!")