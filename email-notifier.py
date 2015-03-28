################################
#      E-mail functions        #
#                              #
# This file contains all the   #
# functions related to sending #
# an e-mail to notify the user #
# that the file has been       #
# uploaded.                    #
################################

###############
#  Libraries  #
###############

import smtplib                                 #The library needed to send e-mails using smtp protocol
from email.mime.text import MIMEText           #Import ome modules used

###############
#  Variables  #
###############

reportNum = 0                                   #The numbers of notifications sent

#Sender and reciver information

FROM = 'notifier@example.com'                   #The e-mail used to send the notifications
TO = 'reciver@example.com'                      #The e-mail that will recive the notifications

USERNAME = FROM                                 #Setting the sender username to the sender e-mail
PASSWORD = 'password'                           #Sender password

#Contents of the notification e-mail

mf = open('notification-message.txt')           #Open the file that contains the message of the e-mail
msg = MIMEText(mf.read())                       #Add the contents of the message file into the message
mf.close()                                      #Closes the message file

msg['Subject'] = 'Notification #' + str(reportNum) #The subject of the notification e-mail
msg['From'] = FROM                              #The notificator e-mail
msg['To'] = TO                                  #The e-mail that will recive the notification (this is for the body of the e-mail)

###############
#  Functions  #
###############

def sendNotification(server, user, password, message): #The function that sends the e-mail
    server = smtplib.SMTP(server)                      #Initializing the conection with the server
    server.starttls()                                  #Start tls encriptation (needed for Gmail)
    server.login(user, password)                       #Login
    server.sendmail(FROM, TO, msg.as_string())         #Sending the e-mail
    server.quit()                                      #Closing conection with the server
