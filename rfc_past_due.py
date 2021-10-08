import win32com.client as win32
import csv

#this is a row of data used for testing the sendMail function
testLine = ['C 21 151', '08/24/2021 0:00:00', 'Revise SP/4090/001, SP/5049/001-0004.00 to .01', 'correct # of water determinations required', 'XW Pharma', 'Open', 'MLR', '09/30/2021 0:00:00', '', '', '09/30/2021 0:00:00', 'LAF', 'N/A', 'Samantha McLaughlin <Samantha.McLaughlin@pacelabs.com>']

##query file - this is a small test to commit
queryFile = "S:\\Public\\Quality System Admin\\Support Files\\RFC\\Past Due CCs - Emails.txt"

def sendMail(queryline):
    ##stages all the csv line variables
    rfc_number = queryline[0]
    rfc_initiation = queryline[1][:10]
    rfc_task = queryline[2]
    rfc_reason = queryline[3]
    rfc_due_date = queryline[10][:10]
    rfc_current_extension = queryline[12]
    rfc_email = queryline[13]

    ##stages all the email variables
    subject = 'Past Due Change Control Reminder for ' + rfc_number
    body = 'Hi, \nThis is an automated reminder that the following RFC is past due: \n' + \
    'RFC#: ' + rfc_number + '\n' + \
    'Task: ' + rfc_task + '\n' + \
    'Description: ' + rfc_reason + '\n' + \
    'Due Date: ' + rfc_due_date + '\n' + \
    'Current Extension: ' + rfc_current_extension + '\n' + '\n' \
    'If there are any questions or corrections, please reply to this email. Thanks.'
    #htmlbody = '<h2> Using HTML Message body </h2>'

    #send the email
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = rfc_email
    mail.Subject = subject
    mail.Body = body
    #mail.HTMLBody = htmlbody #this field is optional

    # To attach a file to the email (optional):
    #attachment  = "Path to the attachment"
    #mail.Attachments.Add(attachment)

    mail.Send()

def readQuery(queryFile):
    with open(queryFile, newline='') as csvfile:
	    reader = csv.reader(csvfile, delimiter=",", quotechar='"')
	    for row in reader:
		    sendMail(row)


readQuery(queryFile)
#sendMail(testLine)