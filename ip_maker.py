import socket 
import subprocess
from pathlib import Path

def make_env_ip():
     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     s.connect(("8.8.8.8", 80))
     
     ip = s.getsockname()[0]
     
     Path('../.env').write_text( f'REACT_APP_SERVER={ip}')
     
     subprocess.run('rm *.crt & rm *.key & rm *.pem')
     subprocess.run(f'mkcert {ip}')
     subprocess.run(f'clear')