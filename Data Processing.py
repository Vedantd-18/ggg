import pandas as pd
data={'Name':["Sam","Kia","Jack","Lilly","Riya","Keshav","Rose"],
      'Age':[12,13,14,13,12,13,14],
      'Gender':['M','F','M','F','F','M','F'],
      'Marks':[98,76,'Nan',65,74,'Nan',66]}
df=pd.DataFrame(data)
df
c=avg=0
for ele in df['Marks']:
    if str(ele).isnumeric():
         c+=1
         avg+=ele
avg/=c

