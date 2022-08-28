from time import time
from pygame import mixer
from datetime import datetime

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(loops=-1)
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
print("Welcome to Healthy Application here we go....")
def log_now(msg):
    with open("Ex9/mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")             

if __name__=='__main__':
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    init_nap=time()
    init_eat=time()
    watersecs=5
    exsecs=10
    eyessecs=15
    napsecs=20
    eatsecs=25

    while True:

        if time() -init_eat>eatsecs:
            print("Eating time.Enter 'edone' to stop the alarm.")
            musiconloop('Ex9/eat.mp3','edone')
            init_eat=time()
            log_now("Had a food at: ")

        if time() -init_water>watersecs:
            print("Water drinking time.Enter 'drank' to stop the alarm.")
            musiconloop('Ex9/water.mp3','drank')
            init_water=time()
            log_now("Drank water at: ")

        if time() -init_eyes>eyessecs:
            print("Eyes exercise time.Enter 'deyes' to stop the alarm.")
            musiconloop('Ex9/eyes.mp3','deyes')
            init_eyes=time()
            log_now("Eyes relaxed at: ")

        if time() -init_exercise>exsecs:
            print("Physical activity time.Enter 'dphy' to stop the alarm.")
            musiconloop('Ex9/physical.mp3','dphy')
            init_exercise=time()
            log_now("Physical activity done at: ")

        if time() -init_nap>napsecs:
            print("Power nap time.Enter 'ndone' to stop the alarm.")
            musiconloop('Ex9/nap.mp3','ndone')
            init_exercise=time()
            log_now("Powernap finished at: ")   
            break 

