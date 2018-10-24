# Information Security

Cloud Computing, Using 3rd party services for web application authentication. Working on your app and deploying to **ANY** cloud!

## Goals

- Create UFW rule and enable ufw, show that client can no longer access the server
- Allow server to deny a client with ufw
- Demonstrate hardening of service http. Stop the demo xxs attack
- password-less ssh Create Pub/Private Keys

## Utlizing a firewall

The first line of defense for any system is the firewall. Firwalls limit traffic to ports defined by the system adminstrator. This stops malicious users from accessing the system through ports opened by services or software. On linux many system administors utilize IPTables to create a firewall. Due to the complexity and flexibility of Iptables we will be using a simplified version call UFW.

Lets begin by bring up a simple network consisting of a simple webserver and a client and a potential hacker.

```
PS C:\ist346>docker-compose up if ufw-example.yml -d
```

Now lets see what is going on with our server. There have been reports of slowness etc from users.

```
PS C:\ist346>docker-compose logs -f lab-j_nginx_1
```

Whoa, What is going on! Our weblogs are showing the attacker making attempts at user and admin logins.

We need to stop this user!

Open and new terminal and login to the server. Leave the window with the logs open
```
PS C:\ist346>docker exec -it lab-j_nginx_1 bash
```

Once logged in we need to setup a firewall to stop malicious users. UFW is already installed on most Linux distributions.

The best way to guarantee security in to stop everything then only let in what you need we do this be setting the default UFW policy to deny all traffic by default.

```
root@webserver:/# ufw default deny
```

Once that is set lets turn the firewall on.

```
root@webserver:/# ufw enable
```

No open another terminal windows and lets check the logs of the webserver and see what happened.

Great! the attack was stopped. Buts lets login to another client and see how the site is working.

Open another terminal and login to the test client that was setup for you.

```
PS C:\ist346>docker exec -it lab-j_client_1 bash
```

After you login lets try to *curl* the website

```
root@client:/# curl -m 3 http://172.44.1.102
```
Uh Oh, that's not good, it looks like our clients can't access the site either. This happened because we stopped all traffic to the server, lets fix this by first opening up port 80 this allows non https traffic to reach or server once we create the rule we need to reload the firewall.


```
root@webserver:/# ufw allow 80
root@webserver:/# ufw reload
```

Now check your client again by using curl. You should find that you can access the website again.

If you check your server logs you see that the hacker is attacking again, lets stop that attack by blocking traffic from that IP address. If we look at the logs being created on the server you can find the IP address of the attacker.

```
172.44.1.104 - - [15/Oct/2018:14:50:34 +0000] "POST /admin HTTP/1.1" 404 153 "-" "curl/7.47.0" "-"
```

Their address is 172.44.1.104 you can see this at the beginning of the line on the logs. Lets block that person by inserting a new rule at position number 1, UFW evaluates rules in order, so we need to make sure our block rule is before the allow all rule for port 80. The status command shows the current rules.

```
root@webserver:/# ufw insert 1 deny from 172.44.1.104 to any
root@webserver:/# ufw reload
root@webserver:/# ufw status numbered
Status: active

     To                         Action      From
     --                         ------      ----
[ 1] Anywhere                   DENY IN     172.44.1.104
[ 2] 80                         ALLOW IN    Anywhere
[ 3] 80 (v6)                    ALLOW IN    Anywhere (v6)
```

And now check your server logs again, and you will see the attacker has been stopped. This is a very simple example, UFW has many options I encourage you to check the documentation for many other ways to secure your server.

## Locking Down NGINX

One of the most used and exposed services on a server is the webserver, that is utilized at many companies. But regardless of the webserver they all need to be configured to protect against attacks.

Cross-site scripting (XSS) is a type of computer security vulnerability typically found in web applications. XSS enables attackers to inject client-side scripts into web pages viewed by other users. A cross-site scripting vulnerability may be used by attackers to bypass access controls such as the same-origin policy. XSS attacks are performed by an attacker inputting a script into a form field on a website such as a comment field on a blog or forum.

These types of attacks can be mitigated by the webserver, informing the client to not download resources from external sources that you do not control.

Get started by running docker compose, if you still have other services running stop those first.

```
PS C:\ist346>docker-compose -f .\vulnerable-website.yml up -d
```

Two webservices are started, one in our website, the other is a server that a malicious user controls.

