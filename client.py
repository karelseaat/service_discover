#!/usr/bin/env python

import socket
from message import message
import time


class Client:

    def __init__(self, addport):
        self.mesg = message()
        self.addport = addport
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('', 6666))

        self.server_addr = None
        self.lisoservers = []
        self.refreshtime = 10

        self.lasttime = 0

    def parse_self_server(self):
        tempservers = []
        for server in self.lisoservers:
            if server['ip'] == "0.0.0.0":
                server['ip'] = self.server_addr
            tempservers.append(server)

        self.lisoservers = tempservers


    def discover(self):
        if time.time() > self.lasttime:
            self.lasttime = time.time() + self.refreshtime
            listoserver = []
            data, addr = self.sock.recvfrom(1024)
            self.server_addr = addr
            self.mesg.add(data)
            self.lisoservers = self.mesg.unpack_servers()
            self.mesg.discard()
            self.parse_self_server()

    def all_servers(self):
        return self.lisoservers

    def get_server_with_port(self, port):
        aserver = None

        for server in self.listoserver:
            if server.port == port:
                aserver = server

        return aserver

    def server_ports(self):
        return [server['port'] for server in self.lisoservers]

def main():

    aclient = Client(None)

    while True:
        aclient.discover()
        print(aclient.all_servers())


if __name__ == "__main__":
    main()
