import os
import shutil
import threading

def kopiruj_adresar(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    pocet_souboru = 0
    pocet_slozek = 0

    for cesta, slozky, soubory in os.walk(src):
        struktura = os.path.join(dst, os.path.relpath(cesta, src))
        if not os.path.exists(struktura):
            os.makedirs(struktura)
            pocet_slozek += 1

        for soubor in soubory:
            zdroj_soubor = os.path.join(cesta, soubor)
            cilovy_soubor = os.path.join(struktura, soubor)
            shutil.copy2(zdroj_soubor, cilovy_soubor)
            pocet_souboru += 1
    print(f"Kopírování dokončeno. Počet zkopírovaných souborů: {pocet_souboru}, počet složek: {pocet_slozek}.")

def main():
    src = input("Zadej cestu k existujícímu adresáři: ")
    dst = input("Zadejte cestu k novému adresáři: ")

    if not os.path.exists(src):
        print("Zadaný adresář neexistuje.")
        return

    kopirovaci_vlakno = threading.Thread(target=kopiruj_adresar, args=(src, dst))
    kopirovaci_vlakno.start()

    kopirovaci_vlakno.join()
    print("Kopírování je HOTOVO.")

main()
