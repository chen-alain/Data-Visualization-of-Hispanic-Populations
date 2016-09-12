"""
This class gets the projections of Hispanic population.

Alain Chen, CJ Phillips, Brett Woods
Created: Oct 27th, 2014
Last Edited: Nov 13th, 2014

We hereby certify that the program below represents our work 
and the design, content, and logic was completed without outside assistance.
"""

import pandas as pd

class Projections(object):
    
    #Returns a list of projections of the given state, county and year. 
    #State is a dataframe.
    def getProjections( self, state, county, year ):     

        #Get county rows.
        countyName = state.loc( "COUNTY NAME" )
        
        #Get the change in Hispanic Data from 2000 to 2010. Get rid of commas.
        increase = str( countyName[ county, "Hispanic Change" ] ).replace( ',', '' )

        #Get 2010 data. Get rid of commas.
        proj = int( str( countyName[ county, "10Hispanic" ] ).replace( ',', '' ) )
        
        #Add the change to the 2010 as many times as needed 
        #until the desired year is hit.
        for i in range( 2010, year, 10 ):
            """
            Only increase if there is data present. 
            If the data piece that indicates change in hispanic population is
            missing, treat the data as if the increase is 0.
            """
            if not increase == 'nan':
                proj += int(increase)
            
        #If there is a projected negative population set 
        #Hispanic population to zero.     
        if proj < 0 :
            proj = 0

        #Return projection.
        return proj
