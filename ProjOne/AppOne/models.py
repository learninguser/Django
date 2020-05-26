from django.db import models

# Blog:
# 1. Title 
# 2. Category 
# 3. Image 
# 4. Content 
# 5. Author 
# 6. Status Draft/Published 
# 7. Published Date 
# 8. Author Description 
# 9. Category description

# Create your models here.
class Blog(models.Model):

    statuses = [('D',"Drafts"), ('P',"Published")]
    title = models.CharField(max_length=256, null=False)
    content = models.TextField(null=True)
    author = models.CharField(max_length=128, unique=True, default='')
    status = models.CharField(max_length=1,choices=statuses,default="D")


    def __str__(self):
        return self.title