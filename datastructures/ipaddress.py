def iptoBinary(ip):
    ipArray=ip.split(".")
    ipArray=filter(None, ipArray)
    ipbin=[]
    for i in range(len(ipArray)):
        ipbin.append('{0:08b}'.format(int(ipArray[i])))
    return ipbin