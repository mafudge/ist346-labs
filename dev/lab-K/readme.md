# Lab K Email and Messaging

Setting up an email server takes a long time and requires knowledge of the many services required to download and save email, send email, and provide a user interface for users to interact with their email. All of these services require knowledge of security best practices. For our example we will be using a prebuilt docker container that has all of these services setup for us.

## Goals

- Setup and run the mail server
- Connect via telnet
- Add and start with Roundcube container
- Connect and check email with Roundcube email client

## Setup and run the mail server

To begin start your environment, navigate to the Lab-K folder

```
PS C:\ist346-labs\lab-K> docker-compose up -d
```

This will start 2 containers to start with. An email server, containing Postfix (email inbox server) and an SMTP server for outgoing mail. The other container is a client container with telnet installed.

## Check and send messages with telnet

We can interact with the mail server using the [telnet](https://en.wikipedia.org/wiki/Telnet) program that allows us to interact with the mail server with our terminal.

First login to the telnet client.

```
PS C:\ist346-labs\lab-K> docker exec -it lab-k_telnet_1 bash
```

Once logged in we can start the telnet interface.

```
root@telnet:/# telnet
```

From the telnet prompt connect to the mailserver.

```
telnet> open mailserver 25
Trying 192.168.144.2...
Connected to mailserver.
Escape character is '^]'.
220-mail.mycompany.com ESMTP Postfix (Debian)
```

Once connected to the mailserver you can test the server connection

```
ehlo mycompany.com
```
You should see this

```
250-mail.mycompany.com
250-PIPELINING
250-SIZE 1048576
250-ETRN
250-STARTTLS
250-AUTH PLAIN LOGIN
250-AUTH=PLAIN LOGIN
250-ENHANCEDSTATUSCODES
250-8BITMIME
250-DSN
250 SMTPUTF8
```

Now you can send an email, first define who the message is from

```
mail from: me@mycompany.com
```

second define the recipient

```
rcpt to: myuser@mycompany.com
```

Now set the data

```
data
```

Then enter the following

```
Subject: Test Email

My Test Email
.
```
Don't forget the . at the end! 

If everything worked the you should see something similiar to:
```
250 2.0.0 Ok: queued as E0684127C
```

Then quit out of the smtp server

```
quit
```

That should have delivered our message to our myuser in our fake company.

Now lets check the email using IMAP

Again connect using telnet but this time connect with port 143
```
root@telnet:/# telnet

telnet> open mailserver 143

```

Once connected you can login

```
a LOGIN myuser@mycompany.com mypassword
```

Now list the available mailboxes

```
a LIST "" "*"
```

You should see all the mailboxes setup for the *myuser* account.

Lets check the inbox

```
a EXAMINE INBOX
```

I should Show that we have some email liek below

```
* FLAGS (\Answered \Flagged \Deleted \Seen \Draft)
* OK [PERMANENTFLAGS ()] Read-only mailbox.
* 1 EXISTS
* 1 RECENT
* OK [UNSEEN 1] First unseen.
* OK [UIDVALIDITY 1540413590] UIDs valid
* OK [UIDNEXT 2] Predicted next UID
a OK [READ-ONLY] Examine completed (0.001 + 0.000 secs).
```

Now read the 1st email

```
a FETCH 1 BODY[]
```

You should see your test email that you sent through the server. Not as pretty as gmail.

```
* 1 FETCH (BODY[] {1393}
Return-Path: <me@mycompany.com>
Delivered-To: myuser@mycompany.com
Received: from mail.mycompany.com
        by mail.mycompany.com with LMTP id GD2SE5bY0FtqUAAAScxBiw
        for <myuser@mycompany.com>; Wed, 24 Oct 2018 20:39:50 +0000
Received: from localhost (localhost [127.0.0.1])
        by mail.mycompany.com (Postfix) with ESMTP id 2BF9D12CC
        for <myuser@mycompany.com>; Wed, 24 Oct 2018 20:39:50 +0000 (UTC)
X-Quarantine-ID: <WwSMRRt2wJmJ>
X-Virus-Scanned: Yes
X-Amavis-Alert: BAD HEADER SECTION, Missing required header field: "Date"
X-Spam-Flag: NO
X-Spam-Score: 2.743
X-Spam-Level: **
X-Spam-Status: No, score=2.743 tagged_above=2 required=6.31
        tests=[ALL_TRUSTED=-1, MISSING_DATE=1.396, MISSING_FROM=1,
        MISSING_HEADERS=1.207, MISSING_MID=0.14]
        autolearn=no autolearn_force=no
Received-SPF: None (mailfrom) identity=mailfrom; client-ip=192.168.144.3; helo=mycompany.com; envelope-from=me@mycompany.com; receiver=<UNKNOWN>
Authentication-Results:mail.mycompany.com; dkim=permerror (bad message/signature format)
Received: from mycompany.com (lab-k_telnet_1.lab-k_default [192.168.144.3])
        by mail.mycompany.com (Postfix) with ESMTP id E0684127C
        for <myuser@mycompany.com>; Wed, 24 Oct 2018 20:38:27 +0000 (UTC)
Subject: Test Email
Message-Id: <20181024203950.2BF9D12CC@mail.mycompany.com>
Date: Wed, 24 Oct 2018 20:39:50 +0000 (UTC)
From: me@mycompany.com

My Test Email
)
a OK Fetch completed (0.001 + 0.000 secs).
```

Well that is not the fun way to do that, so lets setup a mail client!

First Logout of your telnet client

```
a Logout
```

In your docker-compose.yml file uncomment or remove the *#* form this section

```
# roundcube:
  #   image: roundcube/roundcubemail
  #   hostname: mailclient
  #   links:
  #     - mailserver
  #   ports:
  #     - 8080:80
  #   environment:
  #     - ROUNDCUBEMAIL_DEFAULT_HOST=mailserver
  #     - ROUNDCUBEMAIL_DEFAULT_PORT=143
```

It should become this:

```
roundcube:
    image: roundcube/roundcubemail
    hostname: mailclient
    links:
      - mailserver
    ports:
      - 8080:80
    environment:
      - ROUNDCUBEMAIL_DEFAULT_HOST=mailserver
      - ROUNDCUBEMAIL_DEFAULT_PORT=143
```

Now rerun docker-compose up, so it starts the new webmail container.


```
PS C:\ist346-labs\lab-K> docker-compose up -d
lab-k_mailserver_1 is up-to-date
lab-k_telnet_1 is up-to-date
Creating lab-k_roundcube_1 ... done
```

Now let's check our web mail open [http://localhost:8080](http://localhost:8080) in your browser. 

You should see the roundcube login. You can login with **myuser@mycompany.com** and **mypassword**

Once logged in you should be able to see your test message! Open an incognito browser window and navigate to [http://localhost:8080](http://localhost:8080) login with the other account **me@mycompany.com** (password: **mypassword**) and try sending messages back and forth between **me@mycompany.com** and **myuser@mycompany.com**. That is about the limit of what you can do with Roundcube due to our setup.

Note: THIS IS NOT A PRODUCTION READY SETUP, there are many other factors that need to be considered when deploying a mail server. TLS encryption and spam are just naming a few. For this setup some of those precautions were disabled. 

