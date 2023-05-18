# RPPOOP_HomeSync
HomeSync - An IoT based home automation mini-project.

Prerequisites:
1. Make sure the ESP32 is connected to the designated internet.

When we first open the Kivy application, it will check the internet connectivity. If the device running the app is not connected to WiFi or Internet, the app won't proceed to the login page.
Once the login page opens, the user has an option to create an account using the Sign Up hyperlink, or login to an existing account. The account username and password is verified during login by searching the elements in the database stored in Firebase protected database or in the ESP32 database. Incorrect login will display the corresponding error. When a signup account is created, it is appended to the end of the database. This way the account is stored.
The database is updated using an HTTP request to the server hosted by the ESP32 controller to make changes to the database.
Once logged in, the server opens doors for other requests: turning on or off the LEDs, fans, regulating the speed of the fan.
Even if the application is closed, the lights if ON, stay ON. Same with the fan.
On opening the application again and logging in, we will get the same status of the buttons as well.
