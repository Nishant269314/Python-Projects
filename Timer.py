import time

my_time = int(input("Enter time in sec:"))

for x in range(my_time, 0, -1):
    sec = x % 60
    mine = int(x / 60) % 60
    hour = int(x / 3600)

    print(f"{hour:02}:{mine:02}:{sec:02}")

    time.sleep(1)