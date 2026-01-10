"""Module to test the internet connection."""

import socket

def test_connection() -> bool:
    """Tests internet connection trying to connect with google servers.

    Returns:
        bool: True if there is internet connection and false if there is not internet connection.
    """
    try:
        socket.create_connection(("google.com", 80))
        return True
    except OSError:
        print("No internet connection, please connect to the internet and try again.")
        return False
