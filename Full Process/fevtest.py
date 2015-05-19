#!/usr/bin/env python3

# Created by Hiro Christoph 
# May 11 2015
# FEV Internship Test

import csv
import glob
import pandas as df

# Using Glob module to find all .csv files in the current directory
# and puts their names into a list
csvFileList = glob.glob("*.csv")

# Open first file and create csv object
inputfile = open(csvFileList[0], 'rb')
firstInput = csv.reader(inputfile)

# Skip headers
firstInput.next()
firstInput.next()

# Create and write to merged csv object
with open('merge.csv', 'wb') as csvfile:
	csvMerge = csv.writer(csvfile)

	# Grab column titles + data from 1st file
	for row in firstInput:
		csvMerge.writerow(row)

	# Go through every csv file after the first
	for filename in csvFileList[1:]:
		with open(filename, 'rb') as csvfile:
			csvInputFile = csv.reader(csvfile)

			# Skip first 4 lines (headers + column titles)
			# These were already parsed from the 1st csv
			for x in range(0,4):
				csvInputFile.next()

			# Adds onto the end of the merged csv
			for row in csvInputFile:
				csvMerge.writerow(row)

# Read merged csv into pandas dataframe
mergeframe = df.read_csv('merge.csv')

# Sort the columns
mergeframe.sort_index(axis= 1, ascending= True, inplace= True)

# Convert dataframe to csv file 
mergeframe.to_csv('merge.csv', na_rep= '', index= False)

# Close files
inputfile.close()
