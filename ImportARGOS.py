##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2021
## Author: shana.shapiro@duke.edu (For ENV859) 
##---------------------------------------------------------------------

#Import modules
import sys, os, arcpy

# Set input variables (Hard-wired)
inputFile = 'V:/ARGOSTracking/data/ARGOSData/1997dg.txt' #Note can also do \\ instead of /
outputFC = "V:/ARGOSTracking/scratch/ARGOStrack.shp"

#%% construct a while loop to iterate through all lines in the datafile
# Open the ARGOS data file for reading 
inputFileObj = open(inputFile, 'r')

#want the script to be able to read large files. Do this with a while loop 
#Get the first line of data so we can use the while loop
lineString = inputFileObj.readline()

#Start the while loop 
while lineString: 
     # Set code to run only if the line contains the string "Date: "
    if ("Date :" in lineString):
        
        # Parse the line into a list
        lineData = lineString.split()
        
        # Extract attributes from the datum header line
        tagID = lineData[0]
        
        # Extract location info from the next line
        line2String = inputFileObj.readline()
        
        # Parse the line into a list
        line2Data = line2String.split()
        
        # Extract the date we need to variables
        obsLat = line2Data[2]
        obsLon= line2Data[5]
        
        # Print results to see how we're doing
        print (tagID,"Lat:"+obsLat,"Long:"+obsLon)
        
    # Move to the next line so the while loop progresses. This is evaluated for every line
    lineString = inputFileObj.readline()
    
#Close the file object
inputFileObj.close()

