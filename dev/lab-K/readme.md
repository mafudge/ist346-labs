# Lab K Email and Messaging

Setting up an email server takes a long time and requires knowledge of the many services required to download and save email, send email, and provide a user interface for users to interact with their email. All of these services require knowledge of security best practices. For our example we will be using a prebuild docker container that has all of these services setup for us.

## Goals

- Setup and mail server
- Add email account
- Connect via telnet
- Connect and check email with roundcube email

Users
Users are managed in postfix/accounts.cf.
Just add the full email address and its password separated by a pipe.

Example:

user1@domain.tld|mypassword
user2@otherdomain.tld|myotherpassword