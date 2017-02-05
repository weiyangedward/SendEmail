# SendEmail

This is an python agent to send emails to a list of receivers. 

This agent uses gmail server to send email on behalf of you. Make sure you have 'Less secure apps' turn on after sign in gmail on web: https://www.google.com/settings/security/lesssecureapps

This agent:

- only takes gmail account as sender.
- allows you to input your gmail email address and password.
- sends email with title, body and an attachment (e.g. txt, pdf, etc).
- sends email to multiple receivers by adding receiver addresses to the 'to_addresses.txt' file.

Running example can be found within folder './script'.

TODO:

1. use linkedin API to pull down a list of address according to profile that you are interested in (e.g. recruiter)
2. a script to generate email title, body with modified receiver and company names
	
