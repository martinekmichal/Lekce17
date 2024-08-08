import threading

def vypocitat_soucet(values):
    soucet = sum(values)
    print(f"Součet prvků v seznamu je: {soucet}")

def vypocitat_prumer(values):
    if len(values) == 0:
        print("Seznam je prázdný, nelze vypočítat průměr.")
        return
    prumer = sum(values) / len(values)
    print(f"Průměrná hodnota v seznamu je: {prumer}")

values = list(map(int, input("Zadejte hodnoty oddělené mezerou: ").split()))

thread_soucet = threading.Thread(target=vypocitat_soucet, args=(values,))
thread_prumer = threading.Thread(target=vypocitat_prumer, args=(values,))

thread_soucet.start()
thread_prumer.start()

thread_soucet.join()
thread_prumer.join()
print("Výpočty dokončeny.")