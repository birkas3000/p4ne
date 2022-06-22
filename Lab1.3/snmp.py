from pysnmp.hlapi import *

results_get = getCmd(
    SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget(('10.31.70.107', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
)

results_next = nextCmd(
    SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget(('10.31.70.107', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
    lexicographicMode=False
)

for results in results_get:
    print('Error Indication: {}'.format(results[0]))
    print('Error Status: {}'.format(results[1]))
    print('Error Index: {}'.format(results[2]))
    for result in results[3]:
        print(result)
    print('\n')

for results in results_next:
    print('Error Indication: {}'.format(results[0]))
    print('Error Status: {}'.format(results[1]))
    print('Error Index: {}'.format(results[2]))
    for result in results[3]:
        print(result)
    print('\n')