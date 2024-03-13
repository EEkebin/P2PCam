import cv2
import pickle
import socket
import struct


def main():
    # Initialize camera, change the value inside cv2.VideoCapture() to switch to a different VideoCapture device, if not working.
    cap = cv2.VideoCapture(0)

    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print("HOST IP:", host_ip)
    port = 12345
    socket_address = (host_ip, port)

    # Bind socket
    server_socket.bind(socket_address)
    server_socket.listen(5)
    print("Listening on:", socket_address)

    # Accept a client connection
    client_socket, addr = server_socket.accept()
    print("Connected from:", addr)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Serialize the frame
        data = pickle.dumps(frame)

        # Send a message length first
        message_size = struct.pack("L", len(data))

        # Send the data
        client_socket.sendall(message_size + data)


if __name__ == "__main__":
    main()
