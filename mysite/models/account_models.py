from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# BaseUserManager を継承している
class UserManager(BaseUserManager):

    def create_user(self, email, password=None):  # 一般 user の登録. email check, password, save
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):  # 管理者(superuser) を作成する時にこの method が適用される
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True  # ここで superuser 権限の付与
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):  # DataBase の column(列) の定義
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    # アカウントが有効かどうかの判断。user 登録が完了したら有効なので、True
    is_active = models.BooleanField(default=True)
    # 管理画面に入れるかどうか。管理者かどうか。一般 user が入れてはいけないので、 False
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    # 標準で備わっているもの。email に設定
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


# ------- One To One Field　を同時に作成 -------


@receiver(post_save, sender=User)  # user を作成した直後に profile model も作成される(呼び出される)
def create_onetoone(sender, **kwargs):  # 先に profile を作成することはできない。user があって初めて prlfile が作成される
    if kwargs['created']:
        from mysite.models.profile_models import Profile
        Profile.objects.create(user=kwargs['instance'])

# ------- One To One Field　を同時に作成 -------
