from oslo_config import cfg
import oslo_messaging as msg


class TestEndpoint(object):
    target = msg.Target(namespace='control', version='2.0')

    def test(self, ctx, arg):
        print("I am testing endpoint of server")
        print arg

# Create Messaging Transport
transport = msg.get_transport(cfg.CONF)

# Create Target
target = msg.Target(topic='trungnv', server='127.0.0.1')

# Create Endpoint
endpoints = [TestEndpoint(), ]

# Create RPC Server
server = msg.get_rpc_server(transport, target, endpoints, executor='blocking')

# Start RPX Server
server.start()
server.wait()

