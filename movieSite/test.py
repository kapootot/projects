#!/usr/bin/python

import MySQLdb
import os
import moviedata


conn = MySQLdb.connect("192.168.0.56","root","q1q2q3","movies")
c = conn.cursor()
c.execute("select * from moviedb;")
rowsInMain = str(c.rowcount)
c.execute("select * from moviedb_tmp;")
rowsInTmp = (str(c.rowcount))
if (rowsInTmp!=rowsInMain):
    c.execute("TRUNCATE TABLE moviedb_tmp;")
    c.execute("INSERT moviedb_tmp SELECT * FROM moviedb;")
    c.execute("TRUNCATE TABLE moviedb;")
    conn.commit()
#create = c.execute("CREATE TABLE moviedb (title_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, title VARCHAR(40) NOT NULL, title_year VARCHAR(10) NULL, downloaded VARCHAR(40) NOT NULL, imdb_rating VARCHAR(5) NULL, watched ENUM ('Y', 'N') NOT NULL, subtitles ENUM ('Y', 'N') NOT NULL,updated TIMESTAMP);")
    
rootdir = "/run/user/1000/gvfs/smb-share:server=192.168.0.50,share=completed"
videoExtensions = [".avi",".mp4",".mkv",".mpg",".mpeg",".mov",".rm",".vob",".wmv",".flv",".3gp"]

def scan(rootdir):

    conn = MySQLdb.connect("192.168.0.56","root","q1q2q3","movies")
    c = conn.cursor()
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            try:
                ext = os.path.splitext(file)[1]
                if ext in videoExtensions:
                   fname = os.path.join(root, file)
                   inputlist = moviedata.Main(fname)
                   #print inputlist
                   query = "INSERT INTO moviedb (title, title_year, downloaded, imdb_rating, watched, subtitles) VALUES ('%s', '%s', '%s', '%s', '%s', '%s');" % (str(inputlist[0]), str(inputlist[1]), str(inputlist[4]), str(inputlist[2]), "N", str(inputlist[3]))
                   #print query
                   c.execute(query)
                   conn.commit()
                   print "Added '%s'" % file
            except:
                   print "Problem adding '%s'" % (file)

   
   
conn.close()

    
        
if __name__=="__main__":
    scan(rootdir) 
