import mysql.connector,getpass,sys
from mysql.connector import Error

def DataTable(Bot_Id,SiteName,Report_Type,Total_Time,Technology,state,test):

    connection = mysql.connector.connect( host="146.250.147.22",
                                          user="OptSavingsUser",
                                          passwd="Ericsson3yA9",
                                          database="OptSavingsDB")

    print("Connected")
    
    cursor = connection.cursor()
    
    sql = """INSERT INTO bot_report_eniq_nic(bot_parameter_id,report_type,total_execution_str,state,test,user_id,site_name,technology) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

    val = (Bot_Id,Report_Type,Total_Time,state,test,getpass.getuser(),SiteName,Technology)
    cursor.execute(sql, val)
    connection.commit()
    cursor.close()
    connection.close()
    print("MySQL connection is closed")

Bot_Id = sys.argv[1]
SiteName = sys.argv[2]
Report_Type = sys.argv[3]
Total_Time = sys.argv[4]
Technology = sys.argv[5]
state = sys.argv[6]
test = sys.argv[7]

DataTable(Bot_Id,SiteName,Report_Type,Total_Time,Technology,state,test)
