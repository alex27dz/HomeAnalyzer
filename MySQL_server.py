import mysql.connector
import time

# example of working MySQL insertion into table

print('Connect to MySQL server')
db = mysql.connector.connect(
    host='localhost',  # ip when it will be on cloud
    user='root',
    passwd='NV27vnmc',
    database='data_list_storage'
)
mycursor = db.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
db.commit()
time.sleep(1)

'''
Hi this is mysql server configuration code :)
How it works:
Using SQL commands to communicate with mySQL server and do operations
- Make sure MySQL server is up and running (locally, server)
- Importing the mysql.connector module to set up connection with the server
- After we connected , creating database / connecting to database
- Create tables / connect to tables (Address_automation_tool , Builders_automation_tool)
- Copy the converted data to JSON, time, address to our tables
- Finally we got data stored as JSON in our mysql database
How to use the stored data ?
- We just need to go to the wanted address/column and extract the JSON data using json.loads()
* Important rule: when creating columns - the names must be in regular type not ()*&6%$#@[ ] and no spaces
Done :)


connection to server
Endpoint:
database-1.cpleepa9rb37.ca-central-1.rds.amazonaws.com

Port:
3306

Username:
admin

Password:
Sagol$$$30

תנסה לחבר את הדיבי ותגיד לי אם אתה מסתדר.
אצלי ב- Microsoft SQL הוא רק מבקש server name שזה בעצם האנדפוינט פסיק והפורט, ככה:
database-1.cpleepa9rb37.ca-central-1.rds.amazonaws.com,3306

ואז שם משתמש וססמא.

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='NV27vnmc',
    database='data_list_storage'
    )
mycursor = db.cursor()


----------------------------------------------------------------------------------------------------------------------
# DESCRIBE - printing the 'Person' table in the database
# INSERT INTO - Add item - adding info to the table
# SELECT * FROM - Get Item - how to get the item the element from the table in this case is everything (*)
# CREATE TABLE - creating new table under the name 'Person' giving it elements: (name, age, personID)
# mycursor.execute('ALTER TABLE data_list_table DROP [element]') - deleting the column
# change name of the columns and tables
# mycursor.execute('ALTER TABLE data_list_table CHANGE [old name] [new name] VARCHAR(50)')
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
----------------------------------------------------------------------------------------------------------------------
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

# printing test table
mycursor.execute('DESCRIBE test')
for x in mycursor:
    print(x)
----------------------------------------------------------------------------------------------------------------------
# mycursor.execute("CREATE TABLE [] ()")
# mycursor.execute("CREATE TABLE test (time VARCHAR(255), street VARCHAR(255), alex VARCHAR(255))")
# db.commit()

Executing commands example:
# address name
address = 'major_mac'
address2 = 'aylin_cres'
address3 = 'young'
time_now = datetime.datetime.now()

# create list of columns without spaces and special signs
# mycursor.execute('CREATE TABLE Address_automation_tool (time VARCHAR(255), address VARCHAR(255), data JSON)')
# db.commit()
# time.sleep(5)

cma_list = []

# converting list dicts to
cma_list = json.dumps(cma_list)
#print(cma_list)


# inserting into columns (address and data in json format)
sql = "INSERT INTO Address_automation_tool (address, time, data) VALUES (%s, %s, %s)"
val = (address3, time_now, cma_list)
mycursor.execute(sql, val)
db.commit()
time.sleep(5)


# printing table3
mycursor.execute('SELECT * FROM Address_automation_tool')
for x in mycursor:
    print(x)
----------------------------------------------------------------------------------------------------------------------
'''
'''
mycursor.execute('DESCRIBE Limited_Information')
for x in mycursor:
    print(x)
mycursor.execute('DESCRIBE Full_Information')
for x in mycursor:
    print(x)
'''
'''



Tables Creation 
Creation of Full_Information table
CREATE TABLE `data_list_storage`.`Full_Information` (
  `time` VARCHAR(255) NULL,
  `address` VARCHAR(255) NULL,
  `population_total_metro` VARCHAR(255) NULL,
  `population_growth_2010-2019_metro` VARCHAR(255) NULL,
  `projected_population_growth_2019-2024_metro` VARCHAR(255) NULL,
  `total_housing_units_metro` VARCHAR(255) NULL,
  `owner_occupied_hu_metro` VARCHAR(255) NULL,
  `renter_occupied_hu_metro` VARCHAR(255) NULL,
  `vacant_housing_units_metro` VARCHAR(255) NULL,
  `family_households_metro` VARCHAR(255) NULL,
  `average_household_size_metro` VARCHAR(255) NULL,
  `income_median_household_metro` VARCHAR(255) NULL,
  `income_average_household_metro` VARCHAR(255) NULL,
  `median_home_value_metro` VARCHAR(255) NULL,
  `avarage_sold_price_metro` VARCHAR(255) NULL,
  `avarage_asking_price_metro` VARCHAR(255) NULL,
  `community_name` VARCHAR(255) NULL,
  `population_total` VARCHAR(255) NULL,
  `population_growth_2010-2019` VARCHAR(255) NULL,
  `projected_population_growth_2019-2024` VARCHAR(255) NULL,
  `total_housing_units` VARCHAR(255) NULL,
  `owner_occupied_hu` VARCHAR(255) NULL,
  `renter_occupied_hu` VARCHAR(255) NULL,
  `vacant_housing_units` VARCHAR(255) NULL,
  `median_home_value` VARCHAR(255) NULL,
  `average_sold_price` VARCHAR(255) NULL,
  `average_asking_price` VARCHAR(255) NULL,
  `family_households` VARCHAR(255) NULL,
  `average_household_size` VARCHAR(255) NULL,
  `income_median_household` VARCHAR(255) NULL,
  `income_average_household` VARCHAR(255) NULL,
  `crime_rate` VARCHAR(255) NULL,
  `elementary_school_rating` VARCHAR(255) NULL,
  `middle_school_rating` VARCHAR(255) NULL,
  `high_school_rating` VARCHAR(255) NULL,
  `global_data` JSON NULL);


Creation of limited information table 
CREATE TABLE `data_list_storage`.`Limited_Information` (
  `time` VARCHAR(255) NULL,
  `address` VARCHAR(255) NULL,
  `state` VARCHAR(255) NULL,
  `metro` VARCHAR(255) NULL,
  `model` VARCHAR(255) NULL,
  `size` VARCHAR(255) NULL,
  `bedrooms` VARCHAR(255) NULL,
  `bathrooms` VARCHAR(255) NULL,
  `garage` VARCHAR(255) NULL,
  `price` VARCHAR(255) NULL,
  `down_payment` VARCHAR(255) NULL,
  `picture_url` VARCHAR(255) NULL,
  `community_list_of_addresses` JSON NULL,
  `community_mapped_list_of_addresses` JSON NULL,
  `global_data` JSON NULL);

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

# printing table
mycursor.execute('DESCRIBE Full_Information')
for x in mycursor:
    print(x)

'''
# address = 'major_mac'
# time_now = datetime.datetime.now()
# create list of columns without spaces and special signs
# add params from xls structure
# mycursor.execute('CREATE TABLE Limited_Information (time VARCHAR(255), address VARCHAR(255), data JSON)')
# db.commit()
# cma_list = []
# converting list dicts to
# cma_list = json.dumps(cma_list)
# print(cma_list)
# inserting into columns (address and data in json format)
# sql = "INSERT INTO Address_automation_tool (address, time, data) VALUES (%s, %s, %s)"
# val = (address3, time_now, cma_list)
# mycursor.execute(sql, val)
# db.commit()
'''


# printing the data from MySQL
mycursor.execute('DESCRIBE Limited_Information')
for x in mycursor:
    print(x)
mycursor.execute('SELECT * FROM Full_Information')
for x in mycursor:
    print(x)
# printing the data from MySQL
mycursor.execute('DESCRIBE Address_automation_tool')
for x in mycursor:
    print(x)
mycursor.execute('SELECT * FROM Address_automation_tool')
for x in mycursor:
    print(x)
print('success - Connection to MySQL')
except:
print('failed - Connection to MySQL')'''



