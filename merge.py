#merge
from glob import glob

filename = 'merge.csv'

with open(filename, 'a') as singleFile:
    first_csv = True
    for csv in glob('*.csv'):
        if csv == filename:
            pass
        else:
            header = True
            for line in open(csv, 'r'):
                if first_csv and header:
                    singleFile.write(line)
                    first_csv = False
                    header = False
                elif header:
                    header = False
                else:
                    singleFile.write(line)
    singleFile.close()

