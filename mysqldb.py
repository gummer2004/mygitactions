import mysql.connector
from mysql.connector import errorcode

try:
    conn = mysql.connector.connect(user='root',password='', database='cr2800',host='127.0.0.1')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Password Error")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = conn.cursor()
    query = "Select f_name, l_name from students where f_name = '"
    
    print("Enter First Name")
    myinput = input()
    query = query + myinput +"'"
    # print (query)
    try:
        results = cursor.execute(query,multi=True)
        for result in results:
            if result.with_rows:
                print("Running query:", result)
                print("Rows produced by statement '{}':".format(result.statement))
                print(result.fetchall())
            else:
                print("Running query:", result)
                print("Number '{}': {}".format(result.statement, result.rowcount))
                
    except mysql.connector.Error as e:
        print ("MySql Error %s" % str(e))
    else:
        conn.commit()
        conn.close()