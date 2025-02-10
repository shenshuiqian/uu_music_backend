### 数据库配置：

（1）在MySQL中创建数据库

```sql
CREATE DATABASE 数据库名;
```



（2）setting.py

```python
#将DATABASES修改为
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": <(1)中创建的数据库名>,
        "USER": <MySQL用户名>,
        "PASSWORD": <MySQL密码>,
        "HOST": <用户的主机地址>,
        "PORT": <用户的端口号>,
    }
}
```

例如：

```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "uu_music",
        "USER": "root",
        "PASSWORD": "abc",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```



（3）数据库迁移

```cmd
python manage.py makemigrations

python manage.py migrate
```

在新建的数据库中建立一个名称为user-info的表

（4）运行django

```cmd
python manage.py runserver
```

