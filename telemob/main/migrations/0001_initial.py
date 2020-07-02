# Generated by Django 3.0.8 on 2020-07-02 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome da Campanha')),
                ('description', models.TextField(verbose_name='Descrição da Campanha')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('last_updated', models.DateField(auto_now=True, verbose_name='Última atualização em')),
            ],
            options={
                'verbose_name': 'Campanha',
            },
        ),
        migrations.CreateModel(
            name='Politician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
                ('parliamentary_name', models.CharField(max_length=150, verbose_name='Nome Parlamentar')),
                ('political_party', models.CharField(choices=[('PMDB', 'PMDB - Partido Do Movimento Democrático Brasileiro'), ('PTB', 'PTB - Partido Trabalhista Brasileiro'), ('PDT', 'PDT - Partido Democrático Trabalhista'), ('PT', 'PT - Partido Dos Trabalhadores'), ('DEM', 'DEM - Democratas'), ('PCdoB', 'PCdoB - Partido Comunista Do Brasil'), ('PSB', 'PSB - Partido Socialista Brasileiro'), ('PSDB', 'PSDB - Partido Da Social Democracia Brasileira'), ('PTC', 'PTC - Partido Trabalhista Cristão'), ('PSC', 'PSC - Partido Social Cristão'), ('PMN', 'PMN - Partido Da Mobilização Nacional'), ('PRP', 'PRP - Partido Republicano Progressista'), ('PPS', 'PPS - Partido Popular Socialista'), ('PV', 'PV - Partido Verde'), ('PTdoB', 'PTdoB - Partido Trabalhista Do Brasil'), ('PP', 'PP - Partido Progressista'), ('PSTU', 'PSTU - Partido Socialista Dos Trabalhadores Unificado'), ('PCB', 'PCB - Partido Comunista Brasileiro'), ('PRTB', 'PRTB - Partido Renovador Trabalhista Brasileiro'), ('PHS', 'PHS - Partido Humanista Da Solidariedade'), ('PSDC', 'PSDC - Partido Social Democrata Cristão'), ('PCO', 'PCO - Partido Da Causa Operária'), ('PTN', 'PTN - Partido Trabalhista Nacional'), ('PSL', 'PSL - Partido Social Liberal'), ('PRB', 'PRB - Partido Republicano Brasileiro'), ('PSOL', 'PSOL - Partido Socialismo E Liberdade'), ('PR', 'PR - Partido Da República'), ('PSD', 'PSD - Partido Social Democrático'), ('PPL', 'PPL - Partido Pátria Livre'), ('PEN', 'PEN - Partido Ecológico Nacional'), ('PROS', 'PROS - Partido Republicano Da Ordem Social'), ('SDD\xa0', 'SDD - Solidariedade')], max_length=10, verbose_name='Partido')),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=10, verbose_name='UF')),
                ('category', models.CharField(choices=[('T', 'Titular'), ('S', 'Suplente'), ('E', 'Efetivo')], max_length=20, verbose_name='Categoria')),
                ('annex', models.IntegerField(blank=True, null=True, verbose_name='Anexo')),
                ('chamber', models.IntegerField(blank=True, null=True, verbose_name='Gabinete')),
                ('tel', models.CharField(max_length=20, verbose_name='Telefone')),
                ('fax', models.CharField(max_length=20, verbose_name='Fax')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('last_updated', models.DateField(auto_now=True, verbose_name='Última atualização em')),
            ],
            options={
                'verbose_name': 'Político',
            },
        ),
        migrations.CreateModel(
            name='HelpText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome da Ajuda')),
                ('description', models.TextField(verbose_name='Texto de Ajuda')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('last_updated', models.DateField(auto_now=True, verbose_name='Última atualização em')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Campaign', verbose_name='Texto de ajuda para a campanha')),
            ],
            options={
                'verbose_name': 'Texto de Ajuda',
                'verbose_name_plural': 'Textos de Ajuda',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contacted_by', models.CharField(choices=[('tel', 'Telefone'), ('telegram', 'Telegrama via Web'), ('fax', 'Fax'), ('email', 'E-mail')], max_length=10, verbose_name='Contato via')),
                ('result', models.CharField(blank=True, choices=[('Telefonei', (('10', 'Falei com o(a) Deputado(a) em pessoa.'), ('11', 'Falei com outra pessoa.'), ('12', 'Deixei recado em uma máquina.'), ('13', 'Fone: número ocupado'), ('14', 'Fone: ninguém atendeu.'), ('15', 'Fone: número inexistente ou outra falha.'))), ('Enviei telegrama', (('20', 'Nada a reportar: correio vai entregar no gabinete!'),)), ('Enviei fax', (('30', 'Fax: transmissão bem sucedida.'), ('31', 'Fax: número ocupado.'), ('32', 'Fax: não atendeu.'), ('33', 'Fax: número inexistente ou outra falha.'))), ('Enviei e-mail', (('40', 'E-mail enviado e não voltou, tomara que leiam.'), ('41', 'E-mail voltou com erro.')))], max_length=10, null=True, verbose_name='Resultado do contato')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Campaign', verbose_name='Campanha')),
                ('politician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Politician', verbose_name='Político')),
            ],
            options={
                'verbose_name': 'Contato',
            },
        ),
    ]
