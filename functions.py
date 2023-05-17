import machine
import usocket as socket
import time
import network

# Module for login and signup ... pending

def get_user(username) :
    with open("database.csv", "r") as file :
        lines = file.readlines()
    for line in lines:
        line = line.strip().split(",")
        if (line[0] == username) :
            return line
    file.close()
    
def invert_status(search_email, x):
    
    with open("database.csv", "r") as file:
        lines = file.readlines()

    for i in range(len(lines)):
        columns = lines[i].strip().split(",")
        if columns[0] == search_email:
            # Update the specific value
            columns[x] = str((int(columns[x])+1)%2)  # Update the second-to-last column
            # Reconstruct the modified line
            updated_line = ",".join(columns)
            # Replace the line in the list
            lines[i] = updated_line
            break

    with open("database.csv", "w") as file:
        for line in lines:
            file.write(line)
    
def update(search_email, x) :
    with open("database.csv", "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        columns = lines[i].strip().split(",")
        if columns[0] == search_email:
            # Update the specific values
            columns[x] = new_value  # Update the second-to-last column
            # Reconstruct the modified line
            updated_line = ",".join(columns)
            # Replace the line in the list
            lines[i] = updated_line

class HomeSync:
    
    def __init__(self, username) :
        self.LED0 = machine.Pin(2, machine.Pin.OUT)
        self.LED1 = machine.Pin(23, machine.Pin.OUT)
        self.LED2 = machine.Pin(14, machine.Pin.OUT)
        self.user = get_user(username)
        
class LivingRoom(HomeSync) :
    
    def toggle_led(self) :
        self.LED2.value(not int(self.user[6]))
        invert_status(self.user[0], 6)
        #time.sleep(0.5)
        

class Server:
    
    def __init__(self):
        self.timeout = 0
        self.wifi = network.WLAN(network.STA_IF)
        #self.HomeSync = HomeSync()

    def connect_wifi(self, ssid, password):
        self.wifi.active(False)
        time.sleep(0.5)
        self.wifi.active(True)

        self.wifi.connect(ssid, password)

        if not self.wifi.isconnected():
            print('Connecting...')
            while not self.wifi.isconnected() and self.timeout < 5:
                print(5 - self.timeout)
                self.timeout += 1
                time.sleep(1)

        if self.wifi.isconnected():
            print('Connected...')
            print('Network config:', self.wifi.ifconfig())

    def start_server(self, username):
        serv_user = HomeSync(username).user
        HomeSync(username).LED0.value(int(serv_user[4]))
        HomeSync(username).LED1.value(int(serv_user[5]))
        HomeSync(username).LED2.value(int(serv_user[6]))
        
        # Initializing socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET - Internet Socket, SOCK_STREAM - TCP protocol

        host = ''  # Empty means, it will allow all IP addresses to connect
        port = 80  # HTTP port
        # Need to wait some time before binding again
        s.bind((host, port))

        s.listen(5)  # It will handle a maximum of 5 clients at a time
        print("Server started...")
        
        while True:
            connection_socket, address = s.accept()  # Storing Conn_socket & address of a new client connected
            print("Got a connection from", address)
            request = connection_socket.recv(1024)  # Storing response coming from the client
            print("Content", request)  # Printing response
            request = str(request)  # Converting bytes to string
            # Comparing & Finding Position of a word in the string
            led_on0 = request.find('/led0')
            led_on1 = request.find('/led1')
            led_on2 = request.find('/led2')

            #if led_on0 == 6:
                #self.led_controller.toggle_led0()
            #if led_on1 == 6:
                #self.led_controller.toggle_led1()
            if led_on2 == 6:
                LivingRoom(username).toggle_led()
                

            connection_socket.close()
        
    
        
# Open the file in read mode

# <----------------------------------------------------->

#with open("database.csv", "r") as file:
    # Read all lines from the file
    #lines = file.readlines()
    # Process each line of the CSV file
    #for line in lines:
        # Remove any leading or trailing whitespace and newline characters
        #line = line.strip()
        # Split the line into individual columns using comma as the delimiter
        #columns = line.split(",")
        # Access data from each column using index
        #column1 = columns[0]
        #column2 = columns[1]
        #print(columns)