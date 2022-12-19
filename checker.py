import time
from playsound import playsound
from multiprocessing import Process

# Checks the line number of the latest line in the file that starts with a divider
# Returns none if there is none
def note_read(file, divider):
    n = None
    f = open(file, "r")
    for x, line in enumerate(f):
        if (line[:3] == divider):
            n = x
    return n

# play alarm sound
def call_alarm(sound):
    while (True):
        playsound(sound)
    

def main():
    # ESTABLISH PARAMETERS
    #---------------------------------------------------------------------------------------------------------------------

    # establish lambda in terms of minutes
    λ = 3/60

    # establish divider
    divider = "---"

    # establish file name
    file_name = "note.txt"

    # establish alarm
    alarm_sound = "alarm.mp3"

    #---------------------------------------------------------------------------------------------------------------------
    
    # check if file is in valid format and establish starting n value
    n = note_read(file_name, divider)
    if (n == None):
        raise Exception("This file format is invalid.")
    success_count = 0
    round = 1
    print("Welcome - you have started a new session.")

    # forever while the script is running, check every λ minutes if at least one section has been added
    while (True):
        # wait λ minutes
        print(f"This is round {round}")
        time.sleep(λ * 60)
        temp = note_read(file_name, divider)
        if (temp == n):
            # alarm is a seperate process; this is to make it stop on input
            # put ' inside argument parameter or it will cause tuple detection errors in compiler
            alarm = Process(target = call_alarm, args=(alarm_sound,))
            alarm.start()
            print("Uh-oh! You failed to keep up to your standards. Alarm will sound.")
            input("Type anything to terminate alarm: ")
            alarm.terminate()
        else:
            n = temp
            success_count += 1
            print(f"Good job! Keep it up. You've succeeded {success_count} times this session.")
        round += 1

if __name__ == "__main__":
    main()
