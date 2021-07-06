from django.db import models
# Create your models here.
class User(models.Model):
    GENDER_CHOICES = (
        ("m", "male"),
        ("f", "female"),
        ("un", "unkhown")
    )
    username = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    fullname = models.CharField(max_length=100, blank=False)
    phonenumber = models.IntegerField(blank = True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, default="un")
    signing_date = models.DateTimeField()

    def change_username(self, new_username):
        self.username = new_username
        self.save()

    def change_password(self, new_password):
        self.password = new_password
        self.save()

    def change_email(self, new_email):
        self.email = new_email
        self.save()

    def change_fullname(self, new_fullname):
        self.fullname = new_fullname
        self.save()

    def change_phonenumber(self, new_phonenumber):
        self.phonenumber = new_phonenumber
        self.save()


class Post(models.Model):
    SUBJECTS = (
        ("T", "Tech"),
        ("S", "Sport"),
        ("M", "Music"),
        ("H", "History"),
        ("O", "Other"),
    )
    title = models.CharField(max_length=30, blank=False)
    subject = models.CharField(choices=SUBJECTS, max_length=10, default="O")
    image = models.ImageField()
    content = models.TextField(max_length=1000, blank=False)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def change_title(self, new_title):
        self.title = new_title
        self.save()

    def change_subject(self, new_subject):
        self.subject = new_subject
        self.save()

    def change_image(self, new_image):
        self.image = new_image
        self.save()

    def change_content(self, new_content):
        self.content = new_content
        self.save()