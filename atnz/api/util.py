import csv

def writeCSV(fileout, datain):
    """
    Write a UTF-8 properly encoded csv from a dict object
    :param fileout: the name of the file to output
    :param datain: the input dict
    :return:
    """
    with open(fileout, 'wb') as mf:
        wr = csv.writer(mf, quoting=csv.QUOTE_ALL)
        wr.writerow([x.encode('UTF-8') for x in datain[0].keys()])
        for row in datain:
            wr.writerow([x.encode('utf8') if type(x) is unicode else x for x in row.values()])