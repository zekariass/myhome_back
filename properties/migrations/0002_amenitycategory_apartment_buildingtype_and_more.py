# Generated by Django 4.0.3 on 2022-03-25 16:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import properties.models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0001_initial'),
        ('agents', '0001_initial'),
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmenityCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='category name')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='properties.property')),
                ('storey', models.IntegerField(default=0, verbose_name='apartment storey level')),
                ('is_new', models.BooleanField(blank=True, default=False, verbose_name='is property new?')),
            ],
            bases=('properties.property',),
        ),
        migrations.CreateModel(
            name='BuildingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommercialProperty',
            fields=[
                ('property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='properties.property')),
                ('storey', models.IntegerField(default=0, verbose_name='commercial property storey level')),
                ('is_new', models.BooleanField(default=False, verbose_name='is the commercial property new?')),
                ('building_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commercial_properties', to='properties.buildingtype', verbose_name='commercial property building type')),
            ],
            bases=('properties.property',),
        ),
        migrations.CreateModel(
            name='Condominium',
            fields=[
                ('property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='properties.property')),
                ('number_of_rooms', models.IntegerField(default=1)),
                ('number_of_bed_rooms', models.IntegerField(default=1)),
                ('storey', models.IntegerField(default=0, verbose_name='condominium storey level')),
                ('num_of_baths', models.IntegerField(default=1)),
                ('area', models.FloatField(default=0.0)),
                ('is_furnished', models.BooleanField(default=False, verbose_name='is the condominium furnished?')),
                ('is_new', models.BooleanField(default=False, verbose_name='is the condominium new?')),
            ],
            bases=('properties.property',),
        ),
        migrations.CreateModel(
            name='EducationFacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='education facility name')),
                ('ownership', models.CharField(choices=[('PRIVATE', 'Private'), ('PUBLIC', 'Public'), ('NGO', 'NGO'), ('OTHER', 'Other')], default=['PUBLIC'], max_length=50, verbose_name='who own the education facility?')),
                ('distance_from_property', models.FloatField(default=0.0, verbose_name='how far is from property')),
                ('distance_unit', models.CharField(choices=[('METER', 'Meter'), ('KM', 'Kilo Meter'), ('MILE', 'Mile')], default='KM', max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('added_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='EdufaLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=50, verbose_name='education level')),
                ('grade_start', models.CharField(max_length=20, verbose_name='start of grade')),
                ('grade_end', models.CharField(blank=True, max_length=20, null=True, verbose_name='end of grade')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='properties.property')),
                ('area', models.FloatField(default=0.0, verbose_name='area of the land')),
                ('length', models.FloatField(default=0.0, verbose_name='length of the land')),
                ('width', models.FloatField(default=0.0, verbose_name='width of the land')),
                ('has_plan', models.BooleanField(default=True, verbose_name='the land has plan?')),
                ('has_debt', models.BooleanField(default=False, verbose_name='the land has unpaid debt?')),
            ],
            bases=('properties.property',),
        ),
        migrations.CreateModel(
            name='POICategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='POI category name')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='point of interest name')),
                ('description', models.TextField(blank=True, null=True)),
                ('distance_from_property', models.FloatField(default=0.0)),
                ('distance_unit', models.CharField(choices=[('METER', 'Meter'), ('KM', 'Kilo Meter'), ('MILE', 'Mile')], default='KM', max_length=20)),
                ('added_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('poi_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='properties.poicategory', verbose_name='point of interest category')),
            ],
        ),
        migrations.CreateModel(
            name='TraditionalHome',
            fields=[
                ('property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='properties.property')),
                ('number_of_rooms', models.IntegerField(default=1)),
                ('number_of_bed_rooms', models.IntegerField(default=1)),
                ('storey', models.IntegerField(default=0, verbose_name='Home storey level')),
                ('num_of_baths', models.IntegerField(default=1)),
                ('area', models.FloatField(default=0.0)),
                ('is_furnished', models.BooleanField(default=False, verbose_name='is the home furnished?')),
                ('is_new', models.BooleanField(default=False, verbose_name='is the home new?')),
            ],
            bases=('properties.property',),
        ),
        migrations.CreateModel(
            name='TransFaCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='transportation facility category name')),
                ('facility_type', models.CharField(choices=[('BUS_STOP', 'Bus Stop'), ('TRAIN_STATION', 'Train Station'), ('TRAM_STOP', 'Tram Stop'), ('METER_TAXI', 'Meter Taxi'), ('OTHER', 'Other')], default='BUS_STOP', max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VersatilePropertyUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storey', models.IntegerField(default=0, verbose_name='versatile unit storey level')),
                ('number_of_rooms', models.IntegerField(default=1)),
                ('area', models.FloatField(default=0.0)),
                ('vers_prop_unit_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Villa',
            fields=[
                ('property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='properties.property')),
                ('number_of_rooms', models.IntegerField(default=1)),
                ('number_of_bed_rooms', models.IntegerField(default=1)),
                ('storey', models.IntegerField(default=0, verbose_name='How many storey it has')),
                ('num_of_baths', models.IntegerField(default=1)),
                ('total_coumpound_area', models.FloatField(default=0.0)),
                ('housing_area', models.FloatField(default=0.0)),
                ('is_furnished', models.BooleanField(default=False, verbose_name='is the villa furnished?')),
                ('is_new', models.BooleanField(default=False, verbose_name='is the villa new?')),
            ],
            bases=('properties.property',),
        ),
        migrations.RemoveField(
            model_name='property',
            name='propertyCategory',
        ),
        migrations.AddField(
            model_name='property',
            name='added_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='property added on date'),
        ),
        migrations.AddField(
            model_name='property',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='commons.address', verbose_name='property address'),
        ),
        migrations.AddField(
            model_name='property',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent_properties', to='agents.agent', verbose_name='property agent'),
        ),
        migrations.AddField(
            model_name='property',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='property description'),
        ),
        migrations.AddField(
            model_name='property',
            name='is_residential',
            field=models.BooleanField(default=True, verbose_name='is property for residence?'),
        ),
        migrations.AddField(
            model_name='property',
            name='property_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_properties', to='properties.propertycategory'),
        ),
        migrations.AddField(
            model_name='propertycategory',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='propertycategory',
            name='description',
            field=models.TextField(verbose_name='property category description'),
        ),
        migrations.AlterField(
            model_name='propertycategory',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='property category name'),
        ),
        migrations.CreateModel(
            name='VersatileProperty',
            fields=[
                ('property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='properties.property')),
                ('vers_prop_description', models.TextField(blank=True, null=True)),
                ('best_category_for', models.ManyToManyField(to='properties.propertycategory', verbose_name='is is used for?')),
            ],
            bases=('properties.property',),
        ),
        migrations.CreateModel(
            name='TransportFacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='transportation facility name')),
                ('distance_from_property', models.FloatField(default=0.0, verbose_name='how far is from property')),
                ('distance_unit', models.CharField(choices=[('METER', 'Meter'), ('KM', 'Kilo Meter'), ('MILE', 'Mile')], default='KM', max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('trans_fa_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.transfacategory', verbose_name='transportation facility category')),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='rule title')),
                ('description', models.TextField(blank=True, null=True)),
                ('strictness', models.CharField(choices=[('LOWER', 'Lower'), ('MEDIUM', 'Medium'), ('HIGH', 'High'), ('VERY_HIGH', 'Very High')], default='MEDIUM', max_length=100, verbose_name='how strict is the rule?')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyVirtualVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('virtual_video', models.FileField(upload_to=properties.models.get_property_virtual_file_name, verbose_name='property virtual video')),
                ('uploaded_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('property', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=properties.models.get_property_video_name, verbose_name='property video')),
                ('uploaded_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('property', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyUniqueFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='feature name')),
                ('description', models.TextField(blank=True, null=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyTransFacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
                ('transport_facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.transportfacility')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyPOI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('point_of_interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.pointofinterest')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=properties.models.get_property_image_name, verbose_name='property image')),
                ('uploaded_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyEduFacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('education_facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.educationfacility')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='properties.property')),
                ('storey', models.IntegerField(default=0, verbose_name='office storey level')),
                ('number_of_rooms', models.IntegerField(default=1)),
                ('area', models.FloatField(default=0.0)),
                ('is_furnished', models.BooleanField(default=False, verbose_name='is the home furnished?')),
                ('is_new', models.BooleanField(default=False, verbose_name='is the office new?')),
                ('building_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='officess', to='properties.buildingtype', verbose_name='office building type')),
            ],
            bases=('properties.property',),
        ),
        migrations.CreateModel(
            name='ListingPriceByCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_label', models.CharField(max_length=100, verbose_name='label (name) for this pricing')),
                ('price', models.FloatField(default=0.0, verbose_name='listing price')),
                ('description', models.TextField(blank=True, null=True)),
                ('Added_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('expired_on', models.DateTimeField(blank=True, null=True)),
                ('property_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_listing_price', to='properties.propertycategory')),
            ],
        ),
        migrations.CreateModel(
            name='ListingDiscountByCategoryHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_percentage', models.FloatField(default=0.0, verbose_name='listing discount by percentage')),
                ('discount_fixed', models.FloatField(default=0.0, verbose_name='listing discount fixed')),
                ('description', models.TextField(blank=True, null=True)),
                ('discount_start_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='when the discount starts')),
                ('expired_on', models.DateTimeField(blank=True, null=True)),
                ('property_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_discount_history', to='properties.propertycategory')),
            ],
        ),
        migrations.CreateModel(
            name='ListingDiscountByCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_percentage', models.FloatField(default=0.0, verbose_name='listing discount by percentage')),
                ('discount_fixed', models.FloatField(default=0.0, verbose_name='listing discount fixed')),
                ('description', models.TextField(blank=True, null=True)),
                ('discount_start_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='when the discount starts')),
                ('expired_on', models.DateTimeField(blank=True, null=True)),
                ('property_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_discount', to='properties.propertycategory')),
            ],
        ),
        migrations.AddField(
            model_name='educationfacility',
            name='edufa_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.edufalevel', verbose_name='education facility level'),
        ),
        migrations.CreateModel(
            name='CommercialPropertyUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_rooms', models.IntegerField(default=1)),
                ('area', models.FloatField(default=0.0, verbose_name='total area of the unit')),
                ('com_prop_unit_description', models.TextField()),
                ('commercial_property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='single_commercial_units', to='properties.commercialproperty', verbose_name='parent commecrial property')),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_rooms', models.IntegerField(default=1)),
                ('number_of_bed_rooms', models.IntegerField(default=1)),
                ('number_of_baths', models.IntegerField(default=1)),
                ('area', models.FloatField(default=0.0)),
                ('is_furnished', models.BooleanField(default=False, verbose_name='is apartment unit furnished?')),
                ('is_available', models.BooleanField(default=True, verbose_name='is apartment available?')),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartment_units', to='properties.apartment', verbose_name='parent apartment')),
            ],
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='amenity name')),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenities', to='properties.amenitycategory')),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='Point_of_interest',
            field=models.ManyToManyField(related_name='poi_near_by_properties', through='properties.PropertyPOI', to='properties.pointofinterest'),
        ),
        migrations.AddField(
            model_name='property',
            name='TransportFacility',
            field=models.ManyToManyField(related_name='tran_near_by_properties', through='properties.PropertyTransFacility', to='properties.transportfacility'),
        ),
        migrations.AddField(
            model_name='property',
            name='amenity',
            field=models.ManyToManyField(related_name='linked_properties', to='properties.amenity'),
        ),
        migrations.AddField(
            model_name='property',
            name='education_facility',
            field=models.ManyToManyField(related_name='edu_near_by_properties', through='properties.PropertyEduFacility', to='properties.educationfacility'),
        ),
    ]
