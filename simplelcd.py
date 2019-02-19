import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD

lcd = CharLCD(cols=16, rows=2, pin_rs=26, pin_e=19, pins_data=[13, 6, 5, 11], numbering_mode = GPIO.BCM)

def print_msg(msg): 
    lcd.clear()
    lcd.write_string(msg)
