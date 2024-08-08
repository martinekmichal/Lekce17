import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

try:
    while True:
        message = input("zadej zproavu pro server: ")
        client_socket.sendall("Ahoj, server!".encode())
        response = client_socket.recv(1024).decode()
        print(f"Odpoveď zo servera: {response}")
        if message == "konec":
            break
finally:
    client_socket.close()
    print("Client ukončil komunikaci")

