#!/usr/bin/python
# DLL Encoder - Insecurety Research
# Encodes a DLL as a text file for text_inject.py
# Just does a base64, nothing super exciting...
import sys

print "DLL to Text Encoder - Insecurety Research (2013)"
print "Encodes a DLL as a base64 encoded textfile"

if (len(sys.argv) != 3):
    print "Usage: %s <Path To DLL> <Outfile>" %(sys.argv[0])
    print "Eg: %s C:\\test\messagebox.dll encoded.txt" %(sys.argv[0])
    sys.exit(0)

dll = sys.argv[1]
out = sys.argv[2]

try:
    print "[+] Reading DLL..."
    f = open(dll, "r")
    raw = f.read()
    f.close()
except Exception:
    print "[-] Something failed... Quitting!"
    sys.exit(0)
try:
    print "[+] Creating encoded outfile..."
    encoded = raw.encode('base64')
    g = open(out, "w")
    g.write(encoded)
    g.close()
except Exception:
    print "[-] Something failed... Quitting!"
    sys.exit(0)
print "[+] Encoded File Saved As: %s" %(out)
