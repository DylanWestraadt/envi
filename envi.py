import subprocess
import os

#chmod the bash files
os.chmod('flask-env.sh',0o755)
os.chmod('django-env.sh' ,0o755)

print('''
                                                                      
                                                                      
EEEEEEEEEEEEEEEEEEEEEE                                          iiii  
E::::::::::::::::::::E                                         i::::i 
E::::::::::::::::::::E                                          iiii  
EE::::::EEEEEEEEE::::E                                                
  E:::::E       EEEEEEnnnn  nnnnnnnn vvvvvvv           vvvvvvviiiiiii 
  E:::::E             n:::nn::::::::nnv:::::v         v:::::v i:::::i 
  E::::::EEEEEEEEEE   n::::::::::::::nnv:::::v       v:::::v   i::::i 
  E:::::::::::::::E   nn:::::::::::::::nv:::::v     v:::::v    i::::i 
  E:::::::::::::::E     n:::::nnnn:::::n v:::::v   v:::::v     i::::i 
  E::::::EEEEEEEEEE     n::::n    n::::n  v:::::v v:::::v      i::::i 
  E:::::E               n::::n    n::::n   v:::::v:::::v       i::::i 
  E:::::E       EEEEEE  n::::n    n::::n    v:::::::::v        i::::i 
EE::::::EEEEEEEE:::::E  n::::n    n::::n     v:::::::v        i::::::i
E::::::::::::::::::::E  n::::n    n::::n      v:::::v         i::::::i
E::::::::::::::::::::E  n::::n    n::::n       v:::v          i::::::i
EEEEEEEEEEEEEEEEEEEEEE  nnnnnn    nnnnnn        vvv           iiiiiiii
                                                                      
                                                                    
''')

#choose django or flask
main = input('Select environment to set up: \n [1] Django \n [2] Flask\n ==>')
main_int = int(main)

def django():
    #run the django bash file
    django_load = subprocess.call("./django-env.sh")
   

def flask():
    #run flask bash file
    flask_load = subprocess.call("./flask-env.sh")
  
if main_int == 1:
    #if its django
    django()
elif main_int == 2:
    #if it flask
    flask()
else:
     print("na man...you need glasses...its only 1 or 2")   