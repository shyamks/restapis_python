from django.db import models


# class Reporter(models.Model):
#     full_name = models.CharField(max_length=70)
#
#     def __str__(self):              # __unicode__ on Python 2
#         return self.full_name

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    pub_date = models.DateField(default=None,null=True)
    dat = models.DateField(default=None,null=True)
    headline = models.CharField(max_length=200,null=True)
    content = models.TextField(default=None,null=True)

    # reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    class Meta:
        managed = True
        db_table = 'article'

    def __str__(self):  # __unicode__ on Python 2
        return self.headline
