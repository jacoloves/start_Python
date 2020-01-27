import stat
import os
os.chmod('oops.txt', stat.S_IRUSR)