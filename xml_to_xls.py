import xml.etree.ElementTree as ET
from openpyxl import Workbook
import os


def read_file(fname):
    """
        Checks if file exists, parses the file and extracts the needed data
        returns a 2 dimensional list without "header"
    """
    if not os.path.exists(fname):
        return
    tree = ET.parse(fname)
    root = tree.getroot()

    # all keys to be extracted from xml
    dict_keys = ["country", "rank", "year", "neighbor"]      
    temp = []
    for key in dict_keys:
        temp.append(root.find(key).text)
    return temp


def to_xls(mdlist):
    """
        Generates excel file with given data
        mdlist: 2 Dimenusional list containing data
    """
    
    wb = Workbook()
    ws = wb.active
    for i, row in enumerate(mdlist):
        for j, value in enumerate(row):
            ws.cell(row=i + 1, column=j + 1).value = value
    newfilename = os.path.abspath("./xml_to_excel.xlsx")
    wb.save(newfilename)
    print("complete")
    return


path = 'xml/'  # path to directory with xml files
result = list()
# iterate in directory to read data from xml files
for filename in os.listdir(path):
    if not filename.endswith('.xml'):
        continue
    fullname = os.path.join(path, filename)
    result.append(read_file(fullname))

if result:
    to_xls(result)
