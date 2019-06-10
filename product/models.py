# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.safestring import mark_safe


STATUS_CHOICES = [
    ('', '--- select ---'),
    (1, 'Active'),
    (0, 'In Active'),
]

class Company(models.Model):
    companyid = models.AutoField(db_column='CompanyId', primary_key=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=200)  # Field name made lowercase.
    companylogo = models.CharField(db_column='CompanyLogo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    addeddate = models.DateTimeField(db_column='AddedDate')  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Company'

    def __str__(sef):        
        return sef.companyname

class Brand(models.Model):
    brandid = models.AutoField(db_column='BrandId', primary_key=True)  # Field name made lowercase.
    # companyid = models.IntegerField(db_column='CompanyId')  # Field name made lowercase.
    companyid = models.ForeignKey(Company,db_column='CompanyId',to_field='companyid',on_delete=models.DO_NOTHING)
    brandname = models.CharField(db_column='BrandName', max_length=200)  # Field name made lowercase.
    brandlogo = models.CharField(db_column='BrandLogo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status',choices=STATUS_CHOICES)  # Field name made lowercase.
    addeddate = models.DateTimeField(db_column='AddedDate')  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Brand'
    def __str__(self):
        return self.brandname

class Category(models.Model):
    categoryid = models.AutoField(db_column='CategoryId', primary_key=True)  # Field name made lowercase.
    industryid = models.IntegerField(db_column='IndustryId')  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=200)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentId')  # Field name made lowercase.
    categorylevel = models.IntegerField(db_column='CategoryLevel')  # Field name made lowercase.
    categoryicon = models.CharField(db_column='CategoryIcon', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categorytype = models.IntegerField(db_column='CategoryType')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    addeddate = models.DateTimeField(db_column='AddedDate')  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate')  # Field name made lowercase.
    categorycode = models.IntegerField(db_column='CategoryCode', blank=True, null=True)  # Field name made lowercase.
    foodcoupon = models.IntegerField(db_column='FoodCoupon', blank=True, null=True)  # Field name made lowercase.
    aliasname = models.CharField(db_column='AliasName', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    weightage = models.CharField(db_column='Weightage', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder', blank=True, null=True)  # Field name made lowercase.
    categorydepth = models.IntegerField(db_column='CategoryDepth', blank=True, null=True)  # Field name made lowercase.
    isb2b = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Category'
    def __str__(self):
        return self.categoryname

class City(models.Model):
    # stateid = models.IntegerField(db_column='StateId')  # Field name made lowercase.
    stateid = models.ForeignKey('self',on_delete=models.CASCADE,to_field='cityid',db_column='StateId')
    cityname = models.CharField(db_column='CityName', max_length=100)  # Field name made lowercase.
    citycode = models.CharField(db_column='CityCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status',choices=STATUS_CHOICES)  # Field name made lowercase.
    addeddate = models.DateTimeField(db_column='AddedDate')  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate')  # Field name made lowercase.
    cityid = models.AutoField(db_column='CityId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'City'


    def __str__(self):
        return self.cityname    


class Country(models.Model):
    countryid = models.AutoField(db_column='CountryId', primary_key=True)  # Field name made lowercase.
    countryname = models.CharField(db_column='CountryName', max_length=200)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=50)  # Field name made lowercase.
    countryflagimage = models.CharField(db_column='CountryFlagImage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    addeddate = models.DateTimeField(db_column='AddedDate')  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Country'


class Product(models.Model):
    productid = models.AutoField(db_column='ProductId', primary_key=True)  # Field name made lowercase.
    # brandid = models.IntegerField(db_column='BrandId')  # Field name made lowercase.
    brandid = models.ForeignKey(Brand,on_delete=models.DO_NOTHING, to_field='brandid',db_column="BrandId")
    # categoryid = models.IntegerField(db_column='CategoryId')  # Field name made lowercase.
    categoryid = models.ForeignKey(Category,on_delete=models.DO_NOTHING, to_field='categoryid', db_column='CategoryId')  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=500)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status',choices=STATUS_CHOICES)  # Field name made lowercase.
    addeddate = models.DateTimeField(db_column='AddedDate')  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate')  # Field name made lowercase.
    subsubcategoryid = models.IntegerField(db_column='SubSubCategoryId', blank=True, null=True)  # Field name made lowercase.
    source = models.IntegerField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    

    class Meta:
        managed = False
        db_table = 'Product'

    def __str__(self):
        return self.productname

    def __repr__(self):
        return self.productname        

    @property  # change admin name to 'name (website)'
    def category_name(self):
        return "%s" % (self.categoryid)

    # def __unicode__(self):
    #     return self.productname        

class Productbarcode(models.Model):
    productbarcodeid = models.AutoField(db_column='ProductBarcodeId', primary_key=True)  # Field name made lowercase.
    productskuid = models.IntegerField(db_column='ProductSKUId')  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    addeddate = models.DateTimeField(db_column='AddedDate')  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate')  # Field name made lowercase.
    source = models.IntegerField(blank=True, null=True)
    sourceinfo = models.CharField(max_length=3000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProductBarcode'


class Productsku(models.Model):
    productskuid = models.AutoField(db_column='ProductSKUId', primary_key=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductId')  # Field name made lowercase.
    productsku = models.CharField(db_column='ProductSKU', max_length=100)  # Field name made lowercase.
    productskuuqcid = models.IntegerField(db_column='ProductSKUUQCId')  # Field name made lowercase.
    productimage = models.CharField(db_column='ProductImage', max_length=200)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    addeddate = models.DateTimeField(db_column='AddedDate')  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate')  # Field name made lowercase.
    isrecommended = models.IntegerField(db_column='IsRecommended')  # Field name made lowercase.
    hsnc = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProductSKU'


class Productskupricestatewise(models.Model):
    productskupricestatewiseid = models.AutoField(db_column='ProductSKUPriceStatewiseId', primary_key=True)  # Field name made lowercase.
    stateid = models.IntegerField(db_column='StateId')  # Field name made lowercase.
    productskuid = models.IntegerField(db_column='ProductSKUId')  # Field name made lowercase.
    productmrp = models.DecimalField(db_column='ProductMRP', max_digits=7, decimal_places=2)  # Field name made lowercase.
    cessrate = models.IntegerField(db_column='CessRate')  # Field name made lowercase.
    addeddate = models.DateTimeField(db_column='AddedDate')  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate')  # Field name made lowercase.
    adcamount = models.DecimalField(db_column='ADCAmount', max_digits=7, decimal_places=5)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    hsncode = models.CharField(db_column='HSNCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cgstrate = models.DecimalField(db_column='CGSTRate', max_digits=4, decimal_places=2)  # Field name made lowercase.
    sgstrate = models.DecimalField(db_column='SGSTRate', max_digits=4, decimal_places=2)  # Field name made lowercase.
    igstrate = models.DecimalField(db_column='IGSTRate', max_digits=3, decimal_places=1)  # Field name made lowercase.
    exemptedflag = models.IntegerField(db_column='ExemptedFlag')  # Field name made lowercase.
    productsp = models.DecimalField(db_column='ProductSP', max_digits=14, decimal_places=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductSKUPriceStatewise'


class Productskuuqc(models.Model):
    productskuuqcid = models.AutoField(db_column='ProductSKUUQCId', primary_key=True)  # Field name made lowercase.
    productskuuqcfullname = models.CharField(db_column='ProductSKUUQCFullName', max_length=20)  # Field name made lowercase.
    productskuuqcshortname = models.CharField(db_column='ProductSKUUQCShortName', max_length=10)  # Field name made lowercase.
    addeddate = models.DateTimeField(db_column='AddedDate')  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate')  # Field name made lowercase.
    measurement = models.CharField(db_column='Measurement', max_length=100, blank=True, null=True)  # Field name made lowercase.
    level = models.IntegerField(db_column='Level', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductSKUUQC'

class ProductProduct(models.Model):
    name = models.CharField(db_column='Name', max_length=125)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product_product'


class Productskuprices(models.Model):
    productskupriceid = models.IntegerField()
    productskuid = models.IntegerField()
    programid = models.IntegerField()
    productmrp = models.DecimalField(max_digits=7, decimal_places=2)
    productsp = models.DecimalField(max_digits=7, decimal_places=2)
    taxaggregationid = models.IntegerField()
    status = models.IntegerField()
    addeddate = models.DateTimeField()
    lastupdateddate = models.DateTimeField()
    productbarcodeid = models.IntegerField(blank=True, null=True)
    adcamount = models.IntegerField(blank=True, null=True)
    channel = models.IntegerField()
    productpp = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'productskuprices'





