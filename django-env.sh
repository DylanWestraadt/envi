#!/bin/bash
echo '
 ______  _________ _______  _        _______  _______ 
(  __  \ \__    _/(  ___  )( (    /|(  ____ \(  ___  )
| (  \  )   )  (  | (   ) ||  \  ( || (    \/| (   ) |
| |   ) |   |  |  | (___) ||   \ | || |      | |   | |
| |   | |   |  |  |  ___  || (\ \) || | ____ | |   | |
| |   ) |   |  |  | (   ) || | \   || | \_  )| |   | |
| (__/  )|\_)  )  | )   ( || )  \  || (___) || (___) |
(______/ (____/   |/     \||/    )_)(_______)(_______)
                                                      

'

#brew install python3
#brew install pip3

mkdir 'Django'
cd Django
pip3 install virtualenv
virtualenv env
source env/bin/activate
pip3 install django
echo "Name your Django app: "
read varname 
django-admin startproject $varname

