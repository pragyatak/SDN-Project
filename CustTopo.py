#!Author - Pragya Tak
from mininet.topo import Topo

class PTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        #---Creating Hosts
	
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
	h3 = self.addHost( 'h3' )
	h4 = self.addHost( 'h4' )
	h5 = self.addHost( 'h5' )
	h6 = self.addHost( 'h6' )
	h7 = self.addHost( 'h7' )
	h8 = self.addHost( 'h8' )
	h9 = self.addHost( 'h9' )
	h10 = self.addHost( 'h10' )
	h11 = self.addHost( 'h11' )

	#---Creating Switches---
	l_Switch = self.addSwitch( 's1' )
	center1_Switch = self.addSwitch( 's2' )
	center2_Switch = self.addSwitch( 's3' )
 	r_Switch = self.addSwitch( 's4' )

        #---Linking Hosts & Switches--- 
        self.addLink( h1, l_Switch )
	self.addLink( h2, l_Switch )
	self.addLink( h3, l_Switch )
	self.addLink( h4, l_Switch )
	self.addLink( h5, center1_Switch )
        self.addLink( h6, center1_Switch )
	self.addLink( h7, center2_Switch )
	self.addLink( h8, center2_Switch )
	self.addLink( h9, r_Switch )
	self.addLink( h10, r_Switch )
	self.addLink( h11, r_Switch )
	
	#---Linking Switches to each other---
        self.addLink( l_Switch, center1_Switch)
	self.addLink( center1_Switch, center2_Switch)
	self.addLink( center2_Switch, r_Switch )
        

topos = { 'Custtopo': ( lambda: PTopo() ) }

