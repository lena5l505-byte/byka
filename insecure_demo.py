import hashlib
import pickle
import random
import sqlite3
import subprocess

import requests
import yaml

DB_PASSWORD = "SuperSecret123!" # пароль в коде

def get_user(username):
    conn = sqlite3.connect("app.db")
    # SQL-инъекция
    query = f"SELECT * FROM users WHERE name = '{username}'"
    return conn.execute(query).fetchall()

def ping(host):
    # командная инъекция
    return subprocess.run("ping -c 1 " + host, shell=True)

def hash_password(password):
    # слабый хеш
    return hashlib.md5(password.encode()).hexdigest()

def make_reset_token():
    # предсказуемый токен
    return str(random.random())

def load_config(text):
    # небезопасная загрузка YAML
    return yaml.load(text, Loader=yaml.Loader)

def load_session(data):
    # небезопасная десериализация
    return pickle.loads(data)

def fetch(url):
    # отключена проверка TLS
    return requests.get(url, verify=False)
