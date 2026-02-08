import pymysql

# "Lie" to Django and say we are version 2.2.7
pymysql.version_info = (2, 2, 7, "final", 0)

pymysql.install_as_MySQLdb()