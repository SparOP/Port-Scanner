import sys
import socket
import threading

usage = "python3 port_scan.py TARGET START_PORT END_PORT"

print("*" * 60)
print("Welcome to my Port Scanner")
print("*" * 60)

if len(sys.argv) != 4:
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Error during name resolution")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning Target", target)

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    conn = s.connect_ex((target, port))
    if not conn:
        print("Port {} is OPEN".format(port))
    s.close()

threads = []
for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("Scanning completed.")