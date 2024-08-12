import threading
import random
import time

seznam_cisel = []
seznam_naplnen_event = threading.Event()

def napln_seznam():
    global seznam_cisel
    print("Naplnění seznamu náhodnými čísly...")
    time.sleep(1)
    seznam_cisel = [random.randint(1, 100) for _ in range(10)]
    print(f"Seznam naplněn: {seznam_cisel}")
    seznam_naplnen_event.set()

def vypocitej_soucet():
    seznam_naplnen_event.wait()
    soucet = sum(seznam_cisel)
    print(f"Součet v seznamu: {soucet}")



