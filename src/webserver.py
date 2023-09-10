import socket
from datetime import datetime


class WebServer:
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

            # generate response body
            response_body = "<html><body><h1>It works!</h1></body></html>"

            # generate response line
            response_line = "HTTP/1.1 200 OK\r\n"

            # generate response header
            response_header = ""
            response_header += f"Date: {datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}\r\n"
            response_header += "Host: HenaServer/0.1\r\n"
            response_header += f"Content-Length: {len(response_body.encode())}\r\n"
            response_header += "Connection: Close\r\n"
            response_header += "Content-Type: text/html\r\n"

            # generate response
            response = (response_line + response_header + "\r\n" + response_body).encode()

            # Send the response to the client
            client_socket.send(response)

            # Close the connection without sending any response
            client_socket.close()

        finally:
            print("=== Stopping the server. ===")


if __name__ == '__main__':
    server = WebServer()
    server.serve()
