# -*- coding: utf-8 -*-
"""

$Id: __init__.py 9202 2013-09-09 13:19:34Z heijer $
$Date: 2013-09-09 15:19:34 +0200 (Mon, 09 Sep 2013) $
$Author: heijer $
$Revision: 9202 $
$HeadURL: https://svn.oss.deltares.nl/repos/openearthtools/trunk/python/applications/Netica/netica/test/__init__.py $

"""
import unittest

class UnitTests(unittest.TestCase):
    def setUp(self):
        from netica import Netica
        self.netica = Netica()
        self.netfilename = 'curvnet.dne'
        self.env = self.netica.newenv()
        self.netica.initenv(self.env)
        self.net = self.netica.opennet(self.env, self.netfilename)
        self.nl_p = self.netica.getnetnodes(self.net)
        self.netica.compilenet(self.net)
    def test_enternodelikelyhood(self):
        self.netica.retractnetfindings(self.net)
        node_p = self.netica.getnodenamed('radius', self.net)
        self.netica.enternodelikelyhood(node_p, [1,0,0,0,0,0])
#        self.netica.savenet(env, net, 'test.dne')
    def test_equationtotable(self):
        node_p = self.netica.getnodenamed('radius', self.net)
        self.netica.equationtotable(node_p, 10, True, True)
    def test_revisecptsbycasefile(self):
        casefilename = 'wavedir.cas'
        file_p = self.netica._newstream(self.env, casefilename)
        self.netica.revisecptsbycasefile(file_p, self.nl_p, 0, 1)
    def test_getnodeequation(self):
        node_p = self.netica.getnodenamed('phi', self.net)
        eqn = self.netica.getnodeequation(node_p)
        print eqn
        # the radius node has no equation, thus should result in an empty string
        node_p = self.netica.getnodenamed('radius', self.net)
        eqn = self.netica.getnodeequation(node_p)
        self.assertEqual(eqn, '')
    def test_setnodeequation(self):
        node_p = self.netica.getnodenamed('phi', self.net)
        eqn_in = 'phi (theta, wavedir) = theta - wavedir'
        self.netica.setnodeequation(node_p, eqn_in)
        eqn_out = self.netica.getnodeequation(node_p)
        self.assertEqual(eqn_in, eqn_out)
    def test_newnode(self):
        nodename = 'test'
        node_p = self.netica.newnode(nodename, 3, self.net)
        self.assertEqual(self.netica.getnodename(node_p), nodename)
    def test_deletenode(self):
        nodename = 'test'
        node_p = self.netica.newnode(nodename, 3, self.net)
        self.netica.deletenode(node_p)
    def test_addlink(self):
        parent = self.netica.getnodenamed('wavedir', self.net)
        child = self.netica.getnodenamed('erosionfactor', self.net)
        link_index = self.netica.addlink(parent, child)
        print 'index',link_index
    def test_deletelink(self):
        child = self.netica.getnodenamed('erosionfactor', self.net)
        link_index = 1
        self.netica.deletelink(link_index, child)
    def test_getnodelevels_continuous(self):
        node_p = self.netica.getnodenamed('phi', self.net)
        print self.netica.getnodelevels(node_p)
    def test_getnodelevels_discrete(self):
        node_p = self.netica.newnode('Time_horizon', 3, self.net)
        #self.netica.setnodestatenames(node_p, "one, five, ten")
        self.netica.getnodelevels(node_p)
    def test_getnodestatename(self):
        node_p = self.netica.newnode('Time_horizon', 3, self.net)
        self.netica.setnodestatenames(node_p, "one, five, ten")
        print 'STATE: "' + self.netica.getnodestatename(node_p, 0) + '"'
    def test_enterfinding(self):
        node_p = self.netica.getnodenamed('phi', self.net)
        self.netica.enterfinding(node_p, 0)
    def test_getnodeexpectedvalue(self):
        node_p = self.netica.getnodenamed('phi', self.net)
        expval = self.netica.getnodeexpectedvalue(node_p)
        print 'expval = ',expval
        
class IntegrationTests(unittest.TestCase):
    def test_opennet(self):
        from netica import Netica
        netica = Netica()
        netfilename = 'curvnet.dne'
        env = netica.newenv()
        netica.initenv(env)
        net = netica.opennet(env, netfilename)
        # this is another test...
        netica.compilenet(net)
        nl_p = netica.getnetnodes(net)
        print nl_p
        nnodes = netica.lengthnodelist(nl_p)
        print nnodes
        for index in range(nnodes):
            node_p = netica.nthnode(nl_p, index)
            print netica.getnodename(node_p)
            print netica.getnodebeliefs(node_p)
            print netica.getnodetype(node_p)
        self.assertTrue(netica)

if __name__ == '__main__':
    unittest.main()