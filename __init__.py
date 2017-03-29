from oslo_config import cfg

cfg.CONF.register_group(cfg.OptGroup(
    name='oslo_messaging_rabbit', title="Configuration for Testing"
))

cfg.CONF.register_opts([
    cfg.StrOpt('rabbit_userid',
               help="The name of userid"),
    cfg.StrOpt('rabbit_password',
               help="The name of password"),
    cfg.StrOpt('rabbit_virtual_host',
               help="The name of virtual_host"),
    cfg.BoolOpt('rabbit_use_ssl',
                help="The name of use_ssl"),
    cfg.ListOpt('rabbit_hosts',
                default=['127.0.0.1:5672'],
                help='Host:port pairs to listen on'),
], group='oslo_messaging_rabbit')
