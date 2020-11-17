from zipfile import ZipFile


with ZipFile('archive.zip') as myzip:
    with myzip.open('1.txt', 'r') as file:
        if myzip:
            print(file.read().decode('utf-8'))
        else:
            print('')
    