#import smtp
import smtplib
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

# sender's email details
SEmail = input(" sending email: \n")
password = input("Password: \n"
server.login('Email', 'password')

# recievers email
REmail = input("Recieving email: \n")
message = input("message: ")
server.sendmail(SEmail, REmail, str(message))

print("sent succefully")
