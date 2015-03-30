###########################
#    Cloud functions      #
#                         #
# This file contains all  #
# the functions related   #
# with uploading the file #
# to Dropbox.             #
###########################

###############
#  Libraries  #
###############

import dropbox                      #Import the function that uploads a file to Dropbox

###############
#  Variables  #
###############

#Dropbox info

KEY = "your-project-key"             #The key of the Dropbox project
SECRET = "your-project-secret"          #The secret of the Dropbox project
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(KEY, SECRET) #Autentication of the key and secret
FILENAME = "file.txt"               #This is the file we want to upload

#autentication stuff
authorizeUrl = flow.start()
print authorizeUrl
authCode = raw_input("Enter the code: ").strip()

accessToken, userId = flow.finish(authCode)

client = dropbox.client.DropboxClient(accessToken)

uploadFile = open(FILENAME, 'rb')
responce = client.put_file(FILENAME, uploadFile)
print responce

###############
#  Functions  #
###############


