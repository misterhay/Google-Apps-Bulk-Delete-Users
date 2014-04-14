print ('This will delete Google Apps user accounts that are listed in a text file.')
print ('Ensure that your deleteaccounts.txt is in the same directory as this program.')
print ('Each account to be deleted must be on its own line in deleteaccounts.txt.')
#get domain, username, and password from user
domain = raw_input('Google Apps Domain: http://www.')
username = raw_input('Google Apps Admin Username: ')
password = raw_input('Google Apps Admin Password: ')
email = username+'@'+domain
# just to confirm, we'll display their email address
print ('Welcome, '+email)
#log in to Google Apps
import gdata.apps.service
service = gdata.apps.service.AppsService(email=email, domain=domain, password=password)
service.ProgrammaticLogin()
#a variable for counting lines in the file read loop we're going to do
linecount = 0
#get the list of users to delete
f=open ('deleteaccounts.txt', 'r')
#loop through the file and rename then delete accounts
#we rename them first so that the usernames can be reused without having to wait five days
try:
	for delete_this_user in f:
		print ('Deleting user account: '+delete_this_user)
		#strip the newline character and any extra spaces in the line
		delete_this_user = delete_this_user.strip()
		delete_this_renamed_user = (delete_this_user+'ToBeDeletedNow')
		userentry = service.RetrieveUser(delete_this_user)
		userentry.login.user_name = delete_this_renamed_user
		service.UpdateUser(delete_this_user, userentry)
		service.DeleteUser(delete_this_renamed_user)
		#increment linecount variable
		linecount += 1
		#convert the linecount to a string and print it with text
		print (str(linecount)+' users deleted')
#the above code will run until there is an exception
except:
	raw_input (str(linecount)+' user accounts have been deleted, but there was an error.')
#now we wait for the user to press enter, since we're done
raw_input ("We're done, press Enter to close the program...")
