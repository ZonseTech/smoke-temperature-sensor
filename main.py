import sys
import time

from mq import *
import board
import adafruit_dht


"""
Smoke sensor
"""
try:
    print("Press CTRL+C to abort.")
    # VE    - DHT version, e.g. 11 or 22
    # PIN   - GPIO Pin the board is connected to, e.g. D4 = GPIO Pin 4
    #                           VE       PIN
    dhtDevice = adafruit_dht.DHT22(board.D4)
    mq = MQ()
    sensor_threshold = 30
    temperature_threshold = 27

    while True:
        # to handle error
        # will use try - catch technic
        try:
            temperature_c = dhtDevice.temperature
            perc = mq.MQPercentage()
            smokePerc = perc["SMOKE"]

            # handling smoke
            if smokePerc > sensor_threshold:
                """
                    Sound the buzzer && start the fun
                    switch on red LED
                """
            else:
                """
                    stop sounding the buzzer && stop the fun
                    switch on green LED
                """

            # handling temperature
            if temperature_c > temperature_threshold:
                """
                    Sound the buzzer && start the fun
                    switch on red LED
                """
            else:
                """
                    stop sounding the buzzer && stop the fun
                    switch on green LED
                """

        except RuntimeError as error:
            # Sometimes you get errors, so just print them
            print(error.args[0])
            time.sleep(2.0)
            continue

        except Exception as error:
            dhtDevice.exit()
            raise error

        time.sleep(2.1)

except:
    print("\nAbort by user")