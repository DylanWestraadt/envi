import subprocess
import os

#chmod the bash files
os.chmod('flask-env.sh',0o755)
os.chmod('react-env.sh',0o755)
os.chmod('django-env.sh' ,0o755)
os.chmod('react-node.sh' ,0o755)

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
main = input('Select environment to set up: \n [1] Django \n [2] Flask\n [3] React\n ==>')
main_int = int(main)

def django():
    django_load = subprocess.call("./django-env.sh")
def flask():
    flask_load = subprocess.call("./flask-env.sh")
def react():
    flask_load = subprocess.call("./react-env.sh")
def reactnode():
    flask_load = subprocess.call("./react-node.sh")

  
if main_int == 1:
    django()
elif main_int == 2:
    flask()
elif main_int == 3:
    react()
elif main_int == 4:
    reactnode()
else:
     print("na man...you need glasses...")   