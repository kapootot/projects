import MySQLdb
import os
import moviedata


finalInput = []    
conn = MySQLdb.connect("localhost","root","q1q2q3","movies")
c = conn.cursor()
create = c.execute("CREATE TABLE moviedb (title_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, title VARCHAR(100) NOT NULL, title_year VARCHAR(10) NULL, downloaded VARCHAR(40) NOT NULL, imdb_rating VARCHAR(5) NULL, watched ENUM ('Y', 'N') NOT NULL, subtitles ENUM ('Y', 'N') NOT NULL,updated TIMESTAMP);")
    
rootdir = "D:\\Utorrent\Completed\\"
videoExtensions = [".avi",".mp4",".mkv",".mpg",".mpeg",".mov",".rm",".vob",".wmv",".flv",".3gp"]

def scan(rootdir):
    
    #conn = MySQLdb.connect("localhost","root","q1q2q3","movies")
    #c = conn.cursor()
    
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            try:
                ext = os.path.splitext(file)[1]
                if ext in videoExtensions:
                    fname = os.path.join(root, file)
                    inputlist = moviedata.Main(fname)
                    finalInput.append(inputlist)
                    print "Adding '%s'" % file
                    #query = "INSERT INTO moviedb (title, title_year, downloaded, imdb_rating, watched, subtitles) VALUES ('%s', '%s', '%s', '%s', '%s', '%s');" % (str(inputlist[0]), str(inputlist[1]), str(inputlist[4]), str(inputlist[2]), "N", str(inputlist[3]))
                    
                    
            except:
                    print "Problem adding '%s'" % (file)
                        
    
    
    
   
def concat(finalInput):
    conn = MySQLdb.connect("localhost","root","q1q2q3","movies")
    c = conn.cursor()
    insertValues = ""
    for i,val in enumerate(finalInput):
        insertValues += "("+str(val)+")"+","
    insertValues = insertValues[0:-1]
    toQuery = insertValues.translate(None, '[]')
    
    #print toQuery
    query = "INSERT IGNORE INTO moviedb (title, title_year, imdb_rating, subtitles, watched, downloaded) VALUES"+toQuery+";"
    
    #print query
    
    c.execute(query)
    conn.commit()
    conn.close()
    print "Added data successfully"
    
    
    
        
if __name__=="__main__":
    scan(rootdir)
    concat(finalInput)