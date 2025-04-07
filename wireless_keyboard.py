import time

# HID keycode for 'a' is 0x04
KEY_A = b'\x00\x00\x04\x00\x00\x00\x00\x00'  # 'a' key press
KEY_RELEASE = b'\x00\x00\x00\x00\x00\x00\x00\x00'  # key release

# Open the HID device file
with open("/dev/hidg0", "wb") as hid:
    while True:
        hid.write(KEY_A)       # Send 'a'
        hid.write(KEY_RELEASE) # Release key
        print("Sent: a")
        time.sleep(3)
