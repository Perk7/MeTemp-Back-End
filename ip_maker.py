import socket 
from pathlib import Path

def make_env_ip():
     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     s.connect(("8.8.8.8", 80))
     
     Path('../.env').write_text( f'REACT_APP_SERVER={s.getsockname()[0]}')