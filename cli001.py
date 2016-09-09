import socket
import os

def getarp():
  #os.system('ip neigh flush dev wlan0')
  #os.system('arp -a')

  file1 = open("/proc/net/arp", "r")
  file2 = file("arp.txt","wb")
  while True:
    line = file1.readline()
    if line:  #do something here
      #print line
      arp = line
      if "172.24.1" in arp:
          #print "yes"
          #print arp
          file2.writelines(arp)
    else:  #erro
      #print "open arp wrong."
      break
  file1.close()
  file2.close()
  return 0

def finarp():
  count = 0
  nicearp = ""
  file3 = open("arp.txt","r")
  while True:
    line = file3.readline()
    if line:
        countstr = str(count)
        firstarp = line
        nicearp += firstarp[:12]
        nicearp += countstr
        nicearp += ","
        nicearp += firstarp[41:58]
        nicearp += countstr
        nicearp += "&"
        count += 1
    else:
        break
  #print nicearp
  file3.close()
  return nicearp

#print finarp()


getarp()
s = socket.socket()
host = socket.gethostname()
port = 12345

arp = finarp()
#arp = "yes"
#print arp
s.connect((host, port))
s.send(arp)
print s.recv(1024)
s.close()
                                                         Top
