from django.db import models
from django.core.validators import FileExtensionValidator, RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Solo están permitidos los caracteres alfanuméricos.')

# Create your models here.
class Client(models.Model):
    ruc = models.IntegerField()
    nombre_comercial = models.CharField(max_length=60)
    razon_social = models.CharField(max_length=60)
    direccion_social = models.CharField(max_length=80)
    tipo_via = models.CharField(max_length=28)
    referencia_social = models.CharField(max_length=80)
    nro_dpto = models.CharField(max_length=21)
    dpto = models.CharField(max_length=49)
    prov = models.CharField(max_length=49)
    dist = models.CharField(max_length=49)
    first_name = models.CharField(max_length=28)
    last_name = models.CharField(max_length=28)
    middle_name = models.CharField(max_length=28)
    email = models.EmailField()
    phone = models.IntegerField()
    job_title = models.CharField(max_length=35)
    password = models.CharField(max_length=35)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Brand(models.Model):
    name = models.CharField(max_length=41)
    logo = models.FileField(
        upload_to='static/images/brands/logos', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'svg'])]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.ForeignKey(
        "Brand",
        on_delete=models.CASCADE,
        related_name='brands'
    )
    name = models.CharField(max_length=140)
    code = models.CharField(max_length=35)
    price_no_offer = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.ImageField(upload_to='static/images/products/pictures', null=True, blank=True)
    description = models.TextField()
    stock = models.IntegerField()
    idSystem = models.ForeignKey(
        "System",
        on_delete=models.SET_NULL,
        related_name="systems",
        null=True,
        blank=True
    )
    idSubsystem = models.ForeignKey(
        "Subsystem",
        on_delete=models.SET_NULL,
        related_name="subsystems",
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.price} - {self.stock}"


class Reason(models.Model):
    text = models.TextField()
    icon = models.FileField(
        upload_to='static/images/reasons/icons', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'svg'])]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class BannerDestacado(models.Model):
    image = models.ImageField(upload_to='static/images/banners/destacado')
    background = models.ImageField(upload_to='static/images/banners/destacado')
    title = models.CharField(max_length=70)
    subtitle = models.CharField(max_length=70)
    description = models.TextField()
    link_title = models.CharField(max_length=70)
    link = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BannerA(models.Model):
    image = models.ImageField(upload_to='static/images/banners/a')
    background = models.ImageField(upload_to='static/images/banners/a')
    title = models.CharField(max_length=70)
    description = models.TextField()
    link_title = models.CharField(max_length=70)
    link = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TipoVia(models.Model):
    name = models.CharField(max_length=35)
    code = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.name} - {self.code}"


class JobTitle(models.Model):
    name = models.CharField(max_length=140)

    def __str__(self):
        return f"{self.name}"


class PaymentMethod(models.Model):
    name = models.CharField(max_length=140)
    code = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.name} - {self.code}"


class CurrencyType(models.Model):
    name = models.CharField(max_length=70)
    symbol = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.name} - {self.symbol}"


class BankAccount(models.Model):
    number = models.CharField(max_length=140)
    bank_name = models.CharField(max_length=140)
    account_currency = models.ForeignKey(
        "CurrencyType",
        on_delete=models.CASCADE,
        related_name="currencies"
    )

    def __str__(self):
        return f"{self.bank_name} - {self.account_currency}"


class MenuCategory(models.Model):
    name = models.CharField(max_length=140)
    idMenuCategory = models.PositiveIntegerField()

    def __str__(self):
        return f"ID: {self.idMenuCategory} - {self.name}"


class MenuSubcategory(models.Model):
    name = models.CharField(max_length=140)
    idMenuSubcategory = models.PositiveIntegerField()
    idCategory = models.ForeignKey(
        "MenuCategory",
        on_delete=models.CASCADE,
        related_name="subcategories"
    )

    def __str__(self):
        return f"ID: {self.idCategory}{str(self.idMenuSubcategory)} - {self.name}"


class System(models.Model):
    name = models.CharField(max_length=140)

    def __str__(self):
        return f"{self.name}"


class Subsystem(models.Model):
    name = models.CharField(max_length=140)
    system = models.ForeignKey(
        System,
        on_delete=models.CASCADE,
        related_name="subsystems"
    )

    def __str__(self):
        return f"{self.name}"
