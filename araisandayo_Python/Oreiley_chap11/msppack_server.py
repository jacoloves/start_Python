from msgpackrpc import Server, Address

class Services():
    def double(selfself, num):
        return num * 2

server = Server(Services())
server.listen(Address("localhost", 6789))
server.start()