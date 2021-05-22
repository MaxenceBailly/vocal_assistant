import time, multiprocessing
from talk import talk

def remind(text):
    chaine = text
    chaine = chaine.replace("rappelle-moi de ", "")
    chaine = chaine.split()
    copy_chaine = text
    copy_chaine = copy_chaine.replace("rappelle-moi de ", "")
    copy_chaine = copy_chaine.split()
    long = len(chaine)

    remind = ""
    hour = 0
    minute = 0
    second = 0

    inverser = long - 1
    pos_in = 0
    while pos_in == 0:
        if chaine[inverser] == "dans":
            pos_in = inverser
            a = long - pos_in
            for i in range(a):
                copy_chaine.pop(-1)
            remind = copy_chaine
            for i in range(pos_in+1):
                chaine.pop(0)
            

            i = len(chaine)
            i -= 1
            while i != 0:
                if chaine[i] == "minutes":
                    minute = chaine[i-1]
                if chaine[i] == "heures":
                    hour = chaine[i-1]
                if chaine[i] == "secondes":
                    second = chaine[i-1]
                if chaine[i] == "minute":
                    minute = chaine[i-1]
                if chaine[i] == "heure":
                    hour = chaine[i-1]
                if chaine[i] == "seconde":
                    second = chaine[i-1]
                i -= 1
        inverser -= 1

    minute = int(minute)
    minute *= 60
    hour = int(hour)
    hour *= 3600
    second = int(second)
    total_time = minute + second + hour

    final_remind = ', '.join(remind)
    final_remind = final_remind.replace(',', '')
    remind_process = multiprocessing.Process(target=wait, args=[total_time, final_remind])
    remind_process.start()
    remind_process.join()

def wait(time_to_wait, remind):
    time.sleep(time_to_wait )
    talk(f"rappelle, {remind}")

if __name__ == "__main__":
    remind("rappelle-moi de démarer le programme dans 10 secondes")