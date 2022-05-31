from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,lastname,receiver):
    # Creating message subject and sender
    subject="Welcome To NazArticles Newsletter"
    sender="mnazwambura@gmail.com"

    #passing in the context vairables
    text_content=render_to_string('email/newsemail.txt',{"name": name,"lastname":lastname})
    html_content=render_to_string('email/newsemail.html',{"name":name,"lastname":lastname})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()


