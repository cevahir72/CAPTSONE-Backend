from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.author.id, filename)



class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural= "Categories"
        
    def __str__(self):
        return self.name


class Post(models.Model):
    OPTIONS= (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    
    title= models.CharField(max_length=100)
    content= models.TextField()
    image= models.ImageField(upload_to=user_directory_path, blank=True)
    category= models.ForeignKey(Category,on_delete=models.PROTECT)
    # one-->many ilişkisi  
    publish_date= models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)  
    #User silinirse post da silinsin
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')  # Yukarıdaki OPTIONS daki verileriş Dropdown menu yapıyor
    slug =models.SlugField(blank=True, unique=True)   # "how-to-learn-django" aralarına -  koyuyor
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # user silindiği zaman ona ait commentler de silinsin
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content= models.TextField()
    
    
    def __str__(self):
        return self.user.username

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # user silindiği zaman ona ait likelar  da silinsin
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

