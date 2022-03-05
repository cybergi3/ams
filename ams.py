#!/bin/python3

import os , sys
import subprocess


def checkdistrofromfile():
    currentdist = (subprocess.check_output(['brl','which','ls']))
    if currentdist == b'void\n':
        return 'void'
    if currentdist == b'arch\n':
        return 'arch'
    if currentdist == b'fedora\n':
        return 'fedora' 
    if currentdist == b'gentoo\n':
        return 'gentoo'
    if currentdist == b'ubuntu\n':
        return 'ubuntu'
    if currentdist == b'alpine\n':
        return 'alpine'
    if currentdist == b'centos\n':
        return 'centos'
    if currentdist == b'debian\n':
        return 'debian'
    if currentdist == b'devuan\n':
        return 'devuan'

bashcommand = None
package = None
currentdistro = checkdistrofromfile()
update = 0 # 0 = is no update 1 is update the current distro and 2 is to all distros
upgrade = 0 # same as update
remove = False # 1 for true | 1 will remove the package while 0 will install it
ask = 0
NOAUR = 0
def handlinginput():
    global update , upgrade , package , remove , ask , NOAUR , currentdistro
    for i in range((len(sys.argv))):
        if sys.argv[i] == "fetch":
            package = sys.argv[(i + 1)]
            #print(package)
        elif sys.argv[i] == "set":
            currentdistro = sys.argv[(i + 1)]
            #print(currentdistro)
        elif sys.argv[i] == "update":
            if checkdistro(sys.argv[(i + 1)]) != False:
                update = checkdistro(sys.argv[(i + 1)])
            else:
                update = 1
        elif sys.argv[i] == "upgrade":
            if checkdistro(sys.argv[(i + 1)]) != False:
                upgrade = checkdistro(sys.argv[(i + 1)])
            else:
                upgrade = 1
        elif sys.argv[i] == "remove":            
            package = sys.argv[i]
            remove = True
        elif sys.argv[i] == "ask":
            ask = 1
        elif sys.argv[i] == "NOAUR":
            NOAUR = 1
        else:
            if not checkdistro(sys.argv[i]):
                package = sys.argv[i]
def checkdistro(arg):
    if arg == "debian":
        return 3 
    elif arg == "devuan":
        return 4 
    elif arg == "ubuntu":
        return 5
    elif arg == "gentoo":
        return 6
    elif arg == "centos":
        return 7
    elif arg == "arch":
        return 8
    elif arg == "fedora":
        return 9
    elif arg == "void":
        return 10
    elif arg == "alpine":
        return 11
    elif arg == "all":
        return 2
    else:
        return False
def bash():
    global bashcommand
    if not remove:
        if currentdistro == "void":
            bashcommand = "sudo brl strat void xbps-install " + package
        elif currentdistro == "debian":
            bashcommand = "sudo brl strat debian apt install " + package
        elif currentdistro == "gentoo":
            bashcommand = "sudo brl strat gentoo emerge " + package
        elif currentdistro == "devuan":
            bashcommand = "sudo brl strat devuan apt install " + package
        elif currentdistro == "ubuntu":
            bashcommand = "sudo brl strat ubuntu apt install " + package
        elif currentdistro == "fedora":
            bashcommand = "sudo brl strat fedora dnf install " + package
        elif currentdistro == "alpine":
            bashcommand == "sudo brl strat alpine apk install " + package
        elif currentdistro == "centos":
            bashcommand == "sudo brl strat centos yum install " + package
        elif currentdistro == "arch":
            bashcommand == "sudo brl strat arch pacman -S " + package
        else:
            bashcommand == "echo distro not found"

def main():
    handlinginput()
    print(update)
    print(upgrade)
    print(currentdistro)
    print(package)
main()


