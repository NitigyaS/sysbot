import requests
import getpass
import socket

def post_to_slack(message,url):

    headers = {
        'content-type': "application/json"
    }
    payload = '{ "text": "' + message + '" }'
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == 200:
        return "Your Message has bee posted successfuly. :D"
    else:
        return "Mesage not Posted !"


def create_message(arguments):
    if len(arguments) == 2:
        message = arguments[1]
        username = getpass.getuser()
        hostname = socket.gethostname()
    elif len(arguments) == 3:
        username = arguments[2]
        message = arguments[3]
    print "*" + username + "* on *" + hostname + "* : " + message
    return "*"+username + "* on *" + hostname + "* : " + message
