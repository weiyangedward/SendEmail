# SendEmail

This is an python agent to send emails to a list of receivers. (e.g. from linkedin: http://www.business2community.com/linkedin/export-linkedin-contacts-linkedin-01516051#SUwOMJTU3v7bb3j2.97)

This agent uses gmail server to send email on behalf of you. Make sure you have 'Less secure apps' turn on after sign in gmail on web: https://www.google.com/settings/security/lesssecureapps

Agent features:

- only takes gmail account as sender.
- allows you to input your gmail email address and password.
- sends email with title, body and an attachment (e.g. txt, pdf, etc).
- sends email to multiple receivers by adding receiver addresses to the 'to_addresses.txt' file.

Running example can be found within folder './script'.

TODO:

1. a script to generate email title, body with modified receiver and company names
2. write send_email_API that takes a generated email and other information to send the email.
