import mysql.connector as sql

db=sql.connect(host='localhost',
               user='root',
               password='1234',
               auth_plugin='mysql_native_password'
               )
cur=db.cursor()

cur.execute("use Student_Society")

print("Q11: Display the following information: Society name Mentor name Total Capacity Total Enrolled Unfilled Seats . \n")

Q1='select soc_name, mentor_name, total_seats, count(s_id), total_seats-count(s_id) \
from society \
left join enrollment on socid=s_id \
group by s_id,total_seats; '

cur.execute(Q1)

result=cur.fetchall()
for i in range(len(result)):   
    print(result[i][0],'\n')
      
