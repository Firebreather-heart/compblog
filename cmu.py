import sys,os 
commands = ['makemigrations', 'migrate', 'shell']
def managecommand(command):
    for com in command:
        os.system(f'python manage.py {com}')

cd =  {1:'makemigrations',2:"migrate", 3:"shell",4:'runserver'}
buc = []
for arg in sys.argv:
    buc.append(arg)
buc = buc[1:]
print(buc)
if buc[0] == '1':
    managecommand([cd[1], buc[0]])
elif buc[0] == '2':
    managecommand([cd[2], buc[0]])
elif buc[0] == "3":
    managecommand([cd[3], buc[0]+" "+int(buc[1])])
elif buc[0] == "4":
    managecommand([cd[4], buc[0]])
elif buc[0] == "all":
    managecommand([cd[1], buc[0]])
    managecommand([cd[2], buc[0]])
else:print('not found')
