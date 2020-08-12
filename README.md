# Micropython Module for E32CB

*v 1.0.0*

## usage

```python
from e32cb import E32CB


#uart interface
uart = E32CB.uart


#i2c interface
i2c = E32CB.i2c


#buildin LED
E32CB.led(1) #LED on
E32CB.led(0) #LED off


#fan connector
E32CB.fan(512) #pwm value, 0-1023


#mosfets (q1 -q8)
E32CB.q1.on() #turn mosfet on
E32CB.q1.off() #turn mosfet off
E32CB.q1.pwm(512) #pwm value, 0-1023, note: pwm is not available on q8
```
