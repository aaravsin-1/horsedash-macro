import time
import keyboard
import mouse
import threading

hotkey = "g"
RMB = "right"  # jump key
right = "d"
left = "a"
front = "w"
back = "s"
airRollRight = "e"
airRollLeft = "q"

# Shared state
running = False
thread = None

def HorseDash():
    global running
    mouse.press(RMB)
    time.sleep(0.064)
    if not running: return
    mouse.release(RMB)
    time.sleep(0.064)
    if not running: return
    keyboard.press('s')
    time.sleep(0.064)
    if not running: return
    keyboard.release('s')
    time.sleep(0.064)
    if not running: return
    keyboard.press('q')
    time.sleep(0.064)
    if not running: return
    keyboard.release('q')
    time.sleep(0.7)
    if not running: return
    keyboard.press('w')
    mouse.press(RMB)
    time.sleep(0.070)
    if not running: return
    mouse.release(RMB)
    time.sleep(0.045)
    if not running: return
    keyboard.release('w')
    time.sleep(0.040)
    if not running: return

    for i in range(30):
        if not running: break
        keyboard.press('s')
        mouse.press(RMB)
        time.sleep(0.045)
        mouse.release(RMB)
        time.sleep(0.045)
        keyboard.release('s')
        time.sleep(0.045)
        if not running: break
        keyboard.press('w')
        mouse.press(RMB)
        time.sleep(0.045)
        mouse.release(RMB)
        time.sleep(0.045)
        keyboard.release('w')
        time.sleep(0.045)

def toggle():
    global running, thread
    running = not running
    print(f"HorseDash {'started' if running else 'stopped'}")
    if running:
        thread = threading.Thread(target=HorseDash)
        thread.start()

# Main loop
print("Press 'g' to toggle HorseDash on/off.")
while True:
    if keyboard.is_pressed(hotkey):
        toggle()
        # Debounce: wait for key release
        while keyboard.is_pressed(hotkey):
            time.sleep(0.05)
    time.sleep(0.01)
