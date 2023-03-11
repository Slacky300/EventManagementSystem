from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from autoslug import AutoSlugField
# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password = None):
        if not email:
            raise ValueError('User must provide a email')
        
        user = self.model(
            email = email,
            name = name
        )


        user.set_password(password)
        user.save(using = self._db)

        return user


    def xUser(self, email, name, password = None):
        user = self.create_user(email,name,password)

        user.is_mod = True
        user.is_nUser = True
        user.is_staff = False
        user.save(using = self._db)

        return user

    def create_superuser(self, email, name, password = None):
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.is_nUser = False
        user.is_mod = False

        user.save(using = self._db)

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length = 50,unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_xUser = models.BooleanField(default=False)
    is_nUser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name


class City(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class EventPlace(models.Model):

    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=300)
    img = models.ImageField(upload_to='venues/', null=True, blank=True)
    cpcty = models.PositiveIntegerField()
    bkngPrice = models.PositiveIntegerField()
    rating = models.IntegerField(null=True, blank= True)
    areaSpecs = models.CharField(max_length=200)
    city = models.ForeignKey(City,on_delete=models.CASCADE,null=True,blank=True)
    address = models.CharField(max_length=400)
    availabililty = models.BooleanField(default=True)
    slug = AutoSlugField(populate_from = 'name',unique=True,null=True,default=None,blank=True)

    def __str__(self):
        return f'{self.name} + Availaibility - {self.availabililty}'


class CreatEvent(models.Model):

    typ = (
        ('WeddingAnniversary', 'Wedding Anniversary'),
        ('BirthDay Party','BirthDay Party'),
        ('Conference', 'Conference'),
        ('CelebrationParty','Celebration Party'),
    )

    name = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    startDate = models.DateTimeField(auto_now_add=False, auto_now=False)
    endDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    venue = models.ForeignKey(EventPlace,on_delete=models.CASCADE, null=True, blank=True)
    TicketPrice = models.PositiveIntegerField(null=True, blank=True)
    slug = AutoSlugField(populate_from = 'name',unique=True,null=True,default=None)
    img = models.ImageField(upload_to='event/' ,null=True, blank=True)
    eveTyp = models.CharField(choices=typ,null=True,blank=True,max_length=50)
    eveManager = models.ForeignKey(UserAccount, on_delete=models.CASCADE  ,null=True,blank=True)

    def __str__(self):

        return f'{self.name} at {self.venue}'
    
  

