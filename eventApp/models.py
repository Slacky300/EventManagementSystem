import random
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

class Venues(models.Model):


    typV = (
        ('WeddingAnniversary', 'Wedding Anniversary'),
        ('BirthDay Party','BirthDay Party'),
        ('Conference', 'Conference'),
        ('CelebrationParty','Celebration Party'),
    )

    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=300)
    img = models.ImageField(upload_to='venues/', null=True, blank=True)
    cpcty = models.PositiveIntegerField()
    mincpcty = models.PositiveIntegerField(blank=True,null=True)
    bkngPrice = models.PositiveIntegerField()
    rating = models.IntegerField(null=True, blank= True)
    areaSpecs = models.CharField(max_length=200)
    city = models.ForeignKey(City,on_delete=models.CASCADE,null=True,blank=True)
    address = models.CharField(max_length=400)
    availabililty = models.BooleanField(default=True)
    speciality = models.CharField(max_length=100,null=True,blank=True,choices=typV)
    slug = AutoSlugField(populate_from = 'name',unique=True,null=True,default=None,blank=True)
    mobNo = models.CharField(max_length=15,null=True,blank=True)
    srchDate = models.CharField(max_length=50,null=True,blank=True)
    owner = models.ForeignKey(UserAccount,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f'{self.name} Availaibility - {self.availabililty}'
    
    def get_absolute_url(self):

        return f'/venue/{self.slug}/'
    
    def crEvent(self):

        return f'/createEvent/{self.slug}/'
    
    def checkAvail(self):

        return f'/checkAvial/{self.slug}/'
    
    def goCrud(self):

        return f'/regClients/{self.slug}/'
    
    


class CreatEvent(models.Model):

    typ = (
        ('WeddingAnniversary', 'Wedding Anniversary'),
        ('BirthDay Party','BirthDay Party'),
        ('Conference', 'Conference'),
        ('CelebrationParty','Celebration Party'),
    )

    name = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    startDate = models.DateField(auto_now_add=False, auto_now=False)
    endDate = models.DateField(auto_now=False, auto_now_add=False)
    startTime = models.TimeField(auto_now=False,auto_now_add=False,null=True, blank=True)
    endTime = models.TimeField(auto_now=False,auto_now_add=False,null=True, blank=True)
    venue = models.ForeignKey(Venues,on_delete=models.CASCADE, null=True, blank=True)
    TicketPrice = models.PositiveIntegerField(null=True, blank=True)
    slug = AutoSlugField(populate_from = 'name',unique=True,null=True,default=None)
    img = models.ImageField(upload_to='event/' ,null=True, blank=True)
    eveTyp = models.CharField(choices=typ,null=True,blank=True,max_length=50)
    eveManager = models.ForeignKey(UserAccount, on_delete=models.CASCADE  ,null=True,blank=True)
    nGuest = models.PositiveIntegerField(null=True,blank=True)
    tBkngPrice = models.PositiveBigIntegerField(null=True,blank=True)
    status = models.BooleanField(null=True,blank=True,default=False)
    payDone = models.BooleanField(null=True,blank=True,default=False)

    

    def __str__(self):

        return f'{self.name} at {self.venue}'
    
    def getEdit(self):

        return f'/crudEdit/{self.slug}/'
    
    def cnfrmOrder(self):

        return f'/eventCnfrm/{self.slug}/'
    
    def payCr(self):

        return f'/payFor/{self.slug}/'
    
    def getBro(self):

        return f'/payStatus/{self.slug}/'
    
    def deleteIt(self):

        return f'/deletIt/{self.slug}/'
    
   
  



class Receipt(models.Model):


    def create_new_ref_number():
                not_unique = True
                while not_unique:
                    unique_ref = random.randint(1000000000, 9999999999)
                    if not Receipt.objects.filter(rcptNo=unique_ref):
                        not_unique = False
                return str(unique_ref)

    rcptFor = models.ForeignKey(UserAccount,on_delete=models.CASCADE,null=True,blank=True)
    rcptNo = models.CharField(default=create_new_ref_number,max_length=10)
    event = models.ForeignKey(CreatEvent,on_delete=models.CASCADE,null=True,blank=True)
    status = models.BooleanField(null=True,blank=True,default=False)
    rcptDate = models.DateField(auto_now=True,null=True,blank=True)


    def __str__(self):
        return f'{self.event} at {self.event.venue}'


    