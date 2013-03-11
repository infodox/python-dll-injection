#!/usr/bin/python
# Get PID script
from win32com.client import GetObject
import sys
WMI = GetObject('winmgmts:')

print "Tool for finding the PID of a process"
print "Insecurety Research (2013)"

if len(sys.argv) != 2:
    print "Usage: %s processname" %(sys.argv[0])
    print "Eg: %s explorer.exe" %(sys.argv[0])
    sys.exit(0)

proc = sys.argv[1]

p = WMI.ExecQuery('select * from Win32_Process where Name="%s"' %(proc))
pid = p[0].Properties_('ProcessId')
print "Process ID of %s is %s" %(proc, pid)
