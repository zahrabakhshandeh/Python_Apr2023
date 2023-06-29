from config import *
## add
def add(name, phone):
    mycursor = mydb.cursor()
    query = "INSERT INTO contacts (name, phone) VALUES (%s, %s)"
    values = (name, phone)
    mycursor.execute(query, values)
    mydb.commit()
    mycursor.close()
## Search
def search(name):
    mycursor = mydb.cursor()
    query = "SELECT * FROM contacts WHERE name LIKE %s"
    name = "%" + name + "%"
    values = (name,)
    mycursor.execute(query, values)
    contacts = mycursor.fetchall()
    mycursor.close()
    return contacts
## delete 
def delete(name):
    mycursor = mydb.cursor()
    query = "DELETE FROM contacts WHERE name = %s"
    values = (name, )
    mycursor.execute(query, values)
    mydb.commit()
    mycursor.close()