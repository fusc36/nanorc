# I can't script with bash...

import os

pad = '''
#include "/usr/local/share/nano/python.nanorc"
#include "/usr/local/share/nano/nanorc.nanorc"
#include "/usr/local/share/nano/sh.nanorc"
#include "/usr/local/share/nano/rust.nanorc"
#include "/usr/local/share/nano/html.nanorc"

include "%s/nanorc/nanorc-share/*.nanorc"
set whitespace ">>"

set constantshow
set linenumbers
'''

home = os.path.expanduser('~')
nanorc = os.path.join(home, '.nanorc')

with open(nanorc, 'w') as f:
	f.write(pad % (home)) # replaces with home directory

print('Setup finished')
