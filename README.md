ca sa initializezi env:
source env/bin/activate

apoi apare (env) la inceput apoi poti rula python3 filename.py sau ce o fii


in alt terminal:
sudo su postgres
psql (o sa intre in terminalul de postgres)
create user *username* with password *password*
grant all privileges on database *databasename* to *username*

to create a db: create database *databasename*

connection string: postgressql://[user[:password]@][netloc][:port][/dbname][param1=value1&...] ------------ 
                                                                                                e.g."postgresql://copac:copac@localhost:5432/uberdb"
                                                                                                in cazul asta userul este copac cu parola copac @ local pe portul 5432 in baza de date uberdb