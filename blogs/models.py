from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


STATUS = (
    (0, "Draft"),
    (1, "Published")
)

class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    cover = models.ImageField(upload_to="Uploaded/")
    content = RichTextUploadingField(blank=True, null=True)
    sticker = models.CharField(max_length=50, unique=False, null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = models.CharField(max_length=400, null=True, blank=True)

    class Meta:
        ordering = ['-published_at']

    # def image_tag(self):
    #     return format_html("<img src='/Media/{}'".format(self.cover))

    def __str__(self):
        return self.title

    