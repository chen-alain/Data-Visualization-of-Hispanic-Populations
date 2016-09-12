"""
The Data class stores the data that is loaded from US Census files.
This class only contains the data and does not have any methods
that analyze the data.
Alain Chen, CJ Phillips, Brett Woods
Created: Oct 15th, 2014
Last Edited: Dec 3rd, 2014

We hereby certify that the program below represents our work 
and the design, content, and logic was completed without outside assistance.
"""

import pandas as pd
import csv

class Data(object):
    
    #List that stores the file names for population data.
    stateName = []

    #Structure that would store data frames of state data.
    stateData = []

    #List that stores the file names for codes for ZIP and FIPS.
    zipName = []

    #Structure that stores the information to convert ZIP to FIPS.
    zipFrame = []
	
	zipData

    #Initialize.
    def __init__(self):
        self.stateName = [ 'Data/Kansas.csv', 'Data/Missouri.csv' ]
        self.zipName = [ 'ZIP/KansasZIP.csv', 'ZIP/MissouriZIP.csv' ]
        self.putInDataFrame()

    #Put the data inside the 50 state files into 50 different data frames.
    def putInDataFrame(self):
        for state in self.stateName:
            self.stateData.append( pd.DataFrame.from_csv(state) )
        for state in self.zipName:
            self.zipFrame.append( pd.DataFrame.from_csv(state) )
			
		self.zipData = zipFrame.loc("zcta5")

    #Get FIPS from the given ZIP code. ZIP is an int.
    def getFIPS( self, zip ):

        #Change from nine digit zip to five digit if necessary.
        zipCorrected = zip
        if zipCorrected > 99999:
            zipCorrected = int( zipCorrected / 10000 )

        #The ZIP is in Kansas.
        for i in range( 0, len( self.zipFrame[0] ) ):
            if self.zipFrame[0].index[i] == zipCorrected:
                return self.zipData[0][ self.zipFrame[0].index[i], "county" ]

        #The ZIP is in Missouri.
        for i in range( 0, len( self.zipFrame[1] ) ):
            if self.zipFrame[1].index[i] == zipCorrected:
                return self.zipData[1][ self.zipFrame[0].index[i], "county" ]

        #Return error if ZIP is not valid.
        return -1