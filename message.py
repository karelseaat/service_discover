
import struct

class message():
    buff = b""
    pos = 0

    def __len__(self):
        """ get the length of buffer """
        return len(self.buff) - self.pos

    def add(self, data):
        """ add raw data to the buffer """
        self.buff += data

    def save(self):
        self.buff = self.buff[self.pos:]
        self.pos = 0

    def restore(self):
        self.pos = 0

    def discard(self):
        """ empty the buffer """
        self.pos = 0
        self.buff = b""

    def read(self, length=None):
        """ read the buffer and set the pointer where you stopped reading"""
        if length is None:
            data = self.buff[self.pos:]
            self.pos = len(self.buff)
        else:
            if self.pos + length > len(self.buff):
                raise BufferUnderrun()

            data = self.buff[self.pos:self.pos+length]
            self.pos += length

        return data


    def unpack(self, fmt):
        fmt = ">"+fmt
        length = struct.calcsize(fmt)
        fields = struct.unpack(fmt, self.read(length))
        if len(fields) == 1:
            fields = fields[0]
        return fields

    def pack(self, fmt, *fields):
        """ pack but make sure it is big endian """
        return struct.pack(">"+fmt, *fields)

    def unpack_short_int(self):
        """ unpack a byte as a shortint """
        return self.unpack('B')

    def pack_short_int(self, num):
        """ pack a shortint as a byte """
        return self.pack("B", num)

    def pack_int(self, num):
        return self.pack("i", num)

    def unpack_int(self):
        return self.unpack("i")

    def pack_servers(self, servers):
        thestring = b""
        thestring = self.pack_short_int(len(servers['servers']))
        for server in servers['servers']:
            thestring += self.pack_server(server)

        return thestring

    def pack_server(self, server):
        ipparts = server['ip'].split(".")
        return self.pack_short_int(int(ipparts[0])) + self.pack_short_int(int(ipparts[1])) + self.pack_short_int(int(ipparts[2])) + self.pack_short_int(int(ipparts[3])) + self.pack_int(int(server['port']))

    def unpack_server(self):
        return {'ip': str(self.unpack_short_int()) + "." + str(self.unpack_short_int()) + "." + str(self.unpack_short_int()) + "." + str(self.unpack_short_int()), 'port': self.unpack_int()}

    def unpack_servers(self):
        servers = []
        length = int(self.unpack_short_int())
        for server in range(0, length):
            servers.append(self.unpack_server())
        return servers
