from dronekit import connect,VehicleMode,time,LocationGlobalRelative,math,mavutil

vehicle = connect('127.0.0.1:14550',wait_ready=True)

vehicle.mode = VehicleMode("GUIDED")

def get_distance_metres(location1, location2): #location 1 is current and location 2 is waypoint
    dlat = location2.lat - location1.lat
    dlong = location2.lon - location1.lon
    return math.sqrt((dlat * dlat) + (dlong * dlong)) * 1.113195e5

vehicle.armed = True
while not vehicle.armed:
    print("Waiting for vehicle to arm...")
    time.sleep(1)
print("Vehicle is armed!")

Target_altitude = 15

vehicle.simple_takeoff(Target_altitude)
while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= Target_altitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)


def send_ned_velocity(velocity_x, velocity_y, velocity_z, duration):
    """
    Move vehicle in direction based on specified velocity vectors.
    """
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
        0b0000111111000111, # type_mask (only speeds enabled)
        0, 0, 0, # x, y, z positions (not used)
        velocity_x, velocity_y, velocity_z, # x, y, z velocity in m/s
        0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 100)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)


    # send command to vehicle on 1 Hz cycle
    for x in range(0,duration):
        vehicle.send_mavlink(msg)
        time.sleep(1)

# vehicle.airspeed = send_ned_velocity(10,0,0,10)
# time(10)
send_ned_velocity(0,10,0,10)
time.sleep(5)
send_ned_velocity(10,0,0,10)
time.sleep(5)
send_ned_velocity(0,-10,0,10)
time.sleep(5)
send_ned_velocity(-10,0,0,10)
time.sleep(5)

vehicle.mode = VehicleMode('RTL')







     


