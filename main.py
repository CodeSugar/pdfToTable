##  apt update
##  apt install ghostscript python3-tk
##  apt-get install ffmpeg libsm6 libxext6
# pip install camelot-py[cv]
# pip install 'PyPDF2<3.0'
import camelot
import os

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

# Example usage:
directory_path = 'ISC'
files = list_files_in_subdirectory(directory_path)
tableResults = []
test = 0
for file in files:
    tables = camelot.read_pdf(file, pages='all')
    # tables.export('foo.csv', f='csv', compress=True) # json, excel, html, sqlite
    #tables[0]
    #tables[0].parsing_report
    #tables[0].to_csv('foo.csv') # to_json, to_excel, to_html, to_sqlite

    # Consigue las tablas con la columna contenido
    tablesContenido = []
    for table in tables:
        tempDF = table.df
        if tempDF.shape[0] >= 2 and tempDF.shape[1] >= 2 and tempDF[1][0] == 'CONTENIDO':
            tablesContenido.append( tempDF )
    resultadosContenidop = ""
    for table in tablesContenido:
        resultadosContenidop = resultadosContenidop + table[1][2] + "\n"
        #print( table[1][2] )
    tableResults.append([file, resultadosContenidop])



import csv

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

# Example usage:


csv_filename = 'ISC.csv'
export_to_csv(tableResults, csv_filename)
print("CSV file has been created:", csv_filename)

