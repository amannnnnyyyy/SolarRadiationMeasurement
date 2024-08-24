import pandas as pd

benin = '../data/benin-malanville.csv'
sierra = '../data/sierraleone-bumbuna.csv'
togo = '../data/togo-dapaong_qc.csv'
def readData(city):
    if city == 'benin':
        return pd.read_csv(benin)
    elif city == 'sierra':
        return pd.read_csv(sierra)
    elif city == 'togo':
        return pd.read_csv(togo)
    else:
        raise ValueError("City not found")
