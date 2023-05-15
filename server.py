#!/usr/bin/env python

import socket
from time import sleep

from yaml import load, dump, Loader
from message import message

mesg = message()

def make_servers(settings):
    results = mesg.pack_servers(settings)
    mesg.discard()
    return results


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.settimeout(2.0)

    settings = load(open("settings.yml", 'r'), Loader=Loader)

    while True:

        sock.sendto(make_servers(settings), ("localhost", 6666))
        sleep(1)


if __name__ == "__main__":

    main()
