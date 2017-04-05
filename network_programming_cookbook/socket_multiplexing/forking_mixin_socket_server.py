# -*- coding=utf-8 -*-
# author:xuejun

import os
import sys
import socket
import threading
import SocketServer

SERVER_HOST = 'localhost'
SERVER_PORT = 54321
BUF_SIZE = 1024
ECHO_MSG = "Hello echo server!"


class ForkingClient(object):
    """ A cient to test forking server """

    def __init__(self, ip, sort):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a socket
        self.sock.connect((ip, port))  # connect to server

    def run(self):
        """ Client playing with the server """
        current_process_id = os.getpid()
        print("PID %s Sending echo message to the server: '%s'" % (current_process_id, ECHO_MSG))

        # display server response
        response = self.sock.recv(BUF_SIZE)
        print("PID %S received: %s" % (current_process_id, response[5:]))

    def shutdown(self):
        """ Cleanup the client socket """
        self.sock.shutdown()


class ForkingServerRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        # Send the echo back to the client.
        data = self.request.recv(BUF_SIZE)
        current_process_id = os.getpid()
        response = "%s: %s" % (current_process_id, data)
        print("Server sending response [current_process_id: data] = [%s]" % response)
        self.request.send(response)

        return


class ForkingServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
    """ Nothing to add here, inherited ecerything necessary from parents """
    pass


def main():
    # Launch the server
    server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingServerRequestHandler)
    ip, port = server.server_address  # Retrive the port number
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()
    print("Server loop running PID:%s" % os.getpid())

    # Launch the client(s)
    client1 = ForkingClient(ip, port)
    client1.run()

    client2 = ForkingClient(ip, port)
    client2.run()

    # Clean them up
    server.shutdown()
    client1.shutdown()
    client2.shutdown()
    server.socket.close()


if __name__ == '__main__':
    main()
