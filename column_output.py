import datetime

def columnOutput(dbData,cols,formatStr):
# dbData is a list of tuples
# cols is a dictionary with column name as the key and data type as the item
# formatStr uses the following format, with one set of curly braces {} for each column.
# For each column "{: <10}" determines the width of the column, padded with spaces (10 spaces in this example)
#   <, ^ and > determine the alignment of the text: < (left aligned), ^ (centre aligned), > (right aligned)
#   The following example is for 3 columns of output: left-aligned, 5 characters wide; centred, 10 characters; right-aligned 15 characters:
#       formatStr = "{: <5}  {: ^10}  {: >15}"
# Make sure the column is wider than the heading text and the widest entry in that column, otherwise the columns won't align correctly.
# You can also pad with something other than a space and put characters between the columns, 
# e.g. this pads with full stops '.' and separates the columns with the pipe character | :
#       formatStr = "{:.<5} | {:.^10} | {:.>15}"
    print(formatStr.format(*cols))
    for row in dbData:
        rowList = list(row)
        for index, item in enumerate(rowList):
            if item == None:      # Removes any None values from the rowList, which would cause the print(*rowList) to fail
                rowList[index] = ""       # Replaces them with an empty string
            elif type(item) == datetime.date:    # If item is a date, convert to a string to avoid formatting issues
                rowList[index] = str(item)
        print(formatStr.format(*rowList))   