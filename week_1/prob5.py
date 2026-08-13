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

#### Prob 5
# - Scenario: A traffic camera calculates fines for speeding. The fine increases the faster the driver goes, and fines are doubled in school zones.
#- Inputs: driver_speed (number), speed_limit (number), is_school_zone (boolean).
#- Task: For this problem, you do not need to ask for the inputs using input(), instead directly assign values to those variables in your program. 
 # - If speed < speed_limit: No fine.
  #- 1–10 mph over: $50 fine.
  #- 11–20 mph over: $100 fine.
  #- 21+ mph over: $250 fine and a license suspension warning.
  #- Rule: If is_school_zone is true, double the calculated fine before printing the final ticket amount.