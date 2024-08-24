import pandas as pd

benin = pd.read_csv('../data/benin-malanville.csv')
sierra = pd.read_csv('../data/sierraleone-bumbuna.csv')
togo = pd.read_csv('../data/togo-dapaong_qc.csv')
def removeComments(city):
    if city == 'benin':
        return benin.drop(['Comments'],axis=1)
    elif city == 'sierra':
        return sierra.drop(['Comments'],axis=1)
    elif city == 'togo':
        return togo.drop(['Comments'],axis=1)
    else:
        raise ValueError("City not found")