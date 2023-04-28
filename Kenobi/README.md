# Kenobi Challenge Write Up

First We have to run nmap command to find all ports that open and what services are available:
``sudo nmap -sV -sC -oN nmap/initials 10.10.170.162``

open ports:
- 21 ftp
- 22 ssh
- 80 http
- 111 rpcbind
- 139/tcp netbios-ssn Samba smbd 3.X - 4.X
- 445/tcp netbios-ssn Samba smbd 4.3.11-Ubuntu
- 2049 nfs_acl     2-3 (RPC #100227)

Then let's search how many shares we could find
using ``nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.170.162 -oN nmap/smb_445``

result:
```bash
PORT    STATE SERVICE                                                                                                                     
445/tcp open  microsoft-ds                                                                                                                                                                                        
                                                                                                                                                                                                                  
Host script results:                                                                                                                                                                                              
| smb-enum-shares:                                                                                                                                                                           
|   account_used: guest
|   \\10.10.170.162\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: IPC Service (kenobi server (Samba, Ubuntu))
|     Users: 1
|     Max Users: <unlimited>
|     Path: C:\tmp
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.170.162\anonymous: 
|     Type: STYPE_DISKTREE
|     Comment: 
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\home\kenobi\share
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.170.162\print$: 
|     Type: STYPE_DISKTREE
|     Comment: Printer Drivers
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\var\lib\samba\printers
|     Anonymous access: <none>
|_    Current user access: <none>
```

we found that we can login as anonymous, so let's do it:
```bash
smbclient //10.10.239.150/anonymous
```

There we can found **log.txt** file, let's back to our machine than use ``smbget`` to get the files in that directory
```bash
smbget -R smb://10.10.239.150/anonymous
```


