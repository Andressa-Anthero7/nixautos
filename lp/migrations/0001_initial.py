# Generated by Django 4.1.9 on 2023-06-22 00:53

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empreendimento_relacionado', models.CharField(max_length=50)),
                ('imagens', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[1440, 480], upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='ItemEmprrendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empreendimento_relacinado', models.CharField(max_length=50)),
                ('item_empreendimento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LandingPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empreendimento', models.CharField(max_length=50)),
                ('localizacao', models.CharField(max_length=256)),
                ('tag_meta', models.CharField(max_length=256)),
                ('tag_google', models.CharField(max_length=256)),
                ('user_cadastramento', models.CharField(max_length=50)),
                ('data_cadastramento', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_leads', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('whatsapp', models.CharField(max_length=13)),
                ('status_aberto', models.CharField(max_length=20)),
                ('status_leads', models.CharField(max_length=8)),
                ('data_recebimento', models.CharField(max_length=50)),
                ('ultimo_user', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_vinculado', models.CharField(max_length=50)),
                ('img_perfil', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[150, 150], upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='TagGoogle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editado_por', models.CharField(max_length=50)),
                ('data_atualizacao', models.CharField(max_length=15)),
                ('tag_google', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Tagmeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editado_por', models.CharField(max_length=50)),
                ('data_atualizacao', models.CharField(max_length=15)),
                ('tag_meta', models.CharField(max_length=256)),
            ],
        ),
    ]
