#!/usr/bin/python
# Win32 DLL injector from Grey Hat Python
# Minor formatting cleanups done...
import sys
from ctypes import *

print "DLL Injector implementation in Python"
print "Taken from Grey Hat Python"

if (len(sys.argv) != 3):
    print "Usage: %s <PID> <Path To DLL>" %(sys.argv[0])
    print "Eg: %s 1111 C:\\test\messagebox.dll" %(sys.argv[0])
    sys.exit(0)

PAGE_READWRITE = 0x04
PROCESS_ALL_ACCESS = ( 0x00F0000 | 0x00100000 | 0xFFF )
VIRTUAL_MEM = ( 0x1000 | 0x2000 )

kernel32 = windll.kernel32
pid = sys.argv[1]
dll_path = sys.argv[2]

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
kernel32.WriteProcessMemory(h_process, arg_address, dll_path, dll_len, byref(written))

# Resolve LoadLibraryA Address
h_kernel32 = kernel32.GetModuleHandleA("kernel32.dll")
h_loadlib = kernel32.GetProcAddress(h_kernel32, "LoadLibraryA")

# Now we createRemoteThread with entrypoiny set to LoadLibraryA and pointer to DLL path as param
thread_id = c_ulong(0)

if not kernel32.CreateRemoteThread(h_process, None, 0, h_loadlib, arg_address, 0, byref(thread_id)):
    print "[!] Failed to inject DLL, exit..."
    sys.exit(0)

print "[+] Remote Thread with ID 0x%08x created." %(thread_id.value)
