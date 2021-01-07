# coding: utf-8
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm #字体管理器
import pandas as pd
import csv

if __name__ == '__main__': 
    print('begin')
    dict = {'Below30':0,'30To50':0,'Above50':0}
    df = pd.read_csv(r'pythonTest.csv',encoding='UTF-8')
    total = len(df)
    
    range = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010,2020]
    

    for row in df[['gender','birthday']].iterrows():
        row['birthday'],row['gender']
        print()

    

    
    print('end')

