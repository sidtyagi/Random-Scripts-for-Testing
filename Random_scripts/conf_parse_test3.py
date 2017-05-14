'''
Created on Jan 7, 2017

@author: sidtyagi
'''
import time,re
from ciscoconfparse import CiscoConfParse


#this function takes the vrf(if any),the next hop ip and returns the relevant config 
def get_the_static_route_config(vrf_name,far_end_ip):
    parse_9k=CiscoConfParse('phase3-BLR-MPL-PE-RTR-188_Running_Config_28-DEC-2016.iox')
    next_hop=parse_9k.find_objects(r'/[0-9]+\s+'+far_end_ip)
    for k1 in next_hop:
        config=''
        next_hop_parent=k1.parent
        '''next_hop_parent will be something like 'address-family ipv4 unicast'''
        if 'address-family ipv4 unicast' in next_hop_parent.text:
            if vrf:
                parent_of_next_hop_parent=next_hop_parent.parent
                '''the above should have vrf name '''
                
                parent_of_parent_of_next_hop_parent=parent_of_next_hop_parent.parent
                
                #print parent_of_parent_of_next_hop_parent.text
                #the above will be router static
                
                #print parent_of_next_hop_parent.text
                #the above will be vrf name
                if 'vrf '+vrf_name in parent_of_next_hop_parent.text and 'router static' in parent_of_parent_of_next_hop_parent.text:
                    print 'hi'
                    config+='\n'+parent_of_parent_of_next_hop_parent.text+'\n'+parent_of_next_hop_parent.text+'\n'+next_hop_parent.text
                    for k2 in next_hop_parent.children:
                        chk=re.search(r"\b" + re.escape(far_end_ip) + r"\b",k2.text)                        
                        if chk:                            
                            config+='\n'+k2.text
                    print config
                    break
            if not vrf:
                parent_of_next_hop_parent=next_hop_parent.parent
                '''the above should have router static '''          
                
                #print parent_of_next_hop_parent.text
                #the above will be vrf name
                if 'router static' in parent_of_next_hop_parent.text:
                    print 'hi'
                    config+='\n'+parent_of_next_hop_parent.text+'\n'+next_hop_parent.text
                    for k2 in next_hop_parent.children:
                        chk=re.search(r"\b" + re.escape(far_end_ip) + r"\b",k2.text)
                        if chk:
                            config+='\n'+k2.text
                    print config
                    break
            
                        
                    
        

#vrf='AO-PRODUCTS-H'
vrf=''
#far_end_ip="10.10.10.10"
far_end_ip='10.10.10.10'
get_the_static_route_config(vrf, far_end_ip)

