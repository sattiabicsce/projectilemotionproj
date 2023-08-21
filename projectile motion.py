import math


def calculate_projectile_motion(speed, height, angle):

    angle = math.radians(angle)

    # initial vertical and horizontal velocities
    v0x = speed * math.cos(angle)
    v0y = speed * math.sin(angle)

    # time of flight
    t_flight = math.sqrt(v0y ** 2 + (9.8 * height)) / 9.8

    # max height
    max_height = height + (v0y ** 2) / (2 * 9.8)

    # horizontal distance
    horizontal_distance = v0x * t_flight

    # final vertical velocity
    v_final = math.sqrt((v0y ** 2) + (2 * 9.8 * height))

    # Print the results
    print("Projectile Motion Results:")
    print(f"Time of Flight: {t_flight} seconds")
    print(f"Maximum Height: {max_height} m")
    print(f"Horizontal Distance: {horizontal_distance} m")
    print(f"Final Vertical Velocity: {v_final} m/s")


# Get user input
speed = float(input("Enter the launch speed (in m/s): "))
height = float(input("Enter the launch height (in meters): "))
angle = float(input("Enter the launch angle (in degrees): "))

calculate_projectile_motion(speed, height, angle)
