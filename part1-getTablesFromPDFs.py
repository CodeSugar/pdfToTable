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
from utilsFunctions import list_files_in_subdirectory
from utilsFunctions import export_to_csv


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

