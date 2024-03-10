from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length = 50,null=True)
    last_name = models.CharField(max_length = 50,null=True)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length = 100)
    image = models.CharField(max_length = 100)
    date = models.DateField()
    excerpt = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    slug = models.SlugField(default = "",null=False)

    def __str__(self) :
        return f"{self.title}  ({self.date})"