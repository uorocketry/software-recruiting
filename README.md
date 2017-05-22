## uOttawa Team Rocket Software Challenge

## About
This challenge is for undergradute students who want to join the uOttawa
Rocket Team as a software developer on the flight control system.  The Team
competes in the annual
[IREC competition](http://www.soundingrocket.org/2017-irec.html) in New Mexico
where students design rockets to precisely carre an 8 lb payload to a specific
altitude

Our rocket has a very unique capability we have the ability to control its thrust
in real time.  This combined with our sensor stack and onboard flight computer leaves
one missing piece...we need a real time control system to fly this baby to victory

## The Challenge
You must implement the following loop in `flight_controller.py`
```
while (current_altitude < target_altitude):
    #TODO implement your algorithm here
        # track altitude given acceleration
        # adjust thrust accordingly

    rocket.update()
```
which is responsible for controlling the thrust in order to reach a desired altitude
and runs every millisecond

#### Acceleration

Unfortunately, our rocket does not have an altimeter or an airspeed indicator, only
an accelerometer is present.  You must first devise a way to track the velocity and
altitude of the rocket only from the acceleration.  The current accelerometer value
can be fetched with `get_acceleration` but watchout for noise in the sensor readings.

Also the dummy rocket is subject to drag forces and other physical phenomena.
please consider this in your algorithm

#### Thrust

You should use this information and some math to set the thrust_level using
`set_thrust(percentage)`, where 1.0 is the `rocket.max_thrust`. You can continue to
set the thrust until you run out of fuel.  You can check the amount of fuel using
`rocket.get_fuel_mass`.  Once the fuel is depleeted setting the thrust level will
provide you with 0 N of thrust.

#### Mass

If goes without saying the mass of the rocket decreases depending on the amount of
fuel burnt. you can get the current mass using `rocket.get_mass`
