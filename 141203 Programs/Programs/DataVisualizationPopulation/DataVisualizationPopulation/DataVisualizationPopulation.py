"""
This program visualizes and predicts Hispanic populations 
from the 2010 US Census.

Alain Chen, CJ Phillips, Brett Woods
Created: Oct 15th, 2014
Last Edited: Nov 13th, 2014

We hereby certify that the program below represents our work 
and the design, content, and logic was completed without outside assistance.
"""

import Data as dt
import DataProcessor as dtp
import Projections as proj
import Agency as ag
import pandas as pd

data = dt.Data()

pro = proj.Projections()

agencies = ag.Agency()

dataP = dtp.DataProcessor()


print data.getFIPS( 63014 )

"""
#Iterate over the states.
for state in range( 0, 2 ):
    print "#####################" + str(state)
    for i in range( 2, len(data.stateData[state]) ):
        print data.stateData[state].index[i]
        """

"""
        print str(dataP.getFips( data.stateData[state], \
            data.stateData[state].index[i] )) + ': ' \
            + str(pro.getProjections( data.stateData[state], \
            data.stateData[state].index[i], 2010 ))
            """

"""
#Get specific info from the nth agency on the list.
for agency in range( 0, len(agencies.agencyData) ):
    print agencies.getBrName( agency )
"""
