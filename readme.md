#require
- flask 2.2.2
- flask-cors 3.0.10
- Pymysql 1.0.2
- MariaDB 10.8.3(Use Mysql or MariaDB)
---
#config
로그찍히는곳
###flask.json
```
{
    "Key":Your Flask Secret Key
}
```
###sql.json
```
{
    "host": Your Server Host,
    "user": Your Server User,
    "password": Your Server Password,
    "db_name": Your Server DataBaseName,
    "charset" : Your Server Charset,
    "port" : Your Server Port(Mysql default : 3306)
}
```
---
