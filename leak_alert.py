#!/usr/bin/python3

from time import sleep
import RPi.GPIO as GPIO
import spidev


spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 250000

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

def poll_sensor(channel):
    """Poll MCP3002 ADC
    Args:
        channel (int): ADC channel 0 or 1
        Returns:
            int: 10 bit value relating voltage 0 to 1023
    """
    assert 0 <= channel <= 1, 'ADC channel must be 0 or 1.'

    # First bit of cbyte is single=1 or diff=0.
    # Second bit is channel 0 or 1
    if channel:
        cbyte = 0b11000000
    else:
        cbyte = 0b10000000

    # Send (Start bit=1, cbyte=sgl/diff & odd/sign & MSBF = 0)
    r = spi.xfer2([1, cbyte, 0])

    # 10 bit value from returned bytes (bits 13-22):
    return ((r[1] & 31) << 6) + (r[2] >> 2)

try:
    while True:
        channel = 0
        channeldata = poll_sensor(channel)

        voltage = round(((channeldata * 3300) /  1024), 0)
        print('Voltage (mV): {}'.format(voltage))
        print('Data     : {}\n'.format(channeldata))

        if voltage < 50:
            # Green
            GPIO.output(14, GPIO.LOW)
            GPIO.output(15, GPIO.HIGH)
            GPIO.output(18, GPIO.LOW)
        elif voltage < 1000:
            # Yellow
            GPIO.output(14, GPIO.HIGH)
            GPIO.output(15, GPIO.HIGH)
            GPIO.output(18, GPIO.LOW)
        else:
            # Red
            GPIO.output(14, GPIO.HIGH)
            GPIO.output(15, GPIO.LOW)
            GPIO.output(18, GPIO.LOW)
            import voice
            sleep(10)
            import sms

        sleep(2)
finally:            # Run on exit
    spi.close()     # Clean up
    GPIO.cleanup()
    print ("\n All cleaned up.")
