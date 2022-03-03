import sqlite3
from xlsxwriter.workbook import Workbook
workbook = Workbook('data.xlsx')
worksheet = workbook.add_worksheet()

conn=sqlite3.connect('data.db')
c=conn.cursor()
c.execute("select * from nyt_articles")
mysel=c.execute("select * from nyt_articles LIMIT 100")
for i, row in enumerate(mysel):
    for j, value in enumerate(row):
        worksheet.write(i, j, row[j])
workbook.close()