# OverPass1 WriteUp

## Reconnaissance
First Thing First, let's find out how many ports we could find using nmap. 
```sh
nmap -sV -sC -oN nmap/initials [Machine_IP]
```
The result is:

1. 22/TCP SSH
2. 80/TCP HTTP

Open it using port 80 and it brought us to **Password Management** Download Page. Download the Go-Lang script. THe Script just tell us that it encrypt the password using ROT47 Caesar method.
Nothing is interesting, so let's just brute-force all hidden directories using gobuster.
```sh
gobuster dir -u [Machine_IP] -w [dirlist_path] php,js,html,py
``` 
Then we'll find an admin page, we have to insert the right password dan username to get access. If you look into the js file, you'll see that if we set a cookies as **SessionToken** with any value in it, we might get access as admin.
```sh
curl [Machine_IP] --cookie "SessionToken=Anything"
```
And we got access.

Inside, it tell us that there's a user named james and an rsa key. so lets just copy it, find the passphrase, then use it as out ssh access in port 22 (if possible)
## PassPhrase Hash Using Ssh2john
so, we have rsa key, save it as **id_rsa**, and let's bruteforce to find the passphrase using ssh2john
```sh
sudo ssh2john id_rsa > rsa.txt
```
then let's find what is the passphrase that have same hash as our hashed rsa.txt file
```sh
john --wordlist=/usr/share/wordlists/rockyou.txt rsa.txt
```
it will return us a **james13** string, which we could use to connect via ssh remote access.
```sh
ssh -i id_rsa james@[Machine_IP]
```
and insert james13 as PassPhrase.




