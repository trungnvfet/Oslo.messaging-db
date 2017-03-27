from oslo_config import cfg
import oslo_messaging as msg


class client(object):
    def __init__(self, transport, target):
        self.transport = transport
        self.target = target
        self._client = msg.RPCClient(self.transport, self.target)

    def test(self):
            self._client.call(ctxt={}, method = 'test', arg="Hey. This is testing my coding skills")

# Create Messaging Transport
transport = msg.get_transport(cfg.CONF)
# Create Target
target = msg.Target(topic='trungnv')

# Create RPC client
rpc_client = client(transport,target)

# Call function
rpc_client.test()