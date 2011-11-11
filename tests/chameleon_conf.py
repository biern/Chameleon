DATABASE = {
    'db': 'gekosale',
    'user': 'root',
    'passwd': '',
    'host': '',
    'port': 3306,
    'connect_timeout': 3,
}

try:
    from local_conf import DATABASE as LOCAL
    DATABASE.update(LOCAL)

except ImportError:
    raise Exception("local conf not found!!!1!11111")
