from django.db import models
from .validators import validate_timestamp,validate_content
# Create your models here.


class Article(models.Model):
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="Author"
    )
    title = models.CharField(max_length=50, verbose_name="Title")
    content = models.TextField(verbose_name="Content",validators=[validate_content])
    
    timestamp = models.DateField(blank=True, null=True,validators=[validate_timestamp])

    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date",editable=False)
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} | id >> {self.id}"
    
    
def upload_to(instance, filename):
    return f"products/{instance.product.name}/{filename}"