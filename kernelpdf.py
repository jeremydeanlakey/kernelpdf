# possible useful notes
# http://www.oldlinux.org/Linux.old/Linux-0.01/docs/Linux.pdf

code_src = 'https://www.kernel.org/pub/linux/kernel/Historic/linux-0.01.tar.gz'

from subprocess import call
call(['wget', code_src])
call(['tar', '-xzvf', 'linux-0.01.tar.gz'])
