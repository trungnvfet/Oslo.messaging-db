from oslo_config import cfg
import oslo_messaging as messaging


class ServerCotrolEndpoint(object):
    target = messaging.Target(namespace='control', version='2.0')

    def __init__(self, server):
        self.server = server

    def do_something(self, cxtx):
        if self.server:
            print ("## Hello Vietstack")
            self.server.do_something()
        print ("## Hi Vietstack")


class TestEndpoint(object):
    def test(self, cxtx, arg):
        print("I am testing endpoint 1 of server")
        print arg


class TestEndpoint2(object):
    def test2(self, cxtx, arg):
        print("I am testing endpoint 2 of server")
        print arg

# Create Messaging Transport
transport = messaging.get_transport(cfg.CONF)

# Create Target
target = messaging.Target(topic='test', server='server1')

# Create Endpoint
endpoints = [
            ServerCotrolEndpoint(None),
            TestEndpoint(),
            TestEndpoint2()
            ]
# Create RPC Server
server = messaging.get_rpc_server(transport, target, endpoints, executor='blocking')

# Start RPX Server
server.start()
server.wait()