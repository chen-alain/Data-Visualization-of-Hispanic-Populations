"""
This class deals with agencies which MeM works with.

Alain Chen, CJ Phillips, Brett Woods
Created: Oct 27th, 2014
Last Edited: Nov 13th, 2014

We hereby certify that the program below represents our work 
and the design, content, and logic was completed without outside assistance.
"""

import pandas as pd
import csv

class Agency(object):
    
    agencyData = pd.DataFrame.from_csv( "Agencies.csv" ) 
    agencyName = agencyData.loc( "BRANCH_NAME" )

    #Return agency number.
    def getAgNo( self, index ):
        return self.agencyName[ self.agencyData.index[index], "AGENCY_NO" ]

    #Return branch number.
    def getBrNo( self, index ):
        return self.agencyName[ self.agencyData.index[index], "BRANCH_NO" ]

    #Return branch name.
    def getBrName( self, index ):
        return self.agencyData.index[index]

    #Return business address #1.
    def getAddress1( self, index ):
        return self.agencyName[ self.agencyData.index[index], "BUSINESS_ADDRESS1" ]

    #Return business address #2. Some may be empty.
    def getAddress2( self, index ):
        return self.agencyName[ self.agencyData.index[index], "BUSINESS_ADDRESS2" ]

    #Return the city where the agency is located.
    def getCity( self, index ):
        return self.agencyName[ self.agencyData.index[index], "BUSINESS_CITY" ]

    #Return the state where the agency is located.
    def getState( self, index ):
        return self.agencyName[ self.agencyData.index[index], "BUSINESS_STATE" ]

    #Return the zip code of the state. Some are 5 digit, some six.
    def getZip( self, index ):
        return self.agencyName[ self.agencyData.index[index], "BUSINESS_ZIP" ]
