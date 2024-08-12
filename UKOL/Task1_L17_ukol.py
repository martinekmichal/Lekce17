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

def vypocitej_prumer():
    seznam_naplnen_event.wait()
    prumer = sum(seznam_cisel) / len(seznam_cisel)
    print(f"Průměrná hodnota v seznamu je: {prumer}")

def main():
    vlakno_napln = threading.Thread(target=napln_seznam)
    vlakno_soucet = threading.Thread(target=vypocitej_soucet)
    vlakno_prumer = threading.Thread(target=vypocitej_prumer)
    vlakno_napln.start()
    time.sleep(1)
    vlakno_soucet.start()
    time.sleep(1)
    vlakno_prumer.start()

    vlakno_napln.join()
    vlakno_soucet.join()
    vlakno_prumer.join()
    print("Hotovo!")

main()