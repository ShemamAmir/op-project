#if there are multiple packets, and a queue becomes saturated then the QoS or priority score is used.
#interact with json module
#load balancing in multipath routing
#http://en.wikipedia.org/wiki/Multipath_routing
#load balancing in multifple path decision 
#在乙太網協議中規定，同一區域網中的一台主機要和另一台主機進行直接通信，必須要知道目標主機的MAC地址。

class iplb (object):
  
  def __init__ (self, connection, service_ip, servers = []):
    self.service_ip = IPAddr(service_ip)
    self.servers = [IPAddr(a) for a in servers]
    self.con = connection
    self.mac = self.con.eth_addr
    self.live_servers = {} # IP -> MAC,port
    
  def 
  
  
  
  
class lw_ult (object):
"""
find the route withleast connection among the multiple routes
"""

class lw_pri (object):
"""
check priority
define priority(?)
"""

class lw_rrt (object):
"""
find the route with lowest ping time among the multiple routes
"""



def launch (ip, servers):
