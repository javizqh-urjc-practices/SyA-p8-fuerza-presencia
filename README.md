# P8-Fuerza
## Hardware problems
The problem we encountered was that the strenght sensor didn't work as expected, instead of using a 1M ohm resistor, we had to use a 330 ohm resistor because the strength of the signal wasn't strong enough to be considered as a signal

## Observations
The code is almost the same as the previous excercise for the first two parts because the behaviours are almost the same.

For the last excercise we changed the code a little bit, so instead of the calling the callbacks when the signal is rising and falling, now it only calls the callbacks when the signal is rising, and then it sets the loops counters to the maximum value.
```python
lightTTL = ledTTL
detectTTL = presenciaTTL # Reset detect timer
```

Then in order to decrease that loops counters in order to create a timer, we used a while true loop in the main function, because trying to loop in the callbacks wasn't working properly.
```python
while True:
  if (detectTTL > 0): detectTTL -= 1
  if (lightTTL > 0): lightTTL -= 1
  if (lightTTL == 0):  GPIO.output(ledPin, GPIO.LOW) # Turn off light
  # Uncomment for debugging
  # print(f'detectTTL = {detectTTL} seconds')
  # print(f'lightTTL = {lightTTL} seconds')
  sleep(1)
```