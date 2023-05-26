from main import *
import machine
import usocket as socket
import time
import network

server = Server('soham88gupte@gmail.com', 'soham-gupte')
server.connect_wifi('AndroidAPC371', 'passwordnahimilnar')
server.start_server()

# Code first starts with connecting to wifi
# Then waits for login to be successful
# After successful login, it will restore the previous states of the lights and fan
# Once operations done, when you press quit, it exits the start_server loop and goes back to check for the login
