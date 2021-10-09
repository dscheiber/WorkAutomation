import pandas
import time

excelDataDF = pandas.read_excel('Test-RFC.xlsm', sheet_name="MasterList")

periodStart = "2021-07-01"
periodEnd = "2021-09-30"


## filters the main db by date and sorts by requester
open_date_filter = excelDataDF.query('`INITIATION DATE`>= @periodStart and `INITIATION DATE`<= @periodEnd').sort_values(by='REQUESTER', ascending=True)
closed_date_filter = excelDataDF.query('`DATE CLOSED`>= @periodStart and `DATE CLOSED`<= @periodEnd').sort_values(by='REQUESTER', ascending=True)

def filter_by_users(df): ## gets a user list which will be used to loop through the values
    users_from_df = df.REQUESTER
    users = []
    for user in users_from_df:
        if user not in users:
            users.append(user)

    for user in users:
        user_filter = df.query('`REQUESTER` == @user')
        print(user_filter)

    ##to finish this section, i need to either filter or format these in various ways, maybe apply a function that says DUE SOON or PAST DUE to late ones

def rfc_metrics(df_open, df_closed):
    initiated_rfc = df_open.shape[0]
    closed_rfc = df_closed.shape[0]
