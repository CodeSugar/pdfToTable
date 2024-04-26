import os
import csv

def list_files_in_subdirectory(directory):
    """
    Returns a list of all files in the specified subdirectory.
    
    Args:
    - directory (str): Path to the subdirectory.
    
    Returns:
    - file_list (list): List of file names in the subdirectory.
    """
    file_list = []
    # Iterate through all files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

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


# Replaced by "from Levenshtein import distance"
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