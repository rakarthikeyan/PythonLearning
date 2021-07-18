import boto3
session = boto3.Session(profile_name="root")
iamclient = session.client(service_name="iam")
iamclient.create_user(UserName='karthis3user')
iamclient.create_login_profile(
    UserName='karthis3user',
    Password='My123R@ndomPassword',
    PasswordResetRequired=True)

iamclient.attach_user_policy(UserName='karthis3user',
                             PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess')

iamclient.attach_user_policy(UserName='karthis3user',
                             PolicyArn='arn:aws:iam::aws:policy/IAMUserChangePassword')
print("ID created..")
