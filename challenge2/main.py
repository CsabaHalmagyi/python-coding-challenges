# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#time in seconds
#distance in miles
def calculate_speed(time_in_seconds, distance):
    speed = distance / (time_in_seconds / 3600)
    print("If for a car it takes ", time_in_seconds, "seconds to travel ", distance, " mile(s), its speed is ", speed, "mph")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate_speed(52, 1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
