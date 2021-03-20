import time
from talk import talk

def remind(text):
    chaine = text
    chaine = chaine.replace("remind me to ", "")
    chaine = chaine.split()
    copy_chaine = text
    copy_chaine = copy_chaine.replace("remind me to ", "")
    copy_chaine = copy_chaine.split()
    long = len(chaine)

    remind = ""
    hour = 0
    minute = 0
    second = 0

    inverser = long - 1
    pos_in = 0
    while pos_in == 0:
        if chaine[inverser] == "in":
            pos_in = inverser
            a = long - pos_in
            for i in range(a):
                copy_chaine.pop(-1)
            remind = copy_chaine
            for i in range(pos_in+1):
                chaine.pop(0)
                print(chaine)
            

            i = len(chaine)
            i -= 1
            while i != 0:
                if chaine[i] == "minutes":
                    minute = chaine[i-1]
                if chaine[i] == "hours":
                    hour = chaine[i-1]
                if chaine[i] == "seconds":
                    second = chaine[i-1]
                if chaine[i] == "minute":
                    minute = chaine[i-1]
                if chaine[i] == "hour":
                    hour = chaine[i-1]
                if chaine[i] == "second":
                    second = chaine[i-1]
                i -= 1
        inverser -= 1

    minute = int(minute)
    minute *= 60
    hour = int(hour)
    hour *= 3600
    second = int(second)
    total_time = minute + second + hour
    print(total_time)
#!!!a changer car bloque le code
    time.sleep(total_time)

    final_remind = ', '.join(remind)
    final_remind = final_remind.replace(',', '')
    talk(f"remind, {final_remind}")
