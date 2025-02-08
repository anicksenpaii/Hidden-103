from dronekit import connect,VehicleMode,time,LocationGlobalRelative,math

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

vehicle.airspeed = 5
point1 = LocationGlobalRelative(-35.36174540, 149.16511679, 20) 
vehicle.simple_goto(point1)
while True:
    current_location = vehicle.location.global_relative_frame
    distance_to_waypoint = get_distance_metres(current_location,point1)

    if distance_to_waypoint <= 0.5:
        print("waypoint 1 reached")
        time.sleep(5)
        break
    
point2 = LocationGlobalRelative(-35.36172684, 149.16622058, 20)
vehicle.simple_goto(point2)
while True:
    current_location = vehicle.location.global_relative_frame
    distance_to_waypoint = get_distance_metres(current_location,point2)

    if distance_to_waypoint <= 0.5:
        print("waypoint 2 reached")
        time.sleep(2)
        break

point3 = LocationGlobalRelative(-35.36261771, 149.16620920, 20)
vehicle.simple_goto(point3)
while True:
    current_location = vehicle.location.global_relative_frame
    distance_to_waypoint = get_distance_metres(current_location,point3)

    if distance_to_waypoint <= 0.5:
        print("waypoint 3 reached")
        time.sleep(2)
        break

point4 = LocationGlobalRelative(-35.36262699, 149.16510541, 20)
vehicle.simple_goto(point4)
while True:
    current_location = vehicle.location.global_relative_frame
    distance_to_waypoint = get_distance_metres(current_location,point3)

    if distance_to_waypoint <= 0.5:
        print("waypoint 4 reached")
        time.sleep(2)
        break

vehicle.simple_goto(point1)
while True:
    distance_to_waypoint = get_distance_metres(current_location,point1)

    if distance_to_waypoint <= 0.5:
        print("square completed successfully")
        
        vehicle.mode = VehicleMode("RTL")
