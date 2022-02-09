from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


CATEGORY_CHOICES = (
    ('Automotive', 'AUTOMOTIVE'),
    ('Beauty', 'BEAUTY'),
    ('Business', 'BUSINESS'),
    ('Engineering', 'ENGINEERING'),
    ('Entertainment', 'ENTERTAINMENT'),
    ('Financial', 'FINANCIAL'),
    ('Health', 'HEALTH'),
    ('History', 'HISTORY'),
    ('Language', 'LANGUAGE'),
    ('Politics', 'POLITICS'),
    ('Programming', 'PROGRAMMING'),
    ('Psychology', 'PYSCHOLOGY'),
    ('Residential Construction', 'RESIDENTIAL CONSTRUCTION'),
    ('Science', 'SCIENCE')
)

COLOR_CHOICES = (
    ('green', 'GREEN'),
    ('blue', 'BLUE'),
    ('red', 'RED'),
    ('grey', 'GREY'),
    ('black', 'BLACK'),
)

# Post = get_post_model()


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(
        max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(verbose_name="email address", unique=True)
    birth_date = models.DateField(verbose_name="DOB", null=True, blank=True)
    categories_verified = models.CharField(
        max_length=30, choices=CATEGORY_CHOICES, default='')
    color_iqroom = models.CharField(
        max_length=6, choices=COLOR_CHOICES, default='green')
    is_active = models.BooleanField(default=True)
    flag = models.IntegerField(
        choices=((1, 'Standard Account'), (2, 'Pro Account')), default=1)
    #user_doc = models.FileField(upload_to='media/files/', default='')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post_connected=self).count()
    # posts = models.ForeignKey(
    # get_post_model(), on_delete=models.CASCADE, blank=True, null=True)


class UserType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Color(models.Model):
    color = models.CharField(
        max_length=6, choices=COLOR_CHOICES, default='green')
