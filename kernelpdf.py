# possible useful notes by Linus Torvalds
# http://www.oldlinux.org/Linux.old/Linux-0.01/docs/Linux.pdf
import os
from subprocess import call

CODE_URL = 'https://www.kernel.org/pub/linux/kernel/Historic/linux-0.01.tar.gz'

def get_files():
    call(['wget', CODE_URL])
    call(['tar', '-xzvf', 'linux-0.01.tar.gz'])

# TODO for use later
def pdf(path):
    contents = os.listdir()
    for node in contents:
        pdf(path + '/' + node)

# TODO for use later
def tree_string(depth, output):
    if depth == 0:
        return path
    return '| ' * (depth-1) + '|-' + path

class HtmlOutput(object):
    def __init__(self, fname='kernel.html'):
        self.fname = fname
        self.fout = open(fname, 'w')
        self.fout.write('<html>\n')
    def close(self):
        self.fout.write('</html>')
        self.fout.close()
    def print_file(self, path):
        self.fout.write('<h3>' +  path + '</h3> <br />\n')
        self.fout.write('<pre>\n')
        for line in open(path).readlines():
            self.fout.write(line)
        self.fout.write('</pre><br /> <br /> <br />\n')
    def write_line(self, line):
        self.fout.write(line + '\n')
        
def printfolder(output, depth, folder, target):
    contents = os.listdir(folder)
    #print tree_string(depth, folder + '/')
    for item in contents:
        path = os.path.join(folder, item)
        if os.path.isdir(path):
            #print tree_string(depth+1, path + '/')
            printfolder(output, depth+1, path, target)
        else:
            output.print_file(path)
            #print tree_string(depth+1, path)

output = HtmlOutput()
printfolder(output, 0, 'linux', [])


