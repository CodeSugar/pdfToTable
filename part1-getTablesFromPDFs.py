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
tableResults = [["FILE" , "PROPOSITO","CONTENIDO", "PRACTICAS","PRACTICAS_UBICACION"]]
unidadesTematicasResult = [["FILE", "NOMBRE", "UNIDAD_DE_COMPETENCIA","CONTENIDO"]]

for file in files:
    tables = camelot.read_pdf(file, pages='all')
    tablesContenido = []
    PRACTICAS=""
    PRACTICAS_UBICACION=""
    for table in tables:
        tempDF = table.df
        if tempDF.shape[0] >= 2 and tempDF.shape[1] >= 2 and tempDF[1][0] == 'CONTENIDO':
            tablesContenido.append( tempDF )
            unidadesTematicasResult.append( [file, tempDF[0][0], tempDF[0][2], tempDF[1][2] ])

        if tempDF.shape[0] >= 1 and tempDF.shape[1] >= 1 and tempDF[0][0] == 'RELACIÓN DE PRÁCTICAS':
            print(file)
            print(tempDF[0][2])
            print([ x.strip() for x in tempDF[0][2].split("\n")])
            arrayTemp = [ x.strip().replace(".","") for x in tempDF[0][2].split("\n") if x.strip() != ""]
            PRACTICAS = max([ int(x.strip()) for x  in arrayTemp])
            PRACTICAS_UBICACION = tempDF[3][2]


    contentResult = ""
    for table in tablesContenido:
        contentResult = contentResult + table[1][2] + "\n"

    proposito = tables[1].df[0][0]
    tableResults.append([file, proposito,  contentResult, PRACTICAS, PRACTICAS_UBICACION])

export_to_csv(tableResults, csv_filename)
print("CSV file has been created:", csv_filename)
export_to_csv(unidadesTematicasResult, "unidadesTematicasResult.csv")
print("CSV file has been created:", "unidadesTematicasResult.csv")

