from machine import Pin, Signal, PWM, I2C, UART


class Mosfet:
	def __init__(self, pin, pwm_base_freq, pwm_max):
		self.__pwm = PWM(pin, freq=pwm_base_freq, duty=pwm_max)

	def pwm(self, pwm):
		self.__pwm.duty(E32CB.invert_pwm(pwm))

	def on(self):
		self.__pwm.duty(E32CB.pwm_min)

	def off(self):
		self.__pwm.duty(E32CB.pwm_max)



class E32CB:
		
	pwm_fan_freq  = 25000
	pwm_base_freq = 1000
	pwm_min = 0
	pwm_max = 1023


	i2c  = I2C(scl=Pin(22), sda=Pin(21))
	uart = UART(2, 9600)

	q1 = Mosfet(Pin(33), pwm_base_freq, pwm_max)
	q2 = Mosfet(Pin(25), pwm_base_freq, pwm_max)
	q3 = Mosfet(Pin(27), pwm_base_freq, pwm_max)
	q4 = Mosfet(Pin(14), pwm_base_freq, pwm_max)
	q5 = Mosfet(Pin(13), pwm_base_freq, pwm_max)
	q6 = Mosfet(Pin(4 ), pwm_base_freq, pwm_max)
	q7 = Mosfet(Pin(18), pwm_base_freq, pwm_max)

	q8 = Signal(Pin(19, Pin.OUT), invert=True)


	@classmethod
	def invert_pwm(cls, pwm):
		return cls.pwm_min+(cls.pwm_max-pwm)

	@staticmethod
	def led(value):
		Pin(32, Pin.OUT).value(value)

	@staticmethod
	def fan(value):
		PWM(Pin(23), freq=pwm_fan_freq, duty=value);
