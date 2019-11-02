import sys

time1 = sys.stdin.readline().strip()
time1 = [int(time) for time in time1.split(":")]

time2 = sys.stdin.readline().strip()
time2 = [int(time) for time in time2.split(":")]

def transformToSeconds(hour, minute, second):
    return hour * 3600 + minute * 60 + second

seconds1 = transformToSeconds(time1[0], time1[1], time1[2])
seconds2 = transformToSeconds(time2[0], time2[1], time2[2])

seconds2 -= seconds1

seconds = str(int(seconds2%60))
minutes = str(int((seconds2%3600)/60))
hours = str(int((seconds2/3600) % 24))

if len(seconds) == 1:
    seconds = "0" + seconds

if len(minutes) == 1:
    minutes = "0" + minutes

if len(hours) == 1:
    hours = "0" + hours

if (hours + ":" + minutes + ":" + seconds) == "00:00:00":
    print("24:00:00")
else:
    print(hours + ":" + minutes + ":" + seconds)