from django.db import models


# Create your models here.
class Contributor(models.Model):
    contributor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'contributors'
        verbose_name = 'Contributor'
        verbose_name_plural = 'Contributors'


class Apartment(models.Model):
    apartment_id = models.AutoField(primary_key=True)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'apartments'
        verbose_name = 'Apartment'
        verbose_name_plural = 'Apartments'


# class Contributors_Apartment(models.Model):
#     contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
#     apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.apartment, self.contributor
    #
    # class Meta:
    #     db_table = 'contributors_apartment'
    #     verbose_name = 'Contributor Apartment'
    #     verbose_name_plural = 'Contributor Apartments'