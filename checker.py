import time
from playsound import playsound
from multiprocessing import Process

# Checks the line number of the latest line in the file that starts with "---"
# Returns none if there is none
def note_read(file):
    n = None
    print("program start")
    f = open(file, "r")
    for x, line in enumerate(f):
        if (line[:3] == "---"):
            n = x
    return n

def call_alarm():
    while (True):
        playsound("alarm.mp3")
    

def main():
    # establish lambda in terms of minutes
    λ = 3/60

    # establish file name
    file = "note.txt"

    # establish starting case of the file
    n = note_read(file)
    if (n == None):
        raise Exception("This file format is invalid.")
    print(f"latest line is at line {n}.")

    # forever while the script is running, check every λ minutes if at least one section has been added
    while (True):
        temp = note_read(file)
        # if section is not added, trigger alarm sound; else record new line of latest divider
        # alarm is a seperate process; such a process is terminated on input
        if (temp == n):
            alarm = Process(target = call_alarm)
            alarm.start()
            input("Type anything to terminate alarm: ")
            alarm.terminate()
        else:
            n = temp
            print("Good job!")
            print(f"latest line is at line {n} - this is a new line.")
        # wait λ minutes
        time.sleep(λ * 60)

if __name__ == "__main__":
    main()
