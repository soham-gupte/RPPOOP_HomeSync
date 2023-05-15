import pyrebase

config = {
    "apiKey": "AIzaSyBJOviULBXyXD8vrjersJMNiDKzEGquSFY",
    "authDomain": "rppoophomesync.firebaseapp.com",
    "projectId": "rppoophomesync",
    "databaseURL": "https://rppoophomesync-default-rtdb.firebaseio.com/",
    "storageBucket": "rppoophomesync.appspot.com",
    "messagingSenderId": "731212374838",
    "appId": "1:731212374838:web:d505053ccdf94005eb0997",
    "measurementId": "G-W6B8DV84RJ"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

data = {"Username": "soham88gupte@gmail.com", 
        "Password": "helloworld",
        "LED0": 0, "LED1": 0, "LED2": 0, "LED3": 0, "Fan": 0}

def invert_status(pin) :
    y = database.child("User1").get().val()[pin]
    y = not y
    database.child("User1").update({pin: y})

invert_status("LED0")