import sqlite3
connection = sqlite3.connect("Films.db")
cursor = connection.cursor()
sql_command=""" CREATE TABLE Movies(Movie_name VARCHAR(20),
Actor_name VARCHAR(20),
Actress_name VARCHAR(20),
Director_name VARCHAR(20),
Year_of_release INTEGER);"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Movies(Movie_name,Actor_name,Actress_name,Director_name,Year_of_release)VALUES("Alaipayuthey","Madhavan","Shalini","Mani Ratnam",2000);"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Movies(Movie_name,Actor_name,Actress_name,Director_name,Year_of_release)VALUES("Mouna Ragam","Mohan","Revathi","Mani Ratnam",1986);"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Movies(Movie_name,Actor_name,Actress_name,Director_name,Year_of_release)VALUES("Master","Vijay","Malavika Mohanan","Lokesh Kanagaraj",2021);"""
cursor.execute(sql_command)
connection.commit()
cursor.execute("SELECT * FROM Movies")
print("fetchall:")
result=cursor.fetchall()
for r in result:
    print(r)