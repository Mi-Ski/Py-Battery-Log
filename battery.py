import time

def statusFunct():
    # BAT0 could be BAT1 on some machines
    currStatus = open("/sys/class/power_supply/BAT0/status", "r").readline().strip()
    return currStatus

def powerFunct():
    currBattery = open("/sys/class/power_supply/BAT0/capacity", "r").readline().strip()
    return currBattery


while (True):
    power = powerFunct()
    currStatus = statusFunct()

    print('Battery: ' + power + '%...')
    time.sleep(0.5)
    print('Battery: ' + power + '% ...')
    time.sleep(0.5)
    print('Battery: ' + power + '%  ...')
    time.sleep(0.5)
    print('Battery: ' + power + '%   ... ' + currStatus)
    time.sleep(0.5)
    print('Battery: ' + power + '%  ...')
    time.sleep(0.5)
    print('Battery: ' + power + '% ...')
    time.sleep(0.5)
    print('Battery: ' + power + '%...')
    time.sleep(0.5)