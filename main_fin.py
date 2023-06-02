import machine
import usocket as socket
import time
import network

FAN_SPEEDS = [150, 60, 55, 50, 40, 30]

def get_user(username) :
    with open("database.csv", "r") as file :
        lines = file.readlines()
    for line in lines:
        line = line.strip().split(",")
        if (line[9] == username) :
            return line
    
def update_status(search_email, user_status) :
    with open("database.csv", "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        columns = lines[i].split(",")
        if columns[9] == search_email:
            updated_line = ",".join(user_status)
            lines[i] = updated_line
            break

    with open("database.csv", "w") as file:
        for line in lines:
            print(line)
            file.write(line)

class HomeSync:
    
    def __init__(self, username) :
        self.username = username
        self.user_stats = get_user(self.username)
        print(self.user_stats)
        
class Bedroom(HomeSync) :
    
    def __init__(self, username) :
        super().__init__(username)
        self.LED3 = machine.Pin(25, machine.Pin.OUT)
        self.LED3.value(int(self.user_stats[7]))
        
    def toggle_light(self, z) :
        x = (int(z[7])+1)%2
        self.LED3.value(x)
        z[7] = str(x)
        print(z)

class DiningRoom(HomeSync) :
    
    def __init__(self, username) :
        super().__init__(username)
        self.LED2 = machine.Pin(26, machine.Pin.OUT)
        self.LED2.value(int(self.user_stats[6]))
        
    def toggle_light(self, z) :
        x = (int(z[6])+1)%2
        self.LED2.value(x)
        z[6] = str(x)
        print(z)
        
class Kitchen(HomeSync) :
    
    def __init__(self, username) :
        super().__init__(username)
        self.LED1 = machine.Pin(13, machine.Pin.OUT)
        self.LED1.value(int(self.user_stats[5]))
        
    def toggle_light(self, z) :
        x = (int(z[5])+1)%2
        self.LED1.value(x)
        z[5] = str(x)
        print(z)
    
class LivingRoom(HomeSync) :
    
    def __init__(self, username) :
        super().__init__(username)
        self.LED0 = machine.Pin(12, machine.Pin.OUT)
        self.LED0.value(int(self.user_stats[4]))
        self.FAN_pin = machine.Pin(14)
        self.FAN = machine.PWM(self.FAN_pin, freq=50)
        self.FAN.duty(int(self.user_stats[8]))
    
    def toggle_light(self, z) :
        x = (int(z[4])+1)%2
        self.LED0.value(x)
        z[4] = str(x)
        print(z)
        
    def set_fan_speed(self, x, z) :
        y = FAN_SPEEDS[x]
        self.FAN.duty(y)
        z[8] = str(y)

class Server:
    
    def __init__(self):
        self.wifi = network.WLAN(network.STA_IF)
        wifi_check = None
        
    def connect_wifi(self, ssid, password):
        self.timeout = 0
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
            print('Gateway number:', self.wifi.ifconfig()[2])
            wifi_check = self.wifi.ifconfig()[2]
            return 1
        return 0
            
    def auth_login(self, username, password) :
        with open("database.csv", "r") as file :
            lines = file.readlines()
        for line in lines:
            line = line.strip().split(",")
            if (line[9] == username and line[1] == password) :
                return True
        return False
    
    def signup(self, request) :
        with open('database.csv', 'a') as file:
            file.write(f"\n{request[0]},{request[1]},{request[2]},{request[3]},0,0,0,0,150,{request[4]}")
            
    def init_server(self) :
        
        # Initializing socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET - Internet Socket, SOCK_STREAM - TCP protocol

        host = ''  # Empty means, it will allow all IP addresses to connect
        port = 80  # HTTP port
        # Need to wait some time before binding again
        s.bind((host, port))

        s.listen(5)  # It will handle a maximum of 5 clients at a time
        
        self.s = s
        print("Server started...")
    
    def start_server(self) :
        
        while True :
            self.username = "USERNAME"
            connection_socket, address = self.s.accept()
            request = connection_socket.recv(1024)  # Storing response coming from the client
            print("Content", request)  # Printing response
            request = str(request)
            if request.find('/signup/') == 22 :
                request = request[30:-1]
                request = request.split('/')
                print(request)
                self.signup(request)
                continue
            request = request[23:-1]
            request = request.split('/')
            print(request)
            if self.auth_login(request[0], request[1]) :
                print("Valid login!")
                connection_socket.send(bytes("1", "utf-8"))
                connection_socket.close()
                self.username = request[0]
                break
            else :
                print("Invalid login!")
                connection_socket.send(bytes("0", "utf-8"))
                connection_socket.close()
        
        self.user_stats = get_user(self.username)
        self.homesync = HomeSync(self.username)
        self.living_room = LivingRoom(self.username)
        self.kitchen = Kitchen(self.username)
        self.dining_room = DiningRoom(self.username)
        self.bedroom = Bedroom(self.username)
            
        while True :
            
            connection_socket, address = self.s.accept()  # Storing Conn_socket & address of a new client connected
            print("Got a connection from", address)
            request = connection_socket.recv(1024)  # Storing response coming from the client
            print("Content", request)  # Printing response
            request = str(request)  # Converting bytes to string
            # Comparing & Finding Position of a word in the string
            
            exit_status = request.find('/exit')
            led_on0 = request.find('/led0')
            led_on1 = request.find('/led1')
            led_on2 = request.find('/led2')
            led_on3 = request.find('/led3')
            fan_stat = request.find('/fan')
            
            if led_on0 == 6:
                self.living_room.toggle_light(self.user_stats)
            elif led_on1 == 6:
                self.kitchen.toggle_light(self.user_stats)
            elif led_on2 == 6:
                self.dining_room.toggle_light(self.user_stats)
            elif led_on3 == 6:
                self.bedroom.toggle_light(self.user_stats)
            elif fan_stat == 6:
                self.living_room.set_fan_speed(int(request[10]), self.user_stats)
                
            connection_socket.close()
            
            if exit_status == 6:
                update_status(self.username, self.user_stats)
                break
            
        self.living_room.LED0.value(0)
        self.kitchen.LED1.value(0)
        self.dining_room.LED2.value(0)
        self.bedroom.LED3.value(0)
        self.living_room.FAN.duty(150)