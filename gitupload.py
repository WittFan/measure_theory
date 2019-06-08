import sys,os
import time
os.system("git status")
os.system("git add *")
now=time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
os.system("git commit -m '%s'" %now)
os.system("git push")
os.system("")
os.system("")
os.system("")
os.system("")
os.system("")
os.system("")

