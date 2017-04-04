import pandas as pd
import numpy as np
import datetime as dt
import time as t
from time import gmtime, strftime
import random as rd
import itertools

df_txn = pd.read_csv("D:/ML/Hackathon/txn_data.csv")

df_mstr = pd.read_csv("D:/ML/Hackathon/Mast_data_set.csv")


df_txn = pd.read_csv("D:/ML/Hackathon/txn_data.csv")

TXN_PERIOD = []

for index, row in df_txn.iterrows():
    row['TXN_PERIOD']= row['TXN_DATE'][0:7]
    TXN_PERIOD.append(row['TXN_PERIOD'])

df_txn['TXN_DATE'] = TXN_PERIOD

#table = pd.pivot_table(df_txn, values = 'TXN_AMOUNT', index= ['CUST_ID', 'TXN_TYPE'], columns = 'TXN_PERIOD', aggfunc = 'count', fill_value = 0)

df_txn.to_csv("D:/ML/Hackathon/txn_data_mod.csv",mode='w', index=False)

df_grp = pd.read_csv("D:/ML/Hackathon/txn_data_mod.csv")

df_grp_cnt = df_grp.groupby(['CUST_ID','TXN_TYPE', 'TXN_DATE']).count()
df_grp_cnt.to_csv("D:/ML/Hackathon/grp_cnt_data.csv",mode='w')


df_grp_sum = df_grp.groupby(['CUST_ID','TXN_TYPE', 'TXN_DATE']).sum()
df_grp_sum.to_csv("D:/ML/Hackathon/grp_sum_data.csv",mode='w')

first = pd.read_csv('D:/ML/Hackathon/grp_cnt_data.csv')
second = pd.read_csv('D:/ML/Hackathon/grp_sum_data.csv')


first['SUM_AMT'] = second['TXN_AMOUNT']

first.to_csv("D:/ML/Hackathon/grp_sum_data_new.csv",mode='w', index=None)

pd_data = pd.read_csv('D:/ML/Hackathon/grp_sum_data_new.csv')
pd_credit_data = pd_data[pd_data.TXN_TYPE == "CREDIT"]

pd_credit_data.to_csv("D:/ML/Hackathon/credit_data_new.csv",mode='w', index=None)

df_1 = pd.read_csv('D:/ML/Hackathon/credit_data_new.csv')
df_mstr = pd.read_csv("D:/ML/Hackathon/Mast_data_set.csv")

df_merged_data = pd.merge(df_mstr, df_1, on='CUST_ID')

df_merged_data = df_merged_data.rename(columns = {'TXN_AMOUNT':'TXN_CREDIT_CNT'})




FRAUD_FLAG = []

for index, row in df_merged_data.iterrows():
    if row['SUM_AMT'] > 2* row['SAL']:
        FRAUD_FLAG.append("1")
    else:
        FRAUD_FLAG.append("0")

df_merged_data['FRAUD_FLAG'] = FRAUD_FLAG

df_merged_data.to_csv("D:/ML/Hackathon/final/credit_flag_data.csv",mode='w', index=None)

TXN_PERIOD = []

for index, row in df_merged_data.iterrows():
    row['TXN_PERIOD']= row['TXN_DATE'][0:4]+row['TXN_DATE'][5:7]+str(rd.randrange(1, 28)).zfill(2)
    TXN_PERIOD.append(row['TXN_PERIOD'])


df_merged_data['TXN_DATE'] = TXN_PERIOD
    
hdr = ["CUST_ID", "SAL", "TXN_TYPE", "TXN_DATE", "TXN_CREDIT_CNT", "SUM_AMT", "FRAUD_FLAG"]

df_merged_data.to_csv("D:/ML/Hackathon/final/credit_flag_data.csv",mode='w', index=None, columns = hdr)

pd_data = pd.read_csv("D:/ML/Hackathon/final/credit_flag_data.csv")

pd_data['TXN_TYPE'] = pd_data['TXN_TYPE'].map({'CREDIT':1, 'DEBIT':-1})

pd_data.to_csv("D:/ML/Hackathon/final/bank_trans.csv",mode='w', index=None)
