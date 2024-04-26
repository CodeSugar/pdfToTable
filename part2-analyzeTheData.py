# pip install levenshtein

import csv
from Levenshtein import distance
from utilsFunctions import export_to_csv
from utilsFunctions import read_csv_into_memory

dictionaryData = {}

LCDData = read_csv_into_memory('LCD.csv')
IIAData = read_csv_into_memory('IIA.csv')
ISCData = read_csv_into_memory('ISC.csv')

data = [ [ "LCD" , LCDData], [ "IIA" , IIAData], [ "ISC" , ISCData]]
resultTotal = []
for rowData in data:
    current = rowData[0] #EX. ISC
    for row in rowData[1]:

        rowResult = [row[0]]

        for rowData2 in data:
            if rowData2[0] == rowData[0]:
                continue

            maxComparision = 99999999
            maxComparissionPercentage = 100
            file = ""
            for row2 in rowData2[1]:
                currentDistance = distance(row[1],row2[1]) 
                if currentDistance < maxComparision:
                    maxComparision = currentDistance
                    file = row2[0]
                    bigger = max(len(row[1]), len(row2[1]))
                    maxComparissionPercentage = (bigger - currentDistance) / bigger

            rowResult.append(rowData2[0]) 
            rowResult.append(file)
            rowResult.append(maxComparision)
            rowResult.append(maxComparissionPercentage)

        resultTotal.append(rowResult)

export_to_csv(resultTotal, "analyze.csv")