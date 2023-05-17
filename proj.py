from functions import *
import machine
import usocket as socket
import time
import network

server = Server()
server.connect_wifi('OnePlus Nord', 'Qwertyuiop')
server.start_server('soham88gupte@gmail.com')