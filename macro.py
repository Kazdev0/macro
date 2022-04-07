import mouse #Mouse kütüphanesi ile Mouseunuzu Rahatça Kontrol edebilirsiniz
import time #Zaman 
import keyboard
while True:
    if keyboard.is_pressed('ctrl') & keyboard.is_pressed("u"):
        i=1
        print("Macro Başlatıldı")
        while i < 10000000:  # making a loop
            time.sleep(0.09)
            mouse.click()
            print("Macro Devam Ediyor")
            i+=1
            if keyboard.is_pressed('ctrl') & keyboard.is_pressed("y"):
                break
