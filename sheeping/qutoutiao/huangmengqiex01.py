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
    for age in df['age']:
        if age <30:
            dict['Below30'] += 1
        elif age>=30 and age<50:
            dict['30To50'] +=1
        elif age>=50:
            dict['Above50']+=1
    
    colors = ['red','pink','orange']
    plt.axes(aspect='equal')
    plt.xlim(0,8)
    plt.ylim(0,8)
    
    plt.gca().spines['right'].set_color('none')    
    plt.gca().spines['top'].set_color('none')
    plt.gca().spines['left'].set_color('none')
    plt.gca().spines['bottom'].set_color('none')    
    
    
    explode =[0,0,0]
    
    max_number = max(dict.values())
    iter = 0
    list_values = [i for i in dict.values()]

    for item in list_values:
        if item == max_number:
            explode[iter] = 0.3
        iter+=1
    
    plt.pie(x=dict.values(), 
        labels=dict.keys(),        
        explode=explode,        
        colors=colors,                 
        pctdistance=0.8,        
        labeldistance=1.0,        
        startangle=180,        
        center=(4,4),        
        radius=3.8,        
        counterclock=False, 
        wedgeprops= {'linewidth':1,'edgecolor':'green'},
        frame=1) 
    plt.xticks(())
    plt.yticks(())
    plt.title('Age Calculation')
    plt.show()
    
    print('end')

