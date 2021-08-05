from config import Config
from time import time, sleep

def test_command():
    i = 0
    result = Config.TEST_COMMAND
    if result == 0:
        print("0")
    else:
        while i < Config.TEST_THRESHOLD:
            i += 1
            result = Config.TEST_COMMAND
            if result == 0:
                print("0")
                break
            sleep(Config.TEST_INTERVAL)
        else:
            print("ERROR : 1")

test_command()