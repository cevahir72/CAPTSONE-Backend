from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.author.id, filename)




class Post(models.Model):
    OPTIONS= [
        ('d', 'Draft'),
        ('p', 'Published')
    ]
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')  # Yukarıdaki OPTIONS daki verileriş Dropdown menu yapıyor
    title= models.CharField(max_length=100)
    content= models.TextField(max_length=1000)
    image= models.ImageField(upload_to=user_directory_path, blank=True) 
    publish_date= models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)  
    #User silinirse post da silinsin
    POST_CATEGORY_CHOICES = [
        ('Javascript', 'Javascript'),
        ('Python', 'Python'),
        ('SAAS', 'SAAS'),
        ('HTML', 'HTML'),
        ('REACT-JS', 'REACT-JS'),
        ('Django', 'Django'),
        ('CSS', 'CSS')
    ]
    category= models.CharField(max_length=20, choices=POST_CATEGORY_CHOICES)
    # one-->many ilişkisi
    slug =models.SlugField(blank=True, unique=True)   # "how-to-learn-django" aralarına -  koyuyor
    
    def __str__(self):
        return f"{self.user} {self.title} {self.content}"
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ="comments")  # user silindiği zaman ona ait commentler de silinsin
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content= models.TextField()
    createdDate = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.user} {self.content}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # user silindiği zaman ona ait likelar  da silinsin
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = "likes")
    createdDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} {self.post}"
    
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = "views")  
    createdDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} {self.post}"

