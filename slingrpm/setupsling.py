import os.path
import sys
import subprocess

from slingrpm import NoRepoException
from slingrpm import AlreadySlingEnabledException 

def execute(cmd):
  fd = open('execute.log', 'a')
  retcode = subprocess.check_call([cmd], stderr=fd, stdout=fd, shell=True)
  fd.close()
  return retcode

class SetupSling:

  def __init__(self, repopath):
    fullrepopath = os.path.abspath(repopath)
    if not os.path.isdir(fullrepopath):
      raise NoRepoException('directory not found at: ' + fullrepopath)
    if not os.path.isdir(os.path.join(fullrepopath, 'repodata')):
      execute('createrepo ' + fullrepopath)
    if not os.path.isfile(os.path.join(fullrepopath, '.slingrpm.conf')):
      fd = open(os.path.join(fullrepopath, '.slingrpm.conf'), 'w')
      fd.write('foo')
      fd.close()
    else:
      raise AlreadySlingEnabledException('repo at : ' + fullrepopath + ' already sling enabled!')