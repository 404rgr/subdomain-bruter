# Subdomain Bruter
`Subdomain Bruter` is a tool to find subdomains on a website by trying to guess the available subdomains in the wordlist and testing it by making a request to the http protocol.

## Installation & Run
> note: requires python3.*
#### Install python
```
sudo apt install python
git clone https://github.com/404rgr/subdomain-bruter
cd subdomain-bruter
```

#### Install Modules
```
pip install aiohttp
```

#### Run
```
python run.py -u [domain]
```

```
__    _   _  _ _    _ B                                                                                                                                                
 _   _        _   _   R                                                                                                                                                
   _   _  _ _    _    U                                                                                                                                                
* S U B D O M A I N * T                                                                                                                                                
 _   __  _ __ _  _    E                                                                                                                                                
  ____    __ __ _  _  R                                                                                                                                                
  V1.0                                                                                                                                                                 

usage: run.py [-h] [-u URL] [-w WORDLIST] [-o OUTPUT]

optional arguments:
  -h, --help   show this help message and exit
  -u URL       URL
  -w WORDLIST  Costume Wordlist. Default wordlist.txt
  -o OUTPUT    save the obtained subdomain results. default is not saved

```
