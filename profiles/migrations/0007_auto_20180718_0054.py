# Generated by Django 2.0 on 2018-07-18 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20180618_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorprofile',
            name='sector',
            field=models.CharField(choices=[('Agriculture', (('as', 'Agri-Services'), ('at', 'Agri-tech'), ('bk', 'Beauty/Skincare'), ('br', 'Beverages'), ('fu', 'Foodstuffs'), ('fd', 'Restaurant/ Food Retail/ Catering'))), ('Alternative Energy', (('ap', 'Appliances'), ('be', 'Biofuel/Ethanol'), ('co', 'Cooking Energy'), ('ha', 'HVAC Systems'), ('oh', 'Other'), ('se', 'Solar Electricity'), ('sw', 'Solar Water Pumps'))), ('Business Services', (('cl', 'Consulting Services'), ('fn', 'Financing/ Financial Services'), ('hr', 'Human Resources'), ('sp', 'Office Space/ Shared Workspace'))), ('Craft', (('ac', 'Accessories'), ('at', 'Art'), ('ct', 'Clothing'), ('fw', 'Footwear'), ('fd', 'Furniture/décor'), ('hc', 'Handicrafts'), ('jl', 'Jewelry'))), ('Education', (('bo', 'Books'), ('pe', 'Child Care/ primary education'), ('he', 'Higher Education'), ('pu', 'Publishing'), ('st', 'Skills Training'), ('vt', 'Vocational Training'))), ('Other', (('bm', 'BMO'), ('cn', 'Construction Services'), ('py', 'Property & Development'))), ('Services', (('or', 'Other'),)), ('Technology', (('ec', 'E-Commerce'), ('it', 'IT'), ('mm', 'Multimedia'), ('op', 'Online Payments'), ('ot', 'Other'), ('sc', 'Security'), ('sr', 'Software'))), ('Tourism', (('ld', 'House Lodging'), ('lf', 'Lodging and Food'))), ('Accomodation & Food Services', (('hotels', 'Hotels'), ('restaurants', 'Restaurants'), ('catering', 'Catering'), ('bakery', 'Bakery'), ('delivery', 'Food Delivery'))), ('Waste - Health - Hygiene', (('hg', 'Hygiene'), ('rg', 'Recycling'), ('we', 'Waste Management'), ('wr', 'Water')))], max_length=50),
        ),
        migrations.AlterField(
            model_name='smeprofile',
            name='sector',
            field=models.CharField(choices=[('Agriculture', (('as', 'Agri-Services'), ('at', 'Agri-tech'), ('bk', 'Beauty/Skincare'), ('br', 'Beverages'), ('fu', 'Foodstuffs'), ('fd', 'Restaurant/ Food Retail/ Catering'))), ('Alternative Energy', (('ap', 'Appliances'), ('be', 'Biofuel/Ethanol'), ('co', 'Cooking Energy'), ('ha', 'HVAC Systems'), ('oh', 'Other'), ('se', 'Solar Electricity'), ('sw', 'Solar Water Pumps'))), ('Business Services', (('cl', 'Consulting Services'), ('fn', 'Financing/ Financial Services'), ('hr', 'Human Resources'), ('sp', 'Office Space/ Shared Workspace'))), ('Craft', (('ac', 'Accessories'), ('at', 'Art'), ('ct', 'Clothing'), ('fw', 'Footwear'), ('fd', 'Furniture/décor'), ('hc', 'Handicrafts'), ('jl', 'Jewelry'))), ('Education', (('bo', 'Books'), ('pe', 'Child Care/ primary education'), ('he', 'Higher Education'), ('pu', 'Publishing'), ('st', 'Skills Training'), ('vt', 'Vocational Training'))), ('Other', (('bm', 'BMO'), ('cn', 'Construction Services'), ('py', 'Property & Development'))), ('Services', (('or', 'Other'),)), ('Technology', (('ec', 'E-Commerce'), ('it', 'IT'), ('mm', 'Multimedia'), ('op', 'Online Payments'), ('ot', 'Other'), ('sc', 'Security'), ('sr', 'Software'))), ('Tourism', (('ld', 'House Lodging'), ('lf', 'Lodging and Food'))), ('Accomodation & Food Services', (('hotels', 'Hotels'), ('restaurants', 'Restaurants'), ('catering', 'Catering'), ('bakery', 'Bakery'), ('delivery', 'Food Delivery'))), ('Waste - Health - Hygiene', (('hg', 'Hygiene'), ('rg', 'Recycling'), ('we', 'Waste Management'), ('wr', 'Water')))], max_length=50),
        ),
    ]
