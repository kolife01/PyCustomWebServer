import socket


class TCPServer:
    """
    Class representing a TCP server for communication.
    """
    def serve(self):
        """
        Start the server.
        """

        print("=== Starting the server ===")

        try:
            # Create a socket
            server_socket = socket.socket()
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # Assign the socket to localhost on port 8080
            server_socket.bind(("localhost", 8080))
            server_socket.listen(10)

            # Wait for an external connection and establish the connection once it's made
            print("=== Waiting for a client connection ===")
            (client_socket, address) = server_socket.accept()
            print(f"=== Connection established with the client. remote_address: {address} ===")

            # Retrieve the data sent from the client
            request = client_socket.recv(4096)

            # Write the received data to a file
            with open("server_recv.txt", "wb") as f:
                f.write(request)

            # Retrieve the response to be sent to the client from a file
            with open("server_send.txt", "rb") as f:
                response = f.read()

            # Send the response to the client
            client_socket.send(response)

            # Close the connection without sending any response
            client_socket.close()

        finally:
            print("=== Stopping the server. ===")


if __name__ == '__main__':
    server = TCPServer()
    server.serve()
