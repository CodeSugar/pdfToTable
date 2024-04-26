# ESCOM Study Plan PDF Analysis Project

## Overview

This project aims to analyze PDF documents from the ESCOM Study Plan and detect similarities between them.

## Dependencies

To run this project in a Codespace environment, you need to install the following dependencies using the next commands:

```
apt update
apt install ghostscript python3-tk
apt install ffmpeg libsm6 libxext6
pip install camelot-py[cv]
pip install 'PyPDF2<3.0'
pip install levenshtein
```

In our workflow, we use the Camelot library to extract structured data from PDF documents. Additionally, we employ the Levenshtein algorithm to calculate the textual distance between content segments, for the detection of similarities within the analyzed documents.