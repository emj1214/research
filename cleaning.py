# function to clean nasdaq .txt files
import pandas as pd
import re
import sys

def clean(file): # "file" is the nasdaq .txt file name as a string
    # output file name for the save in the final step, adds "-cleaned" to the original file name
    filename = re.sub(r'\.txt$', '-cleaned.txt', file) 

    # read in the text file
    df = pd.read_csv(file, sep="|")

    # remove any empty columns at the end named 'Filler' or 'Filler2' of 'Filler3' and so on
    df = df.drop(list(df.filter(regex='Filler')), axis=1).sort_values("Symbol", ascending=True)
    # sort moves the date row to the front so tables can vary in length without causing issues

    # remove duplicate index created by the above import and sort
    df = df.reset_index()
    df = df.drop("index", axis=1)

    # move date from value into column
    ## first, create + format Date column
    ### originally included dashes to separate year-month-day r'\1-\2-\3', hence the use of re.sub
    df["Date"] = re.sub(r'^(\d{4})(\d{2})(\d{2})(\d*)$', r'\1\2\3',df["Symbol"][0]) 
    ## then drop first row which currently holds the date
    df = df.drop(0, axis=0)

    # save table to new text file 
    df.to_csv(f"{filename}", sep="|", index=False)

# allow function to be called from terminal
if __name__ == '__main__':
    # Map command line arguments to function arguments.
    clean(*sys.argv[1:])