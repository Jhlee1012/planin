from concurrent.futures import thread
from threading import Thread
import time

class Main:
    thread = Thread()
    active = False
    current = time.time()

    def start() :
        print("!!!start!!!")
        
        Main.active = True
        thread = Thread(target=Main.update, args=())
        thread.start()

    def stop() :
        if(not Main.active): return
        Main.active = False
        print(f"!!!stop!!!")


    def update() :
        while Main.active:
            current = time.time()
            if current - Main.current < 1: continue
            else: Main.current = current

            print(f"!!!update!!!")
