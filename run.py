#!/usr/bin/python
# Github: https://github.com/404rgr/subdomain-bruter
import re
import sys
import random
import asyncio
from os import path
from sys import platform
from random import choice
from aiohttp import ClientSession
from argparse import ArgumentParser
from shutil import get_terminal_size

# Colors
purple = '\033[95m'
blue = '\033[94m'
cyan = '\033[96m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
end = '\033[0m'
bold = '\033[1m'
u = '\033[4m'
if platform == 'win32':system('color')

class SubdoScan:
    def __init__(self):
        self.banner()
        self.__file__  = path.split(__file__)[1]
        self.wordlist  = 'wordlist.txt'; #default wordlist
        self.output    = ''
        self.main()
    async def fetch(self, subdo, session):
        try:
            url = 'http://' + subdo + '.' + self.domain
            async with session.get(url) as response:
                cols = get_terminal_size((80, 20)).columns
                print("\r" + " " * cols, end="", flush=True)
                print(f"\r{green}Subdomain Found {subdo}.{self.domain}\r")
                self.total_counter +=1
                with open(self.output, 'a') as sv:
                    sv.write(subdo+'.'+self.domain+'\n')
                return await response.read()
        except:
            self.total_counter +=1
    async def bound_fetch(self, sem, subdo, session):
        async with sem:
            await self.fetch(subdo, session)
            cols = get_terminal_size((80, 20)).columns
            print("\r" + " " * cols, end="", flush=True)
            print("\r{}Progress [{}/{}], Last request to: {}"
                  .format(end,self.total_counter, self.total_list, subdo), flush=True, end="")
    
    async def run(self, domain):
        try:
            subdomains = open(self.wordlist, 'r').read().splitlines() # ['tools', 'cpanel', 'admin', 'kosong', "anjay"]
            subdomains = ['tools', 'www', 'aas']
            self.subdomains_length = len(subdomains)
            print("{}[{}] Subdomains List Loaded\n".format(cyan, self.subdomains_length));
        except:
            exit(red+"there is a problem while preparing the word list")
        self.total_list = len(subdomains)
        self.total_counter = 1
        self.domain = domain
        tasks = []
        sem = asyncio.Semaphore(1000)

        async with ClientSession() as session:
            for subdomain in subdomains:
                task = asyncio.ensure_future(self.bound_fetch(sem, subdomain, session))
                tasks.append(task)
            responses = asyncio.gather(*tasks)
            await responses
            cols = get_terminal_size((80, 20)).columns
            print("\r" + " " * cols, end="", flush=True)
            print(f"\r\n*{cyan}Finished")
    def rcolor(self): #random color
        return choice([red,purple,cyan,green,yellow,end])
    def main(self):
        parser = ArgumentParser()
        parser.add_argument('-u', dest='url', type=str, help='URL')
        parser.add_argument('-w', dest='wordlist', type=str, help='Costume Wordlist. Default '+self.wordlist)
        parser.add_argument('-o', dest="output", type=str, help="save the obtained subdomain results. default is not saved")
        args = parser.parse_args()
        if not args.url:
            print("Usage: python {} -u [domain]".format(self.__file__))
            print("Example: python {} -u google.com".format(self.__file__))
            exit("\n(use -h to see more options)")
        if args.wordlist:
            self.wordlist = args.wordlist
        if args.output:
            self.output = args.output
        url = args.url
        domain = re.sub('http(s)?://|/(.*)', '', url)
        print("{}Target: {}".format(yellow, domain))
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(self.run(url))
        loop.run_until_complete(future)
    def banner(self):
        # https://github.com/404rgr/subdomain-bruter
        print("""{}
_{}_    {}_   {}_  {}_ {}_    {}_ {}B
 {}_   {}_        {}_   {}_   {}R
   {}_   {}_  {}_ {}_    {}_    {}U
{}* {}S U B D O M A I N {}* {}T
{} _   {}_{}_  {}_ {}_{}_ {}_  {}_    {}E
  {}_{}_{}_{}_{}    _{}_ _{}_ {}_  {}_  {}R
  {}V1.0{}
""".format(self.rcolor(),self.rcolor(),self.rcolor(),self.rcolor(),self.rcolor(),self.rcolor(),self.rcolor(),cyan,
self.rcolor(),self.rcolor(),self.rcolor(),self.rcolor(),cyan,
self.rcolor(),self.rcolor(),self.rcolor(),self.rcolor(),self.rcolor(),cyan,
red,cyan,red,cyan,
self.rcolor(),self.rcolor(),self.rcolor(),self.rcolor(),self.rcolor(),self.rcolor(),self.rcolor(),self.rcolor(),cyan,
self.rcolor(),self.rcolor(),self.rcolor(),self.rcolor(),self.rcolor(),self.rcolor(),self.rcolor(),self.rcolor(),self.rcolor(),cyan,
green,end
        ))
if __name__ == '__main__':
    try:
        SubdoScan()
    except KeyboardInterrupt:
        print(f"\n\n{red}Ctrl+C Detected!\nProgram Terminated...{end}")