from ipaddress import IPv4Network as IPv4
import random

class RandomNetwork(IPv4):

    def __init__(self, mask_start, mask_end):
        IPv4.__init__(
            self,
            (
                random.randint(0x0B000000, 0xDF000000),
                random.randint(mask_start, mask_end)
            ),
            strict = False
            )

ddos_list = []

while len(ddos_list) < 30:
    rnet = RandomNetwork(8, 24)
    if rnet not in ddos_list and rnet.is_private == False:
        ddos_list.append(rnet)

for net_ddos in sorted(ddos_list):
    print(net_ddos)
