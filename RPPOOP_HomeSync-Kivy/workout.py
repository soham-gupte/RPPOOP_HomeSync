import socket
from kivy.app import App

class MyApp(App):
    def send_request(self, command):
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set the host and port for the socket
        host = '192.168.1.2'
        port = 80

        # Connect to the server
        s.connect((host, port))

        # Send the command to the server
        request = "GET " + command + " HTTP/1.1\r\nHost: " + host + "\r\n\r\n"
        s.send(request.encode())

        # Receive the response from the server
        response = s.recv(1024)

        # Close the socket
        s.close()

MyApp().run()
