import socket

def test_conection():
    try:
        socket.create_connection(("google.com", 80))
        return True
    except OSError:
        print("No internet connection, please connect to the internet and try again.")
        return False