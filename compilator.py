from cx_Freeze import setup, Executable 
  
setup(name = "ShellTest" , 
      version = "0.1" , 
      description = "AA" , 
      executables = [Executable("shell.py",base="Win32GUI")]) 
