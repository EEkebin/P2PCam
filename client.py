import cv2
import pickle
import socket
import struct


def main():
    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip = "192.168.1.183"  # Replace with your laptop's IP address
    port = 12345

    client_socket.connect((host_ip, port))
    data = b""
    payload_size = struct.calcsize("L")

    while True:
        # Retrieve message length/size
        while len(data) < payload_size:
            data += client_socket.recv(4096)
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]

        # Retrieve all data based on size/length of message
        while len(data) < msg_size:
            data += client_socket.recv(4096)

        frame_data = data[:msg_size]
        data = data[msg_size:]

        # Extract the frame
        frame = pickle.loads(frame_data)

        # Display the frame
        cv2.imshow("Received", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):  # q to quit
            break

    client_socket.close()


if __name__ == "__main__":
    main()
