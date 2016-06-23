import sys  
   
from cx_Freeze import setup, Executable  
   
base = None  
if sys.platform == "win32":  
    base = "Win32GUI"  
   
setup(  
        name = "client",  
        version = "1.0",  
        description = "client tools",  
        executables = [Executable("main.py",base = base)])
