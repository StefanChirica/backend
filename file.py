from sqlalchemy import create_engine
#db is uberdb
#user is copac
#password is copac

db_string = "postgresql://copac:copac@localhost:5432/uberdb"

db = create_engine(db_string)

# Create 
db.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")  
db.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")

# Read
result_set = db.execute("SELECT * FROM films")  
for r in result_set:  
    print(r)

# Update
db.execute("UPDATE films SET title='Some2016Film' WHERE year='2016'")

# Delete
db.execute("DELETE FROM films WHERE year='2016'")