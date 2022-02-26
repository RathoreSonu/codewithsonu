import smtplib
from datetime import datetime,timedelta
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pymysql
import pandas as pd

path="/home/sonu.rathore/"
dat = str(datetime.today()).split()[0]
dat_2 = str(datetime.today()-timedelta(5)).split()[0]


host = "127.0.0.1"
port = 3306
db_name = "sonu.hello"
user = "root"
password= "Ss@@123"



#class for run query
def getDatafromQuery(query):
    connection = pymysql.connect(host=host, user=user, password=password, db=db_name, charset='utf8mb4', port=port)
    cursor=connection.cursor()
  
    
    dataframe = pd.read_sql(query, connection)
    connection.close()
    return dataframe

#call the function
df_scraper_table = getDatafromQuery("select customer,  platform,inserted_date , count(id) from v3_backend_basicecomm_data_table vbbdt where  inserted_date BETWEEN '"+str(dat_2)+"' and '"+str(dat)+"' group by 1,2,3; ")

#pivot Table
pivot1=pd.pivot_table(df_scraper_table, values='count(id)', index=['customer','platform'], columns='inserted_date', aggfunc='sum', fill_value=0,margins=True, margins_name='grand_total', observed=True)




#Final_DF = pd.DataFrame()
#Final_DF = pivot1



# print(Final_DF)
# print()

#Final_DF.to_csv(path+'table_counts.csv', index='False')

pivot1.to_csv(path+'Count_check.csv')


#attach the database in body
html="""\
<html>
   <head>
<b> Count Pivot</b></head>
   <body>
       {0}
    </body>
</html>
""".format(pivot1.to_html())


#print(message)


host = "email-smtp.us-west-2.amazonaws.com"
port = 587
username = "@@@@@@"
password = "@@@@@@@@@"
from_email = "<report@mfilterit.com>"


to = ["first outlook id","second outlook id"]

OFA_PATH = path


# create message object instance
msg = MIMEMultipart()


msg['From'] = "<please mention outlook id which you want you send mail>"

msg['To'] = ",".join(to)#it is use mail ids after send mail
msg['Subject'] = "Ecom_daily_cout_map"

# add in the message body
part1=MIMEText(html,'html')
msg.attach(part1)


# attach file to mail

rating_review_table = MIMEBase('application', "octet-stream")
rating_review_table.set_payload(open(path + "Count_check.csv", "rb").read())
encoders.encode_base64(rating_review_table)
rating_review_table.add_header('Content-Disposition', 'attachment', filename='table_counts.csv')
msg.attach(rating_review_table)



# create server
server = smtplib.SMTP(host, port)

server.starttls()

# Login Credentials for sending the mail
server.login(username, password)

# send the message via the server.
server.sendmail(msg['From'], to, msg.as_string())

server.quit()

print("successfully sent email to %s:" % (msg['To']))
