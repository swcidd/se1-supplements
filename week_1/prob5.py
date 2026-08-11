driver_speed = 62
speed_limit = 40
is_school_zone = False

speed_over = driver_speed - speed_limit
fine = 0

if speed_over <= 10:
    fine = 50
elif speed_over <= 21:
    fine = 100
else:
    fine = 250
    print("License Suspension Warning")

if is_school_zone == True:
    fine = fine * 2

if fine >= 0:
    print(f"Your final ticket is:${fine}")
