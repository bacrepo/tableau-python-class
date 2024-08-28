import pandas as pd
import pantab

df = pd.read_csv('SuperStoreSimple.csv')
pantab.frame_to_hyper(df, 'SuperStoreSimple.hyper', table='Extract')