Open your browser and open the [demo website](http://localhost)

The malicious user has compromised your site by loading an external script in a comment box. Lets fix our webserver so these attacks do not effect our good users. We are also going to add some other security measures that help harden our webserver.

Open a new terminal window and login to the webserver.

```
PS C:\ist346>docker exec -it lab-j_nginx_1 bash
```

Once logged into the server, you need to edit the nginx configuration file for the default site.

```
root@webserver:/# nano /etc/nginx/conf.d/default.conf
```

Copy and paste the code below into you `default.conf` file.



```
# don't send the nginx version number in error pages and Server header
server_tokens off;

# config to don't allow the browser to render the page inside an frame or iframe
# and avoid clickjacking http://en.wikipedia.org/wiki/Clickjacking
# if you need to allow [i]frames, you can use SAMEORIGIN or even set an uri with ALLOW-FROM uri
# https://developer.mozilla.org/en-US/docs/HTTP/X-Frame-Options
add_header X-Frame-Options SAMEORIGIN;


# This header enables the Cross-site scripting (XSS) filter built into most recent web browsers.
# It's usually enabled by default anyway, so the role of this header is to re-enable the filter for 
# this particular website if it was disabled by the user.
# https://www.owasp.org/index.php/List_of_useful_HTTP_headers
add_header X-XSS-Protection "1; mode=block";

# with Content Security Policy (CSP) enabled(and a browser that supports it(http://caniuse.com/#feat=contentsecuritypolicy),
# you can tell the browser that it can only download content from the domains you explicitly allow in our example we are allowing google analytics.
add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://ssl.google-analytics.com";

```

When you are finished your `default.conf` file should look like the one below:
```
server {
    listen       80;
    server_name  localhost;

    # don't send the nginx version number in error pages and Server header
    server_tokens off;

    # config to don't allow the browser to render the page inside an frame or iframe
    # and avoid clickjacking http://en.wikipedia.org/wiki/Clickjacking
    # if you need to allow [i]frames, you can use SAMEORIGIN or even set an uri with ALLOW-FROM uri
    # https://developer.mozilla.org/en-US/docs/HTTP/X-Frame-Options
    add_header X-Frame-Options SAMEORIGIN;


    # This header enables the Cross-site scripting (XSS) filter built into most recent web browsers.
    # It's usually enabled by default anyway, so the role of this header is to re-enable the filter for 
    # this particular website if it was disabled by the user.
    # https://www.owasp.org/index.php/List_of_useful_HTTP_headers
    add_header X-XSS-Protection "1; mode=block";

    # with Content Security Policy (CSP) enabled(and a browser that supports it(http://caniuse.com/#feat=contentsecuritypolicy),
    # you can tell the browser that it can only download content from the domains you explicitly allow in our example we are allowing google analytics.
    add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://ssl.google-analytics.com";

    #charset koi8-r;
    #access_log  /var/log/nginx/host.access.log  main;

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
    }

    #error_page  404              /404.html;

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }

    # proxy the PHP scripts to Apache listening on 127.0.0.1:80
    #
    #location ~ \.php$ {
    #    proxy_pass   http://127.0.0.1;
    #}

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #
    #location ~ \.php$ {
    #    root           html;
    #    fastcgi_pass   127.0.0.1:9000;
    #    fastcgi_index  index.php;
    #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
    #    include        fastcgi_params;
    #}

    # deny access to .htaccess files, if Apache's document root
    # concurs with nginx's one
    #
    #location ~ /\.ht {
    #    deny  all;
    #}
}
```

Save the file by pressing ctrl+x and saving over the current file.

Reload the webserver configuration, you should see the message below, otherwise is will tell you that there is an error
```
root@webserver:/# nginx -s reload
2018/10/16 10:45:59 [notice] 28#28: signal process started
```

Now check your [website](http://localhost). The message should no longer load because we told the browser not to load external scripts.

This is just the beginning of what needs to be done to harden a webserver, check the NGINX documentation for other recommended security practices.

## Utilizing private/public ssh keys for SSH.

Key pairs allow you to login to a remote host without using your password, this way you can only access the host from machines that had the private key installed.

If you have containers still running from previous lessons shut those down now. Then bring up your environment

```
PS C:\ist346> docker-compose -f .\ssh-keys.yml up -d
```

First we need to create a user and keys for that user. Login to the ssh-server.

```
PS C:\ist346> docker exec -it lab-j_ssh-server_1 bash
```

Once logged in create you new user

```
root@ssh-server:/# adduser myuser
```

Follow the onscreen prompts to create your user.

Make sure your user can connect to the ssh-server, open a new terminal window and login

```
PS C:\ist346> docker exec -it lab-j_ssh-client_1 bash
```

Once logged in to the client you should now be able to ssh to the server

```
root@ssh-client:/# ssh myuser@ssh-server
The authenticity of host 'ssh-server (172.20.0.2)' can't be established.
ECDSA key fingerprint is SHA256:iV9FBVXcbAK0fFuM2ecIOuExbnpP1apuejmsNXuPcvk.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'ssh-server,172.20.0.2' (ECDSA) to the list of known hosts.
myuser@ssh-server's password:
Welcome to Ubuntu 16.04.4 LTS (GNU/Linux 4.9.93-linuxkit-aufs x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

myuser@ssh-server:~$
```

exit out of the user account 

```
myuser@ssh-server:~$ exit
```

From the client we can now generate ssh keys, to be used on the server

```
root@ssh-client:/# ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:qzIS1bPB+Yf+nnNHgXmbp8N00C6W+cMpVj4ox3dU6/Q root@ssh-client
The key's randomart image is:
+---[RSA 2048]----+
|                 |
|                 |
|     o .     o . |
|    . *     o + o|
|   .   =S.   . Oo|
|  .   . o..   X+=|
|   .   ...  .=BBo|
|  . o  .. .o.*=OE|
|   . o.  o+o+.o.+|
+----[SHA256]-----+
root@ssh-client:/# ssh myuser@ssh-server
myuser@ssh-server's password:
Welcome to Ubuntu 16.04.4 LTS (GNU/Linux 4.9.93-linuxkit-aufs x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
Last login: Tue Oct 16 14:16:53 2018 from 172.20.0.3
```

Once you have the keys generated they exit in /root/.ssh/

Keys are generated in pairs, a private key and a public key. Your private key should always be kept secret and never distributed to other system. The public key is what other systems use to authenticate

Upload the public key to the server under the user account we created.

First make a .ssh directory on the server from the client

```
root@ssh-client:/# ssh myuser@ssh-server mkdir -p .ssh
```

Then we upload the key to a special file called **authorized_keys**

```
root@ssh-client:/# cat /root/.ssh/id_rsa.pub | ssh myuser@ssh-server 'cat >> .ssh/authorized_keys'
```

If you look on the server you will now see a new file under .ssh

```
myuser@ssh-server:~/.ssh$ ls
authorized_keys
```

If we **cat** this file you will see the public key. (yours will be different)

```
myuser@ssh-server:~/.ssh$ cat authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCuYmc6toOzLNga95izpfQBNhn3psUoYFpVa4wHPDBwLMQchsp3DjXdVDbBn6clpZB0zCA8M28gKSqKPutc1KAXjDVqoC8/GYE9hlnwMmLgICuEzMSPZYuKQNrzQoQ+o47hviQIJkJEXcd+DsuDm8E7Rjw00DxRG0/ohClhJ57
WxHiSYjMB+Tw/0pYLQ0d6kuoI7ClHWaYhxMhLFoN8Qlw66Qy/F7LIDOaWPBM6wJWuB9dV40x+Ehi77JYtExa+RvOUpvlDvZWYVPtJWGxicVt5mWBqV8BJgvMQQhn0f0uFmPml5VqAERM7Hju3b4X+zm5yOveliqJRPDcU4TfLRAD root@ssh-client
myuser@ssh-server:~/.ssh$
```

while on the server set the permissions of the authorized_keys file so only our user can access it, if still on the myuser account exit to the root account

```
root@ssh-server:/home/myuser# chmod 700 /home/myuser/.ssh; chmod 640 /home/myuser/.ssh/authorized_keys
```

You should no be able to access the ssh-server without typing a password

```
root@ssh-client:/# ssh myuser@ssh-server
Welcome to Ubuntu 16.04.4 LTS (GNU/Linux 4.9.93-linuxkit-aufs x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
Last login: Tue Oct 16 14:30:58 2018 from 172.20.0.3
myuser@ssh-server:~$
```



