from netica import Netica
import numpy as np
 
# initialize class
ntc = Netica()
 
# create new environment
env = ntc.newenv()
# initialize environment
ntc.initenv(env)
# create new net
net_p = ntc.newnet('BNZeebrugge', env)
 
# define nodes
nodeBC1 = ntc.newnode('PeakWaterLevel', 5, net_p)
ntc.setnodelevels(nodeBC1, 5, np.asarray([6.35, 7.1, 7.4, 7.8, 7.9], dtype='float64'))
ntc.setnodetitle(nodeBC1,'Peak Water Level (m)')

nodeBC2 = ntc.newnode('MaxSignificantWaveHeight', 5, net_p)
ntc.setnodelevels(nodeBC2, 5, np.asarray([5.2, 5.7, 5.9, 6.08, 6.2], dtype='float64'))
ntc.setnodetitle(nodeBC2,'Max. significant wave height (m)')

nodeR1 = ntc.newnode('Location_Houses', 4, net_p)
ntc.setnodetitle(nodeR1,'Houses - Location')
ntc.setnodestatenames(nodeR1, "Area1, Area2, Area3, Area4")
ntc.setnodestatetitle(nodeR1, 0, 'Area 1 (has 283 houses)')
ntc.setnodestatetitle(nodeR1, 1, 'Area 2 (has 759 houses)')
ntc.setnodestatetitle(nodeR1, 2, 'Area 3 (has 383 houses)')
ntc.setnodestatetitle(nodeR1, 3, 'Area 4 (has 273 houses)')

nodeH1_R1 = ntc.newnode('MaxInundation_Houses', 0, net_p)
ntc.setnodelevels(nodeH1_R1, 4, np.asarray([0, 0, 0.5, 1, 2], dtype='float64'))
ntc.setnodetitle(nodeH1_R1,'Houses - Max. Inundation depth (m)')

nodeC1_R1 = ntc.newnode('RelativeDamage_Houses', 0, net_p)
ntc.setnodelevels(nodeC1_R1, 4, np.asarray([0, 0, 23.5, 47, 50], dtype='float64')) 
ntc.setnodetitle(nodeC1_R1,'Houses - Relative Damage (%)') 	
 
# define links
ntc.addlink(parent=nodeBC1, child=nodeH1_R1)
ntc.addlink(parent=nodeBC2, child=nodeH1_R1)
ntc.addlink(parent=nodeR1, child=nodeH1_R1)
ntc.addlink(parent=nodeH1_R1, child=nodeC1_R1) 
 
ntc.setnodeprobs(nodeH1_R1, np.asarray([0, 0, 0], dtype='int'), np.asarray([16.7,44.7,22.6,16.1],dtype='float32'))	

 
# obtain node list
#nl_p = ntc.getnetnodes(net_p)
# train with cas file
# ntc.revisecptsbycasefile(filename='BNcases.cas', nl_p=nl_p, updating=0, degree=1)
 

 
# compile the net
ntc.compilenet(net_p)

ntc.getnodeprobs(nodeH1_R1, np.zeros(20, dtype='int')) #np.asarray([0, 0, 0], dtype='int'))	
# enable auto updating
ntc.setautoupdate(net_p)
 
# save net
ntc.savenet(env, net_p, 'BNZeebrugge.dne')