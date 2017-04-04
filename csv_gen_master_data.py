import csv
import random
from faker import Faker

l=Faker('en_GB')
f=open("D:\ML\Hackathon\\tst.csv", "r")
k=csv.reader(f)

g=open("D:\ML\Hackathon\\Mast_data_set.csv", "w")
#g.truncate()
w=csv.writer(g)
w.writerow(('CUST_ID', 'CUST_NAME', 'SAL'))
for i in range(101):
	if i >0 and i <= 30:
		w.writerow((i, l.name(), random.randrange(0, 500000, 10000)))
	elif i > 30 and i <= 70:
		w.writerow((i, l.name(), random.randrange(500001, 1000000, 20000)))
	elif i >= 71:
		w.writerow((i, l.name(), random.randrange(1000001, 100000000, 1000000)))
			
f.close()
