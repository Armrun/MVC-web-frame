from models.base_model import SQLModel
from models.user_role import UserRole

import hashlib


class User(SQLModel):
    """
    User 是一个保存用户数据的 model
    现在只有两个属性 username 和 password
    """

    sql_create = '''
    CREATE TABLE `user` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `username` VARCHAR(45) NOT NULL,
        `password` CHAR(64) NOT NULL,
        `role` ENUM('guest', 'normal') NOT NULL,
        PRIMARY KEY (`id`)
    )'''

    def __init__(self, form):
        super().__init__(form)
        self.username = form['username']
        self.password = form['password']
        self.role = form.get('role', UserRole.normal)

    @staticmethod
    def guest():

        form = dict(
            role=UserRole.guest,
            username='【Guest】',
            password='【Guest】',
        )
        u = User(form)
        return u

    def is_guest(self):
        return self.role == UserRole.guest

    @staticmethod
    def salted_password(password, salt='$!@><?>HUI&DWQa`'):
        """$!@><?>HUI&DWQa`"""
        salted = password + salt
        hash = hashlib.sha256(salted.encode('ascii')).hexdigest()
        return hash

    @classmethod
    def login(cls, form):
        salted = cls.salted_password(form['password'])
        u = User.one(username=form['username'], password=salted)
        if u is not None:
            result = 'login successful'
            return u, result
        else:
            result = 'user name or password error'
            return User.guest(), result

    @classmethod
    def register(cls, form):
        valid = len(form['username']) > 2 and len(form['password']) > 2
        if valid:
            form['password'] = cls.salted_password(form['password'])
            form['role'] = "normal"
            u = User.new(form)
            result = 'Sign Up Successful<br> <pre>{}</pre>'.format(User.all())
            return u, result
        else:
            result = 'The length of user name of password must longer than 2'
            return User.guest(), result
