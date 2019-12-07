import socket

class Connection:

    def has_internet_access():
        try:
            host = socket.gethostbyname(cfg.url_check_connection)
            s = socket.create_connection((host, 80), 2)
            return True
        return False
