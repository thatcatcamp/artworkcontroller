import subprocess
from os.path import join
from time import sleep
import hid
import requests

HOOMAN=79
RED=47
BLUE=31


def play(file: str):
    """
    play a random sound from this group
    :param file:
    :return:
    """
    result = requests.post("http://localhost:8888/play", json={'file': file})
    print(result)


for device in hid.enumerate():
    print(f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}")


gamepad = hid.device()
gamepad.open(0x0079, 0x0006)
gamepad.set_nonblocking(True)
while True:
    report = gamepad.read(64)
    # offset 5 is button scanner

    if report:
        button_status = report[5]
        if 15 == button_status:
            sleep(1)
            continue
        print(report)
        print(button_status)
        if button_status == HOOMAN:
            play("laugh.wav")
        if button_status == RED:
            play("grunt1.wav")
        if button_status == BLUE:
            play("grunt2.wav")
    sleep(1)