import mysql.connector



dict_home_data = {
    'address': '14402 English Lavender Drive, Wimauma, FL 33598',
    'name_community': '',
    'home_name': 'Hartford',
    'home_site': '',
    'availability': '',
    'priced_from': '',
    'home_size': '',
    'stories': '',
    'beds': '',
    'baths': '',
    'garage': '',
    'id': '',
    'id_generated': '',
    'description': '',
    'included_features_pdf': 'under solution',
    'floorplans_with_furniture_pic': '',
    'gallery_view_picture': ''
}


# copy to MySQL
print('Connecting to MySQL server')
db = mysql.connector.connect(
    host='localhost',  # ip when it will be on cloud
    user='root',
    passwd='NV27vnmc',
    database='data_list_storage')
print(db)  # checking our connection to DB
mycursor = db.cursor()
command = "SELECT * FROM Limited_Information WHERE address = " + "'" + dict_home_data['address'] + "'" + " AND model = " + "'" + dict_home_data['home_name'] + "'"
print(command)

mycursor.execute(command)
myresult = mycursor.fetchall()  # Note: We use the fetchall() method, which fetches all rows from the last executed statement.
print(len(myresult))
print(myresult)

'''
if len(myresult) == 0:
    print('Similar homes not found, copying to database!')
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='NV27vnmc',
        database='data_list_storage')
    mycursor = db.cursor()
    print(db)
    sql = "INSERT INTO Limited_Information (id_generated, time) VALUES (%s, %s)"
    val = ("alex", datetime.datetime.now())
    mycursor.execute(sql, val)
    db.commit()
    time.sleep(3)
    print('IMPORTANT - Home data copied to mySQL')
else:
    print('Similar homes found in database, NOT copying to mySQL')


'''


