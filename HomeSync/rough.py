# firebaseConfig = {
#     "apiKey": "AIzaSyBJOviULBXyXD8vrjersJMNiDKzEGquSFY",
#     "authDomain": "rppoophomesync.firebaseapp.com",
#     "databaseURL": "https://rppoophomesync-default-rtdb.firebaseio.com",
#     "projectId": "rppoophomesync",
#     "storageBucket": "rppoophomesync.appspot.com",
#     "messagingSenderId": "731212374838",
#     "appId": "1:731212374838:web:d418480d658f5eaaeb0997",
#     "measurementId": "G-67X55W8FJJ"
# }
import requests

email = "example@example.com"  # Replace with the actual email
password = "password123"  # Replace with the actual password
first_name = "John"  # Replace with the actual first name
last_name = "Doe"  # Replace with the actual last name
username = "johndoe"  # Replace with the actual username

# Create the data payload
data = {
    "Email": email,
    "Password": password,
    "First": first_name,
    "Last": last_name,
    "LED0": 0,
    "LED1": 0,
    "LED2": 0,
    "LED3": 0,
    "FAN_STAT": 150,
    "USERNAME": username
}
response = requests.post("http://192.168.43.37", json=data)
if response.status_code == 200:
    print("User details sent successfully to Firebase.")
else:
    print("Failed to send user details to Firebase.")