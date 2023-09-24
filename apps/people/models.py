from django.db import models
from django.contrib.postgres.fields import ArrayField


class People(models.Model):
    ID = models.PositiveBigIntegerField(primary_key=True)
    ParentID = models.PositiveBigIntegerField()
    BirthDate = models.DateField(null=True, blank=True)
    GenderId = models.CharField(max_length=1, blank=True, null=True)
    postalcode = models.PositiveIntegerField(null=True, blank=True)
    IsBiamrKhas = models.BooleanField(null=True, blank=True)
    IsMalool = models.BooleanField(null=True, blank=True)
    IsBimePardaz_Sandoghha = models.BooleanField(null=True, blank=True)
    IsBazneshaste_Sandoghha = models.BooleanField(null=True, blank=True)
    Provincename = models.CharField(max_length=128, null=True, blank=True)
    countyname = models.CharField(max_length=64, null=True, blank=True)
    HasMojavezSenfi = models.BooleanField(null=True, blank=True)
    Senf = models.CharField(max_length=256, null=True, blank=True)
    IsMaliati_Shaghel = models.BooleanField(null=True, blank=True)
    daramad_Total_Rials = models.PositiveBigIntegerField(null=True, blank=True)
    HasBimeSalamat = models.BooleanField(null=True, blank=True)
    CarsPrice_Sum = models.PositiveBigIntegerField(null=True, blank=True)
    AmCrdtr_95 = models.PositiveBigIntegerField(null=True, blank=True)
    Amdbtr_95 = models.PositiveBigIntegerField(null=True, blank=True)
    frstPrd_95 = models.PositiveBigIntegerField(null=True, blank=True)
    lstPrd_95 = models.PositiveBigIntegerField(null=True, blank=True)
    SmBnft_95 = models.PositiveBigIntegerField(null=True, blank=True)
    AmCrdtr_96 = models.PositiveBigIntegerField(null=True, blank=True)
    Amdbtr_96 = models.PositiveBigIntegerField(null=True, blank=True)
    frstPrd_96 = models.PositiveBigIntegerField(null=True, blank=True)
    lstPrd_96 = models.PositiveBigIntegerField(null=True, blank=True)
    SmBnft_96 = models.PositiveBigIntegerField(null=True, blank=True)
    AmCrdtr_97 = models.PositiveBigIntegerField(null=True, blank=True)
    Amdbtr_97 = models.PositiveBigIntegerField(null=True, blank=True)
    frstPrd_97 = models.PositiveBigIntegerField(null=True, blank=True)
    lstPrd_97 = models.PositiveBigIntegerField(null=True, blank=True)
    SmBnft_97 = models.PositiveBigIntegerField(null=True, blank=True)
    AmCrdtr_98 = models.PositiveBigIntegerField(null=True, blank=True)
    Amdbtr_98 = models.PositiveBigIntegerField(null=True, blank=True)
    frstPrd_98 = models.PositiveBigIntegerField(null=True, blank=True)
    lstPrd_98 = models.PositiveBigIntegerField(null=True, blank=True)
    SmBnft_98 = models.PositiveBigIntegerField(null=True, blank=True)

    class Meta:
        abstract = True


class People1399(People):
    isurban = models.BooleanField(null=True, blank=True)
    Card98_Rials = models.PositiveBigIntegerField(null=True, blank=True)
    Card98_PaymentCount = models.PositiveBigIntegerField(null=True, blank=True)
    Card99_Rials = models.PositiveBigIntegerField(null=True, blank=True)
    Card99PaymentCount = models.PositiveBigIntegerField(null=True, blank=True)
    Cars_Count = models.PositiveIntegerField(null=True, blank=True)
    Trips_Count_AirNotPilgrimage = models.PositiveSmallIntegerField(
        null=True, blank=True
    )
    Trips_Count_NotAirNotPilgrimage = models.PositiveSmallIntegerField(
        null=True, blank=True
    )
    Trips_Count_AirPilgrimage = models.PositiveSmallIntegerField(null=True, blank=True)
    Trips_Count_NotAirPilgrimage = models.PositiveSmallIntegerField(
        null=True, blank=True
    )
    BimeSalmat_Type = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        verbose_name_plural = "People"


