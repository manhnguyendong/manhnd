import psycopg2

conn = psycopg2.connect(
    database="Bill", user='postgres', password='manh123'
)
conn.autocommit = True
#Create Table
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS HANGHOA")
DataGoods = '''CREATE TABLE HANGHOA(
    TENandSize VARCHAR(255) PRIMARY KEY NOT NULL,
    DGIA VARCHAR(255) NOT NULL
)'''
cursor.execute(DataGoods)
cursor.execute("DROP TABLE IF EXISTS phieuthanhtoan")
Databill = '''CREATE TABLE phieuthanhtoan(
    TENHANGHOA VARCHAR(255) NOT NULL,
    SL SMALLINT NOT NULL,
    DGIA VARCHAR(255) NOT NULL,
    TTIEN VARCHAR(255) NOT NULL,
    FOREIGN KEY (TENHANGHOA) REFERENCES HANGHOA(TENandSize)
)'''
cursor.execute(Databill)
print('Created successfully')

conn.close()