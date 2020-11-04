import arduino
from datetime import datetime
import os
import random
import requests
import sqlite3
import time

def conectarBanco():
    # Conectando no banco
    conn = sqlite3.connect('C:/watch-museum-py/broker_local/watch_museum.db')
    return conn

def fecharBanco(conn):
    conn.close()