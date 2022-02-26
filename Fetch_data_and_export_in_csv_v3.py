import pymysql
import traceback
import pandas as pd 
import numpy as np

# Mysql Credentials
host = "127.0.0.1"
port = 3306
db_name = "ecomm_v3_db"
user = "shwetap"
password= "N8bC[4by"

X=input("please enter your file name without file format:-")
# Where Sql Data will Save in CSV
path = '/home/sonu.rathore/FETCH_DATA/'
csv_filname = X+'.csv.gz'

# Read Data From DB
def getDatafromQuery(query):
    connection = pymysql.connect(host=host, user=user, password=password, db=db_name, charset='utf8mb4', port=port, cursorclass=pymysql.cursors.DictCursor)
    dataframe = pd.read_sql(query, connection)
    connection.close()
    return dataframe


sql = input("please enter SQL quary:-")



print(sql)

df = getDatafromQuery(sql)
print("No of Records : " + str(len(df)))

df.to_csv(path + csv_filname, index=False, header=True, compression='gzip')
#df.to_excel(path + csv_filname, index=False, header=True)
#Na=df.to_numpy()
#np.savetxt("SOS_01-30_May.txt",Na)
print("Data Extraction Process Done...")
