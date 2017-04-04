import pandas as pd
import numpy as np
import datetime as dt
import random as rd

df=pd.DataFrame()
year=['2016','2017']
months=['01','02','03','04','05','06','07','08','09','10','11','12']
credit_txn_list=[]
debit_txn_list=[]

def creditdebit(cust_id,yr,mn):
    credits=np.random.randint(9)
    debits=np.random.randint(9)
    i=0
    while i < credits:
        my_credit_txn=[]
        txn_date =  yr+'-'+mn+'-'+str(rd.randrange(1, 28)).zfill(2)
        txn_amount = rd.randrange(1000, 200000)
        my_credit_txn=[cust_id + 1,txn_date,txn_amount,'CREDIT']
        i=i+1
        if len(my_credit_txn) > 0:
            credit_txn_list.append(my_credit_txn)

    j=0    
    while j < debits:
        my_debit_txn=[]
        txn_date =  yr+'-'+mn+'-'+str(rd.randrange(1, 28)).zfill(2)
        txn_amount = rd.randrange(1000, 200000)
        my_debit_txn=[cust_id + 1,txn_date,txn_amount,'DEBIT']
        j=j+1
        if len(my_debit_txn) > 0:
            debit_txn_list.append(my_debit_txn)

for cust_id in range(100):
    for yr in year:
        if yr == '2016':
            for mn in months:
                creditdebit(cust_id,yr,mn)
                        
        elif yr == '2017':
            for mn in months[0:3]:
                creditdebit(cust_id,yr,mn)

whole_list = credit_txn_list + debit_txn_list
df = df.append(pd.DataFrame(whole_list, columns=['CUST_ID','TXN_DATE','TXN_AMOUNT','TXN_TYPE']),ignore_index=True)    

df.head()

df.to_csv("D:/ML/Hackathon/txn_data.csv",mode='w', index=False)
