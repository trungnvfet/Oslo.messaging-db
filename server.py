from oslo_config import cfg
import oslo_messaging as msg


class TestEndpoint(object):
    def test_method1(self, ctx, arg):
        print("I am testing endpoint 1 of server")
        print arg

    def test_method2(self, ctx, arg):
        print("I am testing endpoint 2 of server")
        print arg

# Create Messaging Transport
transport = msg.get_transport(cfg.CONF)

# Create Target
target = msg.Target(topic='trungnv', server='server1')

# Create Endpoint
endpoints = [
            TestEndpoint()
            ]

# Create RPC Server
server = msg.get_rpc_server(transport, target, endpoints, executor='blocking')

# Start RPX Server
server.start()
server.wait()

