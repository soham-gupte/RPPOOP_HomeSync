import socket
import pyrebase

ssid_to_connect = "192.168.43.37".split('.')

firebaseConfig = {
    "apiKey": "AIzaSyBJOviULBXyXD8vrjersJMNiDKzEGquSFY",
    "authDomain": "rppoophomesync.firebaseapp.com",
    "databaseURL": "https://rppoophomesync-default-rtdb.firebaseio.com",
    "projectId": "rppoophomesync",
    "storageBucket": "rppoophomesync.appspot.com",
    "messagingSenderId": "731212374838",
    "appId": "1:731212374838:web:d418480d658f5eaaeb0997",
    "measurementId": "G-67X55W8FJJ"
}

firebase = pyrebase.initialize_app(firebaseConfig) 
database = firebase.database()

# data = {
#     "Email": "pranjali_jadhav@gmail.com",
#     "Password": "KivyIsAmazing",
#     "First": "Pranjali",
#     "Last": "Jadhav",
#     "LED0": 0,
#     "LED1": 0,
#     "LED2": 0,
#     "LED3": 0,
#     "FAN_STAT": 150,
#     "USERNAME": "pranjaaa"
# }

# database.child("Users").child(data["USERNAME"]).set(data)
# user = database.child("Users").get().val()
# print(user.items())
# for k,v in user.items() :
    # print(k, v["Email"])


def check_username(username) :
    user = database.child("Users").get().val()
    for db_username, details in user.items() :
        if (username == db_username) :
            return True
    return False

def check_email(email) :
    user = database.child("Users").get().val()
    for db_username, details in user.items() :
        if (details["Email"] == email) :
            return True
    return False

def check_login(username, password) :
    user = database.child("Users").get().val()
    for db_username, details in user.items() :
        if (details["USERNAME"] == username and details["Password"] == password) :
            return True
    return False

def check_internet_connection():
        try:
            # Attempt to connect to a well-known website
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            # Connection failed
            return False
        
def check_connection_with_esp():
    app_ip = socket.gethostbyname(socket.gethostname())
    app_ip = app_ip.split('.')
    print(app_ip)
    print(ssid_to_connect)
    for i in range(0,3) :
        if ssid_to_connect[i] == app_ip[i] :
            pass
        else :
            return False
    return True