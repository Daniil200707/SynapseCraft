import pandas as pd

def open_qualyty():
    d = pd.read_csv('qualyty.csv')
    return d

def open_fermer_csv():
    d = pd.read_csv('../../Резервные копии/python/fermer.csv')
    return d

def open_csv(file):
    d = pd.read_csv(file)
    print(f"file {file} read")
    return d

if __name__ == '__main__':
    print(open_qualyty())
