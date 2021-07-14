import ipaddress

ipI = '192.168.0.1'
ipN = '192.168.0.0/24'

endereco = ipaddress.ip_address(ipI)
rede = ipaddress.ip_network(ipN, strict=False)

#print(endereco)
#print(rede)

for ipN in rede:
    print(ipN)