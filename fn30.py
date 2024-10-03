# 4 oy 7 dars vazifasining 4 - masalasi

fayl_nomi = "misol.txt"

try:
    with open(fayl_nomi, 'r') as fayl:
        matn = fayl.read()  
        sozlar = matn.split()  

        if sozlar:  
            eng_qisqa_soz = min(sozlar, key=len)
            eng_uzun_soz = max(sozlar, key=len)

            print(f"Eng qisqa so'z: '{eng_qisqa_soz}'")
            print(f"Eng uzun so'z: '{eng_uzun_soz}'")
        else:
            print("Faylda hech qanday so'z topilmadi.")

except FileNotFoundError:
    print(f"{fayl_nomi} fayli topilmadi.")