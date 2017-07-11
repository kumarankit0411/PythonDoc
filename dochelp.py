import sys
import webbrowser

mod = sys.argv[1] if len(sys.argv)>1 else input('Enter the Module name:  ')
fun = mod+'.'+sys.argv[2] if len(sys.argv)==3 else input('Enter the function name[optional]:  ')
if fun!='':
    fun = mod+'.'+fun
url = 'https://docs.python.org/3.6/library/{}.html#{}'.format(mod, fun)
mod += '\n'
file = open('ModulesList/modules.txt', 'r')
if mod == '\n':
    if fun == '':
        print('No input given(Exiting...)\n')
        sys.exit()
    else:
        print('Module name is required(Exiting...)\n')
        sys.exit()
if mod in file:
    webbrowser.open(url)
else:
    print('Built-in module only')

