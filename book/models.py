from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField("نام خانوادگی", max_length=50)
    birthdate = models.DateField(null=True)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسنده‌"


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        "Author", on_delete=models.SET_NULL, null=True, verbose_name="نویسنده"
    )
    category = models.ForeignKey("Category", on_delete=models.PROTECT)
    published_day = models.DateField()
    pages = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}-{self.author}"
