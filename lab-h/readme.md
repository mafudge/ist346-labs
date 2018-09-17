# Storage and Network File Systems

Network File Systems and access control

## Part 1: SMB and PAM

Simple SMB server using Samba. Access control will be controlled by simple Samba users and PAM.

### Setup

#### Goals

1. Setup a Simple Samba Server
2. Demonstrate how to start and stop services on Linux (Ubuntu)
3. Demonstrate how to create a user and file share on the server.
4. Start a Linux client, and mount the new share to the clients filesystem, demonstrate how the file is really created on the server from the client.

#### Step 1: Setup the server

The server has the proper dependencies and packages pre installed.

Lets start by brining up our docker environment. Open you terminal and navigate to the folder that contains the docker-compose file for part 1. And the docker-compose up

```
$ docker-compose up -d
```

You should see something similiar to the following screen.

```
Creating network "part1_default" with the default driver
Creating part1_server_1 ... done
Creating part1_client_1 ... done
```

So now the server and client are running waiting to be setup!

First docker exec into the server

```
$ docker exec -it part1_server_1 bash
```

Once at the server container root prompt, lets setup the server. First we need to add a new user that will allow us to connect to our share. When is asks for a password use something easy to remember

```
$ useradd ist-t-user --shell /bin/false
```

This will add a new user with the username ist-t-user, the --shell flag does not allow the user to login to the server.

Next we need to create a home directory for the user and give the new user ownership of the directory

```
$ mkdir -p /home/ist-t-user
$ chown ist-t-user:ist-t-user /home/ist-t-user

# ls command lists the directory and ownership info
# Should show that ist-t-user owns the directory
$ ls -l /home
total 4
drwxr-xr-x 1 ist-t-user ist-t-user 4096 Sep 12 03:08 ist-t-user
```

Now we need to configure Samba to share the directory with clients to do this we need to edit the smb.conf file that is installed with Samba. We do this with the nano editor using the command below.

```
$ nano /etc/samba/smb.conf
```

The file contains an enormous amount of configuration options. We are going to go right to the bottom of the file and add the code below

```
[myshare]
path = /home/ist-t-user
valid users = ist-t-user
available = yes
browsable = yes
public = yes
writable = yes
read only = no
```

What's this? this tell samba to expost the path /home/ist-t-user and call it myshare. The only user that can access this share is ist-t-user. The other options allow for browsability and access.

Once you add the above code to the smb.conf file you should test it for errors.

```
$ testparm
```
When you run this it will ask you to hit enter, and you will see an output similiar to the one below

```
Load smb config files from /etc/samba/smb.conf
WARNING: The "syslog" option is deprecated
Processing section "[printers]"
Processing section "[print$]"
Processing section "[myshare]"
Loaded services file OK.
Server role: ROLE_STANDALONE

Press enter to see a dump of your service definitions

# Global parameters
[global]
        server string = %h server (Samba, Ubuntu)
        server role = standalone server
        map to guest = Bad User
        obey pam restrictions = Yes
        pam password change = Yes
        passwd program = /usr/bin/passwd %u
        passwd chat = *Enter\snew\s*\spassword:* %n\n *Retype\snew\s*\spassword:* %n\n *password\supdated\ssuccessfully* .
        unix password sync = Yes
        syslog = 0
        log file = /var/log/samba/log.%m
        max log size = 1000
        dns proxy = No
        usershare allow guests = Yes
        panic action = /usr/share/samba/panic-action %d
        idmap config * : backend = tdb


[printers]
        comment = All Printers
        path = /var/spool/samba
        create mask = 0700
        printable = Yes
        browseable = No


[print$]
        comment = Printer Drivers
        path = /var/lib/samba/printers


[myshare]
        path = /home/ist-t-user
        valid users = ist-t-user
        read only = No
        guest ok = Yes
```

If there is an error it will tell you, the output below is shortened so you can see the error.

```
Load smb config files from /etc/samba/smb.conf
WARNING: The "syslog" option is deprecated
Processing section "[printers]"
Processing section "[print$]"
Processing section "[myshare]"
Unknown parameter encountered: "pathjk"
Ignoring unknown parameter "pathjk"
WARNING: No path in service myshare - making it unavailable!
NOTE: Service myshare is flagged unavailable.
Loaded services file OK.
Server role: ROLE_STANDALONE

Press enter to see a dump of your service definitions
...
```

Can you see what the error is?

After the server setup is complete and there are no errors we can start the service.

First check the status.
So see the status of a service, you can use the following command

```
$ service samba status
* nmbd is not running
* smbd is not running
```

Currently our service is not running, lets fix that.
user the service command to start samba, you will see the output below.

```
$ service samba start
* Starting NetBIOS name server nmbd       [ OK ]
* Starting SMB/CIFS daemon smbd           [ OK ]
```

To stop a service use the following command, if you stop it don't forget to start it again before moving onto the client setup!

```
$ service samba stop
* Stopping Samba AD DC daemon samba           [ OK ]
* Stopping SMB/CIFS daemon smbd               [ OK ]
* Stopping NetBIOS name server nmbd           [ OK ]
```

At this point you can exit the container, or open a new terminal to access the client.

#### Access the share from a client

To access the running client use docker exec

```
$ docker exec -it part1_client_1 bash
```

Once logged in you can view the shares provided by the server using the command below.

```
$ smbclient -L //server -U ist-t-user

WARNING: The "syslog" option is deprecated
Enter ist-t-user's password:
Domain=[WORKGROUP] OS=[Windows 6.1] Server=[Samba 4.3.11-Ubuntu]

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        myshare         Disk
        IPC$            IPC       IPC Service (35f96533555e server (Samba, Ubuntu)) Domain=[WORKGROUP] OS=[Windows 6.1] Server=[Samba 4.3.11-Ubuntu]

        Server               Comment
        ---------            -------
        35F96533555E         35f96533555e server (Samba, Ubuntu)

        Workgroup            Master
        ---------            -------
        **WORKGROUP**
```

We can see that the *myshare* that we created listed in the output

To actually use the share, we need to mount it to the client file system. To do this we use the *mount* command.

```
$ mkdir /mnt/myshare
$ mount -t cifs -o user=ist-t-user //server/myshare /mnt/myshare
```

after entering the password the shared path is now mounted to the local filesystem, and we can interact with it just like it was part of the client.

We can create files

```
$ echo "my new file" > /mnt/myshare/test.txt
```

We can list the files (You should see the test.txt file that was created above)

```
$ ls /mnt/myshare
```

Now lets check the server, if you exited before, open a new terminal and docker-exec into the server.

```
$ docker exec -it part1_server_1 bash
```

List the items in the share, we should see the new test.txt file!

```
$ ls /home/ist-t-user
test.txt

$ cat test.txt
my new file
```






- Show shares using samba client
- Connect to samba share using client
- Mount folder using mount command
- Navigate to directory, add a file and some text
- Show on server that file is there

## SMB with LDAP

Creating and SMB server utilizing LDAP for access control, Use prebuild samba control

### Setup

Start LDAP Server
Configure SMB Server for ldap

Log into client with proper user

## Cloud Storage with Minio (Self Hosted S3)

Minio Server and Bucket policies

## Setup

Install Minio

Create a Bucket, set the bucket Policy with Minio client

View Bucket with minio UX

Connect and interact with MC client