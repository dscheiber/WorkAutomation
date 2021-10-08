import pandas
import time

excelDataDF = pandas.read_excel('W:\\Change Control\\CHANGE CONTROL LOG.xlsm', sheet_name="MasterList")

Q3Start = "2021-07-01"
#Q3StartConverted = time.strptime(Q3Start, '%Y-%m-%d')
#print(Q3StartConverted)
#print("Passed the start.")
Q3End = "2021-09-30"
#Q3EndConverted = time.strptime(Q3End, '%Y-%m-%d')
#print(Q3EndConverted)
#print('Passed the end.')

open_date_filter = excelDataDF.query('`INITIATION DATE`>= @Q3Start and `INITIATION DATE`<= @Q3End')
opened_count = open_date_filter.shape(0)



print(date_filter)