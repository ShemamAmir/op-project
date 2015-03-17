
from __future__ import print_function
log = open("C:\Users\O609787\Desktop\ip_list.txt", "w+")


def ipRange(start_ip, end_ip):
   start = list(map(int, start_ip.split(".")))
   end = list(map(int, end_ip.split(".")))
   temp = start
   ip_range = []

   ip_range.append(start_ip)
   while temp != end:
      start[3] += 1
      for i in (3, 2, 1):
         if temp[i] == 256:  #3.2.1.0
            temp[i] = 1
            temp[i-1] += 1
      ip_range.append(".".join(map(str, temp)))

   return ip_range


# sample usage
ip_range = ipRange("10.0.0.255", "10.0.1.2")
count=0
ip_limit=501 #define how many ip you need
for ip in ip_range:
	if count != ip_limit:
		count=count+1
		data= 'host '+ ip +','
		print(data, file = log)
	else: break


print(count)
