import camelot

tables = camelot.read_pdf('file.pdf', pages='1', flavor='lattice')
print(tables)

tables.export('file.csv', f='csv', compress=False)
tables[0].to_csv('file.csv')  # to a csv file
print(tables[0].df)  # to a df