from oslo_config import cfg
import oslo_messaging as messaging
import logging

LOG = logging.getLogger(__name__)


class TestClient(object):
    def __init__(self, transport, target):
        self.transport = transport
        self.target = target
        self._client = messaging.RPCClient(self.transport, self.target)

    def test(self):
        try:
            self._client.call(ctxt={}, method = 'test', arg='Hi Vietstack')
            self._client.call(ctxt={}, method = 'test2', arg='Hello Vietstack')
        except messaging.MessageDeliveryFailure:
            LOG.error("Fail")

    def prepare1(self):
        cctxt = self._client.prepare(namespace='control',version='2.0')
        cctxt.cast({}, 'do_something')

    def prepare2(self):
        cctxt = self._client.prepare(namespace='control',version='2.0')
        cctxt.cast({}, 'do_something')

target = messaging.Target(topic='test')
transport = messaging.get_transport(cfg.CONF)
client = TestClient(transport,target)
client.test()

client.prepare1()
client.prepare2()