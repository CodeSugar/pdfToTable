## Steps to run in Codespaces

##  apt update
##  apt install ghostscript python3-tk
##  apt-get install ffmpeg libsm6 libxext6
##  pip install camelot-py[cv]
##  pip install 'PyPDF2<3.0'

# CONFIG section

directory_path = 'ISC'
csv_filename = directory_path + '.csv'

# END CONFIG section

import camelot
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

# Get all the files in the directory_path
files = list_files_in_subdirectory(directory_path)

# Get all the tables with section "CONTENIDO" and extract the information,
#  save it in tableResults
tableResults = [["FILE" , "CONTENIDO"]]
for file in files:
    tables = camelot.read_pdf(file, pages='all')
    tablesContenido = []
    for table in tables:
        tempDF = table.df
        if tempDF.shape[0] >= 2 and tempDF.shape[1] >= 2 and tempDF[1][0] == 'CONTENIDO':
            tablesContenido.append( tempDF )
    contentResult = ""
    for table in tablesContenido:
        contentResult = contentResult + table[1][2] + "\n"
    tableResults.append([file, contentResult])

export_to_csv(tableResults, csv_filename)
print("CSV file has been created:", csv_filename)