'''
print('Trying to Connect and copy same data to MySQL server')
                            try:
                                db = mysql.connector.connect(
                                    host='localhost',
                                    user='root',
                                    passwd='NV27vnmc',
                                    database='data_list_storage'
                                )
                                mycursor = db.cursor()
                                print(db)  # checking our connection to DB

                                # add if statement to check home details before and copy only if the home not located in the sql before
                                sql = "INSERT INTO Limited_Information (id_generated, time, address, state, metro, model, size, bedrooms, bathrooms, garage, price, picture_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                val = (self.dict_home_data['id_generated'],
                                       datetime.datetime.now(),
                                       self.dict_home_data['address'],
                                       self.short_state,
                                       self.metropolitan,
                                       self.dict_home_data['home_name'],
                                       self.dict_home_data['home_size'],
                                       self.dict_home_data['beds'],
                                       self.dict_home_data['baths'],
                                       self.dict_home_data['garage'],
                                       self.dict_home_data['priced_from'],
                                       self.dict_home_data['gallery_view_picture'])
                                mycursor.execute(sql, val)
                                db.commit()
                                time.sleep(3)
                                print('IMPORTANT - Home data copied to mySQL')

                                mycursor.execute("SELECT * FROM Limited_Information WHERE address = '14402 English Lavender Drive, Wimauma, FL 33598' AND model = 'Harrrtford'")
                                myresult = mycursor.fetchall()  # Note: We use the fetchall() method, which fetches all rows from the last executed statement.
                                print(len(myresult))

                                if len(myresult) == 0:
                                    print('Similar homes not found, copying to database!')
                                    db = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        passwd='NV27vnmc',
                                        database='data_list_storage')
                                    mycursor = db.cursor()
                                    print(db)
                                    sql = "INSERT INTO Limited_Information (id_generated, time, address, state, metro, model, size, bedrooms, bathrooms, garage, price, picture_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                    val = (self.dict_home_data['id_generated'],
                                           datetime.datetime.now(),
                                           self.dict_home_data['address'],
                                           self.short_state,
                                           self.metropolitan,
                                           self.dict_home_data['home_name'],
                                           self.dict_home_data['home_size'],
                                           self.dict_home_data['beds'],
                                           self.dict_home_data['baths'],
                                           self.dict_home_data['garage'],
                                           self.dict_home_data['priced_from'],
                                           self.dict_home_data['gallery_view_picture'])
                                    mycursor.execute(sql, val)
                                    db.commit()
                                    time.sleep(3)
                                    print('IMPORTANT - Home data copied to mySQL')
                                else:
                                    print('Similar home found in database - NOT copying to mySQL')


                            except:
                                print('failed to work with mySQL')

'''