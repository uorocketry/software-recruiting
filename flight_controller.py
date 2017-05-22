from dummy_rocket import DummyRocket

current_altitude = 0
target_altitude = 3048

rocket = DummyRocket()
rocket.set_thrust(1)

while rocket.flying():
    rocket.update()
    #TODO implement your algorithm here
        # track altitude given acceleration
        # adjust thrust accordingly


print "total flight time: ", rocket.flight_time /1000.0, " seconds"
# DO NOT USE rocket.altitude to track altitude

print "You missed the target by: ", (rocket.altitude - target_altitude), " meters"
