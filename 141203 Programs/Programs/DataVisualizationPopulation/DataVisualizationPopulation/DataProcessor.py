"""
The DataProcessor class translates numbers into graphical representations.
Alain Chen, CJ Phillips, Brett Woods
Created: Oct 17th, 2014
Last Edited: Nov 13th, 2014

We hereby certify that the program below represents our work 
and the design, content, and logic was completed without outside assistance.
"""

import Data as dt
import Projections as proj

class DataProcessor(object):

    #Constant used to adjust size
    k = 10.0

    #Returns a marker that represents data.
    def getDot( self, state, county, year ):

        projection = proj.getProjections( state, county, year )

        #Size of marker.
        size = projection / k


    #Returns the FIPS code, as an integer, of the county.
    def getFips( self, state, county ):     

        #Get county rows.
        countyName = state.loc( "COUNTY NAME" )
        
        #Get the FIPS code of the county.
        fips = int(countyName[ county, "Unnamed: 3" ])

        #Return projection.
        return fips