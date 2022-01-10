import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = ''
PASSWORD = ''

SUBJECT=input("Subject: ")
DOMAIN=input("Domain: ")
DOMAIN_FINAL=DOMAIN.replace("http", "hxxp")
FULL_URL=input("Full URL: ")
FULL_URL_FINAL= FULL_URL.replace("http", "hxxp")
SCREENSHOT=input("Screen Shot: ")
HOSTIN=input("Who shall i send the email too? (000webhost, ovh, hostinger, goddaddy, vautron, midphase, cloudflare, aws, namecheap, tektonic, freenom (.tk, just type freenom): ")
if HOSTIN == "000webhost":
  HOST= "abuse@000webhost.com"
elif HOSTIN=="hostinger":
  HOST="abuse@hostinger.com"
elif HOSTIN == "godaddy":
  HOST="abuse@godaddy.com"
elif HOSTIN == "midphase":
  HOST="abuse@midphase.com"
elif HOSTIN == "vautron":
  HOST="abuse@vautron.de"
elif HOSTIN == "cloudflare":
  HOST="abuse@cloudflare.com"
elif HOSTIN == "aws":
  HOST = "abuse@amazonaws.com"
elif HOSTIN == "namecheap":
  HOST = "abuse@namecheap.com"
elif HOSTIN == "tektonic":
  HOST = "abuse@tektonic.net"
elif HOSTIN == "freenom":
  HOST= "abuse@freenom.com"
elif HOSTIN == "ovh":
  print("Ce domaine appartient à OVH, veuillez le signaler à cette adresse : https://www.ovh.com/abuse/#!/")
def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('contacts.txt')
    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=HOSTIN, DOMAIN_PLACEHOLDER=DOMAIN_FINAL, LINK_PLACEHOLDER=FULL_URL_FINAL, SCREENSHOT_URL=SCREENSHOT)
		
        # Prints out the message body for our sake
        print(message)
        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=HOST
        msg['Subject']=SUBJECT
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    main()