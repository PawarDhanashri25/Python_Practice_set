# sending main using python
#sending HTML emails using python

# html file strucutre named as "test_email.html"

'''
<html>
<body>
<p> Hello HTML mainl|</p>
<b> Bold text>

</body>
</html>
'''
import smtplib
from emai.message import EmailMessage

#from pathlib import path


#html_content= Path('test_email.html').read_text()

email=EmailMessage()



email['from'] = 'Python <pawardhanashri2002@gmail.com>'
email['to'] = '21032017_cse@adcet.in'
email['subject']= 'Good job python'

email.set_content('Wow! Congratulations')

#email.set_content(html_content, 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('pawardhanashri2002@gmail.com', 'fill_password')
    smtp.send_message(email)

    print("The main sent") 
      
