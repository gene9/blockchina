
print '#!/bin/sh\n'

print 'sudo iptables -F "chinadrop"'
print 'sudo iptables -X "chinadrop"'

print 'sudo iptables -N "chinadrop"'

for line in open('cn.zone'):
    line = line.strip()
    if not line:
        continue

    print 'sudo iptables -A "chinadrop" -s {0} -j DROP'.format(line)
