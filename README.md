python-dll-injection
====================

Python toolkit for injecting DLL files into running processes on Windows

This toolkit is ever expanding as I bother hacking up extra parts for it.
It was inspired after reading Grey Hat Python as a little bit of bedtime reading 
to familiarize myself with using Python on Windows for interacting with processes, etc.

Anyway, here is a breakdown of the components and their usage:

dll_inject.py - Simple enough Python DLL injector. Give it a DLL and a PID to inject into, and it will inject the DLL into the process using the createRemoteThread API.

$ python dll_inject.py

DLL Injector implementation in Python

Taken from Grey Hat Python

Usage: dll_inject.py <PID> <Path To DLL>

Eg: dll_inject.py 1111 C:\test\messagebox.dll




dll_encoder.py - Rather simple tool, takes in a DLL file and outputs it as a base64 encoded text file for use with other tools.

$ python dll_encoder.py 

DLL to Text Encoder - Insecurety Research (2013)

Encodes a DLL as a base64 encoded textfile

Usage: dll_encoder.py <Path To DLL> <Outfile>

Eg: dll_encoder.py C:\test\messagebox.dll encoded.txt



ads_encoded_dll_inject.py - my piece de resistance :) it takes in the encoded DLL file, decodes it, stores the decoded DLL file in ADS, and then injects it into the process of your choice.

$ python ads_encoded_dll_inject.py 

Encoded DLL Injector

uses ADS streams for extra 1337'ness

version 0.1.

Usage: ads_encoded_dll_inject.py <PID> <Path To Encoded DLL> <Path to file to use for hiding>

Eg: ads_encoded_dll_inject.py 1111 C:\test\encoded.txt C:\Windows\explorer.exe


This project is for informational use only and so I can mess with Windows a little. Will clean up and rewrite the original code borrowed from Grey Hat Python eventually.
