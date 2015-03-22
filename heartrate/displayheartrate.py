#!/usr/bin/python

from ant.easy.channel import Channel
from ant.easy.node import Node

import logging

NETWORK_KEY= [0xb9, 0xa5, 0x21, 0xfb, 0xbd, 0x72, 0xc3, 0x45]

class HeartRate:
    def setup_channel(self, node):
        channel = node.new_channel(Channel.Type.BIDIRECTIONAL_RECEIVE)

        channel.on_broadcast_data = self.on_data
        channel.on_burst_data = self.on_data

        channel.set_period(8070)
        channel.set_search_timeout(255)
        channel.set_rf_freq(57)
        channel.set_id(0, 120, 0)

        return channel

    def on_data(self, data):
        self.write_file(data[7])


    def write_file(self, heartrate): 
        f = file('/tmp/messages/heartrate', 'w')
        f.write('Heartrate: ' + str(heartrate))
        f.close()
    
logging.basicConfig()
logging.disable(logging.ERROR)

node = Node()
node.set_network_key(0x00, NETWORK_KEY)
heartrate = HeartRate()

channel_heart = heartrate.setup_channel(node)

try:
    channel_heart.open()
    node.start()
finally:
    node.stop()
