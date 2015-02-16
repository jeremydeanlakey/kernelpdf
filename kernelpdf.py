# possible useful notes
# http://www.oldlinux.org/Linux.old/Linux-0.01/docs/Linux.pdf

import os
from subprocess import call

CODE_URL = 'https://www.kernel.org/pub/linux/kernel/Historic/linux-0.01.tar.gz'

call(['wget', CODE_URL])
call(['tar', '-xzvf', 'linux-0.01.tar.gz'])


def pdf(path):
    contents = os.listdir()
    for node in contents:
        pdf(path + '/' + node)

pdf('../linux')
  
