from machine import Pin, PWM, ADC
"""
buzzer = PWM(Pin(18))
btn = Pin(20, Pin.IN, Pin.PULL_DOWN)
adc = ADC(Pin(27))

buzzer.freq(500)

while True:
    if not btn.value():
        buzzer.duty_u16(adc.read_u16())
        print(adc.read_u16())
    else:
        buzzer.duty_u16(0)


#RGB

from machine import Pin
import neopixel
import time
import random

rgb = neopixel.NeoPixel(Pin(28), 1)

BRIGHTNESS = 0.5

def set(color):
    r, g, b = color
    r = int(r * BRIGHTNESS)
    g = int(g * BRIGHTNESS)
    b = int(b * BRIGHTNESS)
    return(r, g, b)



while True:
    a = random.randrange(0, 255)
    b = random.randrange(0, 255)
    c = random.randrange(0, 255)
    
    rgb.fill(set((a, b, c)))
    rgb.write()
    time.sleep(1)
    
    rgb.fill(set((b, a, c)))
    rgb.write()
    time.sleep(1)
    
    rgb.fill(set((c, b, a)))
    rgb.write()
    time.sleep(1)


#vice frekvenci na buzzeru

from machine import Pin,PWM


buzzer = PWM(Pin(18))

btn = Pin(20, Pin.IN)
btn1 = Pin(21, Pin.IN)
btn2 = Pin(22, Pin.IN)


while True:
    if not btn.value():
        buzzer.freq(2008)
        buzzer.duty_u16(30000)
    else:   
        buzzer.duty_u16(0)
        
    if not btn1.value():
        buzzer.freq(280)
        buzzer.duty_u16(1000)
    else:   
        buzzer.duty_u16(0)

    if not btn2.value():
        buzzer.freq(28)
        buzzer.duty_u16(1000)
    else:   
        buzzer.duty_u16(0)

####

led = Pin(10, Pin.OUT)
led1 = Pin(11, Pin.OUT)
led2 = Pin(12, Pin.OUT)
btn = (20, Pin.IN, Pin.PULL_DOWN)


while True:
    if btn.value():
        led.off()
        led1.off()
        led2.off()
        
    else:
        led2.on()
        led1.on()
        led.on()
####      

led = Pin(5,Pin.OUT)
btn = Pin(20, Pin.IN)
while True:
    if btn.value():
        led.on()
        
    else:
        led.off()
"""