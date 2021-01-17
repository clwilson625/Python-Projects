
#importing sqlite3
import sqlite3

#Creating the dB
conn = sqlite3.connect ('new.db')


#including in the dB
with conn:
      cur = conn.cursor()
      cur.execute("CREATE TABLE  IF NOT EXISTS  tbl_name (  \
           ID INTEGER PRIMARY KEY AUTOINCREMENT,  \
           col_fname STRING \
           )" )
      #committing the information to the db
      conn.commit ()
#closing the dB 
conn.close()


#telling it to use the new.db
conn = sqlite3.connect ('new.db')

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#include this information in the dB

with conn:
      cur = conn.cursor()

      #iterates through the list of files
      for file in fileList:
            #checks if each item is a .txt file
            if file.endswith(".txt"):
                  #if it is, then insert it into the table
                  cur.execute("INSERT INTO tbl_name(col_fname) VALUES(?)", \
                                    (file,))
      conn.commit()
#closing the information going to the dB
conn.close()

      
      












      

