import threading

def find_max(values):
    max_value = max(values)
    print(f"Největší hodnota v seznamu je: {max_value}")

def find_min(values):
    min_value = min(values)
    print(f"Nejmenší hodnota v seznamu je: {min_value}")

values = list(map(int, input("Zadejte hodnoty oddělené mezerou: ").split()))

max_thread = threading.Thread(target=find_max, args=(values,))
min_thread = threading.Thread(target=find_min, args=(values,))
max_thread.start()
min_thread.start()

max_thread.join()
min_thread.join()
print("Vyhledávání dokončeno.")