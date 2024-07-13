def fun(str):
    if str == '':
        return False
    else:
        return True



ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_route = ospf_route.split(' ')
print(ospf_route)
ospf_route = list(filter(fun, ospf_route))
print(ospf_route)
ospf_route = [x.replace(',', '') for x in ospf_route]
ospf_route = [x.replace('[', '') for x in ospf_route]
ospf_route = [x.replace(']', '') for x in ospf_route]
ospf_route.pop(2)


heading = ['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
print(len(heading))
print(len(ospf_route))

for x, y in zip(heading, ospf_route):
    print("%-20s, %-10s" % (x, y))
