from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image
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

    @property
    def cover_preview(self):
        if self.cover:
            return mark_safe("<img src='/Images/{}' width='300' height='250'>".format(self.cover))
        return ""
    
    def save(self):
        super().save()  # saving image first

        img = Image.open(self.cover.path) # Open image using self

        if img.height > 720 or img.width > 1280:
            new_img = (720, 720)
            img.thumbnail(new_img)
            img.save(self.cover.path)  # saving image at the same path
