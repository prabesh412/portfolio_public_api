from django.db import models
from datetime import timedelta
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    class Meta:
        abstract = True

class Skill(BaseModel):
    name = models.CharField(max_length = 200, unique=True)
    slug = models.CharField(max_length = 200, blank = True)

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Skill, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']


class Category(BaseModel):
    name = models.CharField(max_length = 200, unique=True)
    slug = models.CharField(max_length = 200, blank = True)

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']



class Portfolio(BaseModel):
    full_name = models.CharField(max_length = 50)
    phone_no = models.IntegerField(blank=True, default=0)
    portfolioParent = models.OneToOneField(User, on_delete = models.CASCADE)
    portfolioslug = models.CharField(max_length = 500, blank = True, default = None,)
    profile_pics = models.ImageField(upload_to="photos/")
    skills = models.ManyToManyField(Skill, blank=True, default = None)
    category = models.ManyToManyField(Category, blank=True)
    description = models.TextField(max_length = 500)

    def __str__(self):
        return self.full_name

    def save(self,*args, **kwargs):
        original_slug = slugify(self.full_name)
        queryset = Portfolio.objects.all().filter(portfolioslug__iexact=original_slug).count()
        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = Portfolio.objects.all().filter(portfolioslug__iexact=slug).count()
        self.portfolioslug = slug
        
        super(Portfolio, self).save(*args, **kwargs)


class Projects(BaseModel):
    title = models.CharField(max_length = 50)
    projectParent = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    project_pics = models.ImageField(upload_to="photos/")
    description = models.TextField(max_length = 500)

    def __str__(self):
        return self.title
