import csv

def read_csv_into_memory(filename):
    """
    Reads a CSV file into memory and returns its contents as a list of lists.
    
    Args:
    - filename (str): Name of the CSV file to read.
    
    Returns:
    - data (list of lists): Contents of the CSV file.
    """
    data = []
    with open(filename, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            data.append(row)
    return data

def export_to_csv(data, filename):
    """
    Exports a 2D array into a CSV file.
    
    Args:
    - data (list of lists): 2D array to export.
    - filename (str): Name of the CSV file to create.
    """
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)

dictionaryData = {}

LCDData = read_csv_into_memory('LCD.csv')
IIAData = read_csv_into_memory('IIA.csv')
ISCData = read_csv_into_memory('ISC.csv')

data = [ [ "LCD" , LCDData], [ "IIA" , IIAData], [ "ISC" , ISCData]]

for row in LCDData:
    if row[1] not in dictionaryData:
        dictionaryData[row[1]] = []
    dictionaryData[row[1]] .append(row[0])
for row in IIAData:
    if row[1] not in dictionaryData:
        dictionaryData[row[1]] = []
    dictionaryData[row[1]] .append(row[0])
for row in ISCData:
    if row[1] not in dictionaryData:
        dictionaryData[row[1]] = []
    dictionaryData[row[1]] .append(row[0])

for key in dictionaryData:
    if len(dictionaryData[key]) > 1:
        print(dictionaryData[key])


def levenshtein_distance(str1, str2):
    """
    Calculates the Levenshtein distance between two strings.
    
    Args:
    - str1 (str): First string.
    - str2 (str): Second string.
    
    Returns:
    - distance (int): Levenshtein distance between the two strings.
    """
    len_str1 = len(str1)
    len_str2 = len(str2)
    
    # Create a matrix to store the distances
    matrix = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]
    
    # Initialize the matrix
    for i in range(len_str1 + 1):
        matrix[i][0] = i
    for j in range(len_str2 + 1):
        matrix[0][j] = j
        
    # Fill the matrix
    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            if str1[i - 1] == str2[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            matrix[i][j] = min(matrix[i - 1][j] + 1,     # Deletion
                               matrix[i][j - 1] + 1,     # Insertion
                               matrix[i - 1][j - 1] + substitution_cost)   # Substitution
            
    # Return the Levenshtein distance (the bottom-right element of the matrix)
    return matrix[len_str1][len_str2]

# Example usage:
str1 = "kitten"
str2 = "sitting"
distance = levenshtein_distance(str1, str2)
print("Levenshtein distance between '{}' and '{}': {}".format(str1, str2, distance))

resultTotal = []
for rowData in data:
    current = rowData[0] #EX. ISC
    for row in rowData[1]:

        rowResult = [row[0]]

        for rowData2 in data:
            if rowData2[0] == rowData[0]:
                continue

            maxComparision = 99999999
            file = ""
            for row2 in rowData2[1]:
                currentDistance = levenshtein_distance(row[0],row2[0]) 
                if currentDistance < maxComparision:
                    maxComparision = currentDistance
                    file = row2[0]

            rowResult.append(file)
            rowResult.append(maxComparision)

        resultTotal.append(rowResult)

export_to_csv(resultTotal, "analyze.csv")