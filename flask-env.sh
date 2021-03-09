#!/bin/bash
echo '
 _______  _        _______  _______  _       
(  ____ \( \      (  ___  )(  ____ \| \    /\
| (    \/| (      | (   ) || (    \/|  \  / /
| (__    | |      | (___) || (_____ |  (_/ / 
|  __)   | |      |  ___  |(_____  )|   _ (  
| (      | |      | (   ) |      ) ||  ( \ \ 
| )      | (____/\| )   ( |/\____) ||  /  \ \
|/       (_______/|/     \|\_______)|_/    \/
                                             
   
'

#brew install python3
#brew install pip3

mkdir 'Flask-env'
cd Flask-env
pip3 install virtualenv
virtualenv env
source env/bin/activate
pip3 install flask flask-sqlalchemy 
