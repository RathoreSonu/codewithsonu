#it is made by me for easy my work with good quality

import hashlib as lb
import pandas as pd
ls=[]
#load file 
df=pd.read_excel(r'C:\Users\sonum\OneDrive\Documents\2.Google_Cleaning_Raw_Data\Body_Care_till_18Jan.xlsx')
#check df
# print(df)
# initializing string
  
# encoding using encode()
# then sending to md5()
for i in df['url']:
    r= lb.md5(i.encode())
    p=r.hexdigest()
#append the values of p in list
    ls.append(p)
df['new_hash']=ls
# printing the equivalent hexadecimal value.
print(df['new_hash'])
#store data
df.to_excel(r'C:\Users\sonum\OneDrive\Documents\2.Google_Cleaning_Raw_Data\1.Body_Care_till_18Jan.xlsx', index=False)
  


