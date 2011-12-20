DATABASE = {
    'db': 'gekosale',
    'user': 'root',
    'passwd': '',
    'host': '',
    'port': 3306,
    'connect_timeout': 3,
}

DEFAULT_ARGS = {
    'userid': 1,
    'languageid': 1,
    }

try:
    from local_conf import DATABASE as LOCAL
    DATABASE.update(LOCAL)

    from local_conf import DEFAULT_ARGS as LOCAL_DEF_ARGS
    DEFAULT_ARGS.update(LOCAL_DEF_ARGS)

except ImportError:
    raise Exception("local conf not found!!!1!11111")
