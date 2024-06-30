from django.db import models

# Create your models here.

class tipo_producto(models.Model):
    product_type_id = models.AutoField(db_column='product_type_id', primary_key=True)
    product_type = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.product_type)
    
class Producto(models.Model):
    product_name = models.CharField('Nombre del Producto', max_length=400)
    precio = models.IntegerField('Precio Actual del Producto', default=0)
    stock = models.IntegerField('Stock restante del producto', default=0)
    prduct_type_id = models.ForeignKey('tipo_producto',on_delete=models.CASCADE, db_column='product_type_id')
    product_id = models.IntegerField('Id del producto', primary_key=True, default='0')
    product_img = models.ImageField('Imagen del producto', upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.product_name