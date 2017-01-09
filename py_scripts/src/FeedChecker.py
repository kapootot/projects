import http.client
import smtplib
from email.mime.text import MIMEText


def get_status_code(host, path="/feeds/il/en/competitions/140/1495/matches/472905.json"):

    try:
        conn = http.client.HTTPConnection(host)
        conn.request("GET", path)
        return conn.getresponse().status
    except Exception:
        return "Something is wrong!"


def checkFeed():
    status = get_status_code("feedmonster.onefootball.com")

    if (status == 200):
        message = "\nFeed is alive"
        print(message)
        return True
    else:
        message = "\nSomething's wrong. \n\nStatus code is: "+ str(status)
        print(message)
        return False


if __name__ == '__main__':
    checkFeed()






