
from __future__ import print_function
log = open("IP.txt", "w")


def ipRange(start_ip, end_ip):
   start = list(map(int, start_ip.split(".")))
   end = list(map(int, end_ip.split(".")))
   temp = start
   ip_range = []

   ip_range.append(start_ip)
   while temp != end:
      start[3] += 1
      for i in (3, 2, 1):
         if temp[i] == 256:
            temp[i] = 0
            temp[i-1] += 1
      ip_range.append(".".join(map(str, temp)))

   return ip_range


# sample usage
ip_range = ipRange("192.168.255.255", "192.170.0.25")
count=0
ip_limit=10000 #define how many ip you need
for ip in ip_range:
    data= 'host '+ ip +','
    count=count+1
    if count != ip_limit:
        print(data, file = log)
    else: break

print(count)
