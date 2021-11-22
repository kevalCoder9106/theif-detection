# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
   
class send_mail:
    def __init__(self,from_mail,from_mail_pass,user_email) -> None:
        self.from_mail = from_mail
        self.from_mail_pass = from_mail_pass

    def send_mail(self,msg):
        try:
            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)
            
            # start TLS for security
            s.starttls()
            
            # Authentication
            s.login(self.from_mail, self.from_mail_pass)
            
            # message to be sent
            message = msg
            
            # sending the mail
            s.sendmail(self.from_mail, self.user_email, message)
            
            # terminating the session
            s.quit()
        except:
            return f"[-] Error sending video clip"

    def send_mail_with_attachment(self,subject,body,clip_path=None):
        try:
            fromaddr = self.from_mail
            
            # instance of MIMEMultipart
            msg = MIMEMultipart()
            
            # storing the senders email address  
            msg['From'] = fromaddr
            
            # storing the receivers email address 
            msg['To'] = self.user_email
            
            # storing the subject 
            msg['Subject'] = subject
            
            # string to store the body of the mail
            body = body
            
            # attach the body with the msg instance
            msg.attach(MIMEText(body, 'plain'))
            
            # open the file to be sent 
            filename = clip_path
            attachment = open(filename, "rb")
            
            # instance of MIMEBase and named as p
            p = MIMEBase('application', 'octet-stream')
            
            # To change the payload into encoded form
            p.set_payload((attachment).read())
            
            # encode into base64
            encoders.encode_base64(p)
            
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            
            # attach the instance 'p' to instance 'msg'
            msg.attach(p)
            
            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)
            
            # start TLS for security
            s.starttls()
            
            # Authentication
            s.login(fromaddr, self.from_mail_pass)
            
            # Converts the Multipart msg into a string
            text = msg.as_string()
            
            # sending the mail
            s.sendmail(fromaddr, self.user_email, text)
            
            # terminating the session
            s.quit()

            return f"[+] Successfully sended video clip"
        except:
            return f"[-] Error sending video clip"