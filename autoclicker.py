import pyautogui
import keyboard
import time

# Ayarlar
TOGGLE_KEY = 'f3'  # Açma/kapama tuşu
CLICKS_PER_SECOND = 20  # Saniyede kaç tık yapılacağı (10x normal hız)
BUTTON = 'left'  # 'left' veya 'right' olarak değiştirilebilir

clicking_active = False

def toggle_clicking():
    global clicking_active
    clicking_active = not clicking_active
    status = "AKTİF" if clicking_active else "PASİF"
    print(f"AutoClicker {status} - Saniyede {CLICKS_PER_SECOND} {BUTTON} tık")

keyboard.add_hotkey(TOGGLE_KEY, toggle_clicking)
print(f"AutoClicker başlatıldı. Açmak/kapatmak için {TOGGLE_KEY.upper()} tuşuna basın.")

delay = 1 / CLICKS_PER_SECOND

while True:
    if clicking_active:
        pyautogui.click(button=BUTTON)
        time.sleep(delay)
    else:
        time.sleep(0.01)  # CPU kullanımını azaltmak için
