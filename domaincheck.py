# Get email id as input and check if using a custom domain or a public mail domain.
publicemail = ["yahoo.com", "hotmail.com",
               "gmail.com", "mail.com", "outlook.com", "aol.com"]
emailid = input("Enter your email id : ")
emaillen = len(emailid)
delindex = emailid.index('@')
domain = emailid[delindex+1:emaillen+1]
if domain in publicemail:
    print(emailid, " - using a public email domain")
else:
    print(emailid, " - using a custom domain")
