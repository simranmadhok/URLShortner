from django.db import models

class OriginalURL(models.Model):
    """
        # Create an original url instance
        >>> original_url_obj = OriginalURL.objects.create(original_url="https://www.xyz.com")
    """
    original_url = models.CharField(
        max_length=500,
        primary_key=True,
    )

    def __str__(self):
        return self.original_url

    class Meta:
        """
        Declares a plural name for OriginalURL model
        """
        verbose_name_plural = 'Original URLS'
    

class URLid(models.Model):
    """
        # Create a url id instance
        >>> URLid.objects.create(original_url=original_url_obj, url_id=123224)
    """
    original_url = models.OneToOneField(
        OriginalURL,
        on_delete=models.CASCADE,
        primary_key=True
    )
    url_id = models.CharField(
        max_length=200
    )

    class Meta:
        """
        Declares a plural name for URLid model
        """
        verbose_name_plural = 'URLid'
