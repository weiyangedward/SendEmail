import smtplib, sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

from_address = 'weiyangedward@gmail.com'
from_passowrd = '198956Yw'
# to_address = 'weiyangedward2@gmail.com'


def send_email(email_title_file, email_body_file, email_attachment_file, to_address):

	# init msg
	msg = MIMEMultipart()

	# add from- and to- address
	msg['From'] = from_address
	msg['To'] = to_address

	# add title to msg
	msg['Subject'] = get_msg(email_title_file)
	
	# add body to msg
	body = get_msg(email_body_file)
	msg.attach(MIMEText(body, 'plain'))

	# add attachment to msg
	filename = email_attachment_file
	attachment = get_msg(email_attachment_file)
	
	part = MIMEBase('application', 'octet-stream')
	part.set_payload(attachment)
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

	msg.attach(part)
	
	# login gmail server
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(from_address, from_passowrd)

	# send email
	server.sendmail(from_address, to_address, msg.as_string())
	server.quit()


def get_msg(file):
	fp = open(file, 'rb')
	msg = fp.read()
	fp.close()
	return msg


def main():
	if len(sys.argv) != 5:
		print 'Usage: python send_email.py title.txt body.txt attach.txt to_address'
		exit(1)

	email_title_file, email_body_file, email_attachment_file, to_address = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
	send_email(email_title_file, email_body_file, email_attachment_file, to_address)

if __name__ == '__main__':
	main()