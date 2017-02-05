import smtplib, sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


def send_email(from_address_file, from_password_file, email_title_file, email_body_file, email_attachment_file, to_address):

	from_address = get_file(from_address_file)
	from_passowrd = get_file(from_password_file)

	# init msg
	msg = MIMEMultipart()

	# add from- and to- address
	msg['From'] = from_address
	msg['To'] = to_address

	# add title to msg
	msg['Subject'] = get_file(email_title_file)
	
	# add body to msg
	body = get_file(email_body_file)
	msg.attach(MIMEText(body, 'plain'))

	# add attachment to msg
	filename = email_attachment_file
	attachment = get_file(email_attachment_file)
	
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


def get_file(file):
	fp = open(file, 'rb')
	msg = fp.read()
	fp.close()
	return msg


def main():
	if len(sys.argv) != 7:
		print 'Usage: python send_email.py from_address.txt from_passowrd.txt title.txt body.txt attach.txt to_address'
		exit(1)

	from_address_file, from_password_file, email_title_file, email_body_file, email_attachment_file, to_address = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]
	send_email(from_address_file, from_password_file, email_title_file, email_body_file, email_attachment_file, to_address)

if __name__ == '__main__':
	main()