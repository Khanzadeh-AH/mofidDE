# Generated by Django 4.2.5 on 2023-09-24 08:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="People1399",
            fields=[
                (
                    "ID",
                    models.PositiveBigIntegerField(primary_key=True, serialize=False),
                ),
                ("ParentID", models.PositiveBigIntegerField()),
                ("BirthDate", models.DateField(blank=True, null=True)),
                ("GenderId", models.CharField(blank=True, max_length=1, null=True)),
                ("postalcode", models.PositiveIntegerField(blank=True, null=True)),
                ("IsBiamrKhas", models.BooleanField(blank=True, null=True)),
                ("IsMalool", models.BooleanField(blank=True, null=True)),
                ("IsBimePardaz_Sandoghha", models.BooleanField(blank=True, null=True)),
                ("IsBazneshaste_Sandoghha", models.BooleanField(blank=True, null=True)),
                (
                    "Provincename",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                ("countyname", models.CharField(blank=True, max_length=64, null=True)),
                ("HasMojavezSenfi", models.BooleanField(blank=True, null=True)),
                ("Senf", models.CharField(blank=True, max_length=256, null=True)),
                ("IsMaliati_Shaghel", models.BooleanField(blank=True, null=True)),
                (
                    "daramad_Total_Rials",
                    models.PositiveBigIntegerField(blank=True, null=True),
                ),
                ("HasBimeSalamat", models.BooleanField(blank=True, null=True)),
                (
                    "CarsPrice_Sum",
                    models.PositiveBigIntegerField(blank=True, null=True),
                ),
                ("AmCrdtr_95", models.PositiveBigIntegerField(blank=True, null=True)),
                ("Amdbtr_95", models.PositiveBigIntegerField(blank=True, null=True)),
                ("frstPrd_95", models.PositiveBigIntegerField(blank=True, null=True)),
                ("lstPrd_95", models.PositiveBigIntegerField(blank=True, null=True)),
                ("SmBnft_95", models.PositiveBigIntegerField(blank=True, null=True)),
                ("AmCrdtr_96", models.PositiveBigIntegerField(blank=True, null=True)),
                ("Amdbtr_96", models.PositiveBigIntegerField(blank=True, null=True)),
                ("frstPrd_96", models.PositiveBigIntegerField(blank=True, null=True)),
                ("lstPrd_96", models.PositiveBigIntegerField(blank=True, null=True)),
                ("SmBnft_96", models.PositiveBigIntegerField(blank=True, null=True)),
                ("AmCrdtr_97", models.PositiveBigIntegerField(blank=True, null=True)),
                ("Amdbtr_97", models.PositiveBigIntegerField(blank=True, null=True)),
                ("frstPrd_97", models.PositiveBigIntegerField(blank=True, null=True)),
                ("lstPrd_97", models.PositiveBigIntegerField(blank=True, null=True)),
                ("SmBnft_97", models.PositiveBigIntegerField(blank=True, null=True)),
                ("AmCrdtr_98", models.PositiveBigIntegerField(blank=True, null=True)),
                ("Amdbtr_98", models.PositiveBigIntegerField(blank=True, null=True)),
                ("frstPrd_98", models.PositiveBigIntegerField(blank=True, null=True)),
                ("lstPrd_98", models.PositiveBigIntegerField(blank=True, null=True)),
                ("SmBnft_98", models.PositiveBigIntegerField(blank=True, null=True)),
                ("isurban", models.BooleanField(blank=True, null=True)),
                ("Card98_Rials", models.PositiveBigIntegerField(blank=True, null=True)),
                (
                    "Card98_PaymentCount",
                    models.PositiveBigIntegerField(blank=True, null=True),
                ),
                ("Card99_Rials", models.PositiveBigIntegerField(blank=True, null=True)),
                (
                    "Card99PaymentCount",
                    models.PositiveBigIntegerField(blank=True, null=True),
                ),
                ("Cars_Count", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "Trips_Count_AirNotPilgrimage",
                    models.PositiveSmallIntegerField(blank=True, null=True),
                ),
                (
                    "Trips_Count_NotAirNotPilgrimage",
                    models.PositiveSmallIntegerField(blank=True, null=True),
                ),
                (
                    "Trips_Count_AirPilgrimage",
                    models.PositiveSmallIntegerField(blank=True, null=True),
                ),
                (
                    "Trips_Count_NotAirPilgrimage",
                    models.PositiveSmallIntegerField(blank=True, null=True),
                ),
                (
                    "BimeSalmat_Type",
                    models.CharField(blank=True, max_length=64, null=True),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="People1400",
            fields=[
                (
                    "ID",
                    models.PositiveBigIntegerField(primary_key=True, serialize=False),
                ),
                ("ParentID", models.PositiveBigIntegerField()),
                ("BirthDate", models.DateField(blank=True, null=True)),
                ("GenderId", models.CharField(blank=True, max_length=1, null=True)),
                ("postalcode", models.PositiveIntegerField(blank=True, null=True)),
                ("IsBiamrKhas", models.BooleanField(blank=True, null=True)),
                ("IsMalool", models.BooleanField(blank=True, null=True)),
                ("IsBimePardaz_Sandoghha", models.BooleanField(blank=True, null=True)),
                ("IsBazneshaste_Sandoghha", models.BooleanField(blank=True, null=True)),
                (
                    "Provincename",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                ("countyname", models.CharField(blank=True, max_length=64, null=True)),
                ("HasMojavezSenfi", models.BooleanField(blank=True, null=True)),
                ("Senf", models.CharField(blank=True, max_length=256, null=True)),
                ("IsMaliati_Shaghel", models.BooleanField(blank=True, null=True)),
                (
                    "daramad_Total_Rials",
                    models.PositiveBigIntegerField(blank=True, null=True),
                ),
                ("HasBimeSalamat", models.BooleanField(blank=True, null=True)),
                (
                    "CarsPrice_Sum",
                    models.PositiveBigIntegerField(blank=True, null=True),
                ),
                ("AmCrdtr_95", models.PositiveBigIntegerField(blank=True, null=True)),
                ("Amdbtr_95", models.PositiveBigIntegerField(blank=True, null=True)),
                ("frstPrd_95", models.PositiveBigIntegerField(blank=True, null=True)),
                ("lstPrd_95", models.PositiveBigIntegerField(blank=True, null=True)),
                ("SmBnft_95", models.PositiveBigIntegerField(blank=True, null=True)),
                ("AmCrdtr_96", models.PositiveBigIntegerField(blank=True, null=True)),
                ("Amdbtr_96", models.PositiveBigIntegerField(blank=True, null=True)),
                ("frstPrd_96", models.PositiveBigIntegerField(blank=True, null=True)),
                ("lstPrd_96", models.PositiveBigIntegerField(blank=True, null=True)),
                ("SmBnft_96", models.PositiveBigIntegerField(blank=True, null=True)),
                ("AmCrdtr_97", models.PositiveBigIntegerField(blank=True, null=True)),
                ("Amdbtr_97", models.PositiveBigIntegerField(blank=True, null=True)),
                ("frstPrd_97", models.PositiveBigIntegerField(blank=True, null=True)),
                ("lstPrd_97", models.PositiveBigIntegerField(blank=True, null=True)),
                ("SmBnft_97", models.PositiveBigIntegerField(blank=True, null=True)),
                ("AmCrdtr_98", models.PositiveBigIntegerField(blank=True, null=True)),
                ("Amdbtr_98", models.PositiveBigIntegerField(blank=True, null=True)),
                ("frstPrd_98", models.PositiveBigIntegerField(blank=True, null=True)),
                ("lstPrd_98", models.PositiveBigIntegerField(blank=True, null=True)),
                ("SmBnft_98", models.PositiveBigIntegerField(blank=True, null=True)),
                ("Familysize", models.PositiveSmallIntegerField(blank=True, null=True)),
                ("AmCrdtr_99", models.PositiveBigIntegerField(blank=True, null=True)),
                ("Amdbtr_99", models.PositiveBigIntegerField(blank=True, null=True)),
                ("frstPrd_99", models.PositiveBigIntegerField(blank=True, null=True)),
                ("lstPrd_99", models.PositiveBigIntegerField(blank=True, null=True)),
                ("SmBnft_99", models.PositiveBigIntegerField(blank=True, null=True)),
                ("AmCrdtr_1400", models.PositiveBigIntegerField(blank=True, null=True)),
                ("Amdbtr_1400", models.PositiveBigIntegerField(blank=True, null=True)),
                ("frstPrd_1400", models.PositiveBigIntegerField(blank=True, null=True)),
                ("lstPrd_1400", models.PositiveBigIntegerField(blank=True, null=True)),
                ("SmBnft_1400", models.PositiveBigIntegerField(blank=True, null=True)),
                ("Card98_Percentile", models.SmallIntegerField(blank=True, null=True)),
                (
                    "Card99_SumMonth1To6_Percentile",
                    models.SmallIntegerField(blank=True, null=True),
                ),
                (
                    "Card99_SumMonth6To12_Percentile",
                    models.SmallIntegerField(blank=True, null=True),
                ),
                (
                    "Card1400_SumMonth01To06_Percentile",
                    models.SmallIntegerField(blank=True, null=True),
                ),
                (
                    "Card1400_SumMonth06to12_Percentile",
                    models.SmallIntegerField(blank=True, null=True),
                ),
                ("Loan_99", models.PositiveBigIntegerField(blank=True, null=True)),
                ("Loan_1400", models.PositiveBigIntegerField(blank=True, null=True)),
                (
                    "CarsPrice_Omoomi_Sum",
                    models.PositiveBigIntegerField(blank=True, null=True),
                ),
                (
                    "CarsPrice_Omoomi_Max",
                    models.PositiveBigIntegerField(blank=True, null=True),
                ),
                (
                    "CarsPrice_Omoomi_Min",
                    models.PositiveBigIntegerField(blank=True, null=True),
                ),
                ("Cars_Omoomi_Count", models.SmallIntegerField(blank=True, null=True)),
                (
                    "CarsPrice_GheyrOmoomi_Sum",
                    models.PositiveBigIntegerField(blank=True, null=True),
                ),
                (
                    "CarsPrice_GheyrOmoomi_Max",
                    models.PositiveBigIntegerField(blank=True, null=True),
                ),
                (
                    "CarsPrice_GheyrOmoomi_Min",
                    models.PositiveBigIntegerField(blank=True, null=True),
                ),
                (
                    "Cars_GheyrOmoomi_Count",
                    models.PositiveBigIntegerField(blank=True, null=True),
                ),
                (
                    "CarsPrice_Max",
                    models.PositiveBigIntegerField(blank=True, null=True),
                ),
                (
                    "CarsPrice_Min",
                    models.PositiveBigIntegerField(blank=True, null=True),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
