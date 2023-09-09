import socket


class TCPClient:
    """
    Class representing a TCP client for communication.
    """
    def request(self):
        """
        Send a request to the server.
        """

        print("=== Starting the client ===")

        try:
            # Create a socket
            client_socket = socket.socket()
            client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # Connect to the server
            print("=== Connecting to the server ===")
            client_socket.connect(("127.0.0.1", 80))
            print("=== Connection to the server established ===")

            # Retrieve the request to be sent to the server from a file
            with open("client_send.txt", "rb") as f:
                request = f.read()

            # Send the request to the server
            client_socket.send(request)

            # Wait and retrieve the response from the server
            response = client_socket.recv(4096)

            # Write the received response to a file
            with open("client_recv.txt", "wb") as f:
                f.write(response)

            # Close the communication
            client_socket.close()

        finally:
            print("=== Stopping the client. ===")


if __name__ == '__main__':
    client = TCPClient()
    client.request()