class People1400(People):
    Familysize = models.PositiveSmallIntegerField(null=True, blank=True)
    AmCrdtr_99 = models.PositiveBigIntegerField(null=True, blank=True)
    Amdbtr_99 = models.PositiveBigIntegerField(null=True, blank=True)
    frstPrd_99 = models.PositiveBigIntegerField(null=True, blank=True)
    lstPrd_99 = models.PositiveBigIntegerField(null=True, blank=True)
    SmBnft_99 = models.PositiveBigIntegerField(null=True, blank=True)
    AmCrdtr_1400 = models.PositiveBigIntegerField(null=True, blank=True)
    Amdbtr_1400 = models.PositiveBigIntegerField(null=True, blank=True)
    frstPrd_1400 = models.PositiveBigIntegerField(null=True, blank=True)
    lstPrd_1400 = models.PositiveBigIntegerField(null=True, blank=True)
    SmBnft_1400 = models.PositiveBigIntegerField(null=True, blank=True)
    Card98_Percentile = models.SmallIntegerField(null=True, blank=True)
    Card99_SumMonth1To6_Percentile = models.SmallIntegerField(null=True, blank=True)
    Card99_SumMonth6To12_Percentile = models.SmallIntegerField(null=True, blank=True)
    Card1400_SumMonth01To06_Percentile = models.SmallIntegerField(null=True, blank=True)
    Card1400_SumMonth06to12_Percentile = models.SmallIntegerField(null=True, blank=True)
    Loan_99 = models.PositiveBigIntegerField(null=True, blank=True)
    Loan_1400 = models.PositiveBigIntegerField(null=True, blank=True)
    CarsPrice_Omoomi_Sum = models.PositiveBigIntegerField(null=True, blank=True)
    CarsPrice_Omoomi_Max = models.PositiveBigIntegerField(null=True, blank=True)
    CarsPrice_Omoomi_Min = models.PositiveBigIntegerField(null=True, blank=True)
    Cars_Omoomi_Count = models.SmallIntegerField(null=True, blank=True)
    CarsPrice_GheyrOmoomi_Sum = models.PositiveBigIntegerField(null=True, blank=True)
    CarsPrice_GheyrOmoomi_Max = models.PositiveBigIntegerField(null=True, blank=True)
    CarsPrice_GheyrOmoomi_Min = models.PositiveBigIntegerField(null=True, blank=True)
    Cars_GheyrOmoomi_Count = models.PositiveBigIntegerField(null=True, blank=True)
    CarsPrice_Max = models.PositiveBigIntegerField(null=True, blank=True)
    CarsPrice_Min = models.PositiveBigIntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "People"


class Family(models.Model):
    ParentID = models.PositiveBigIntegerField(primary_key=True)
    MembersID = ArrayField(models.PositiveBigIntegerField(), blank=True, null=True)

    class Meta:
        abstract = True


class Family1399(Family):
    ...

    class Meta:
        verbose_name_plural = "Families"


class Family1400(Family):
    ...

    class Meta:
        verbose_name_plural = "Families"


class SamePeople(models.Model):
    id_1399 = models.PositiveBigIntegerField()
    id_1400 = models.PositiveBigIntegerField()

    class Meta:
        verbose_name_plural = "SamePeople"


class SameFamilies(Family):
    parentid_1399 = models.PositiveBigIntegerField()
    parentid_1400 = models.PositiveBigIntegerField()
    membersid_1399 = ArrayField(models.PositiveBigIntegerField(), blank=True, null=True)
    membersid_1400 = ArrayField(models.PositiveBigIntegerField(), blank=True, null=True)

    class Meta:
        verbose_name_plural = "SameFamilies"
