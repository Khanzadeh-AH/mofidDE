Mofid DE enterance problem
=======================
برای پیدا کردن افراد یکسانی که در جداول سال های ۹۹ و ۴۰۰ وجود داشتند، از کوئری زیر استفاده شده است.

::

    $ select p99."ID" personID_1399, p00."ID" personID_1400 from people_people1399 p99 join people_people1400 p00 on (p99."BirthDate" = p00."BirthDate" and p99."GenderId" = p00."GenderId" and p99."AmCrdtr_95" = p00."AmCrdtr_95" and p99."Amdbtr_95" = p00."Amdbtr_95" and p99."frstPrd_95" = p00."frstPrd_95" and p99."lstPrd_95" = p00."lstPrd_95" and p99."SmBnft_95" = p00."SmBnft_95" and p99."Amdbtr_96" = p00."Amdbtr_96" and p99."frstPrd_96" = p00."frstPrd_96" and p99."lstPrd_96" = p00."lstPrd_96" and p99."SmBnft_96" = p00."SmBnft_96" and p99."SmBnft_96" = p00."SmBnft_96" and p99."Amdbtr_97" = p00."Amdbtr_97" and p99."frstPrd_97" = p00."frstPrd_97" and p99."lstPrd_97" = p00."lstPrd_97" and p99."SmBnft_97" = p00."SmBnft_97" and p99."SmBnft_97" = p00."SmBnft_97" and p99."Amdbtr_98" = p00."Amdbtr_98" and p99."frstPrd_98" = p00."frstPrd_98" and p99."lstPrd_98" = p00."lstPrd_98" and p99."SmBnft_98" = p00."SmBnft_98" and p99."SmBnft_98" = p00."SmBnft_98") or (p99."BirthDate" = p00."BirthDate" and p99."GenderId" = p00."GenderId" and p99."Amdbtr_98" = p00."Amdbtr_98" and p99."frstPrd_98" = p00."frstPrd_98" and p99."lstPrd_98" = p00."lstPrd_98" and p99."SmBnft_98" = p00."SmBnft_98" and p99."SmBnft_98" = p00."SmBnft_98" and p99."postalcode" = p00."postalcode" and p99."IsBiamrKhas" = p00."IsBiamrKhas" and p99."IsMalool" = p00."IsMalool" and p99."Provincename" = p00."Provincename" and p99."countyname" = p00."countyname" and p99."Senf" = p00."Senf" and p99."HasBimeSalamat" = p00."HasBimeSalamat")

البته برای پیدا کردن افرادی یکسان می توانستیم از فیچر های دیگری نیز استفاده کنیم ولی احتمال خطا در آن ها بیشتر از حالت فعلی بود. در نظر داشته باشید که متاسفانه کوئری فوق نمی تواند تمامی افراد یکسان در این دو سال را استخراج کند.


با فرض اینکه خروجی کوئری بالا صحیح است، صرفا با بررسی آی دی سرپرستان، می توانیم خانوار هایی که در این دو سال یکسان هستند را استخراج کنیم.

::

    $ select f99."ParentID", f00."ParentID", f99."MembersID", f00."MembersID" from people_family1399 f99  join people_samepeople ps on f99."ParentID" = ps."id_1399" join people_family1400 f00 on f00."ParentID" = ps."id_1400";





Anomalies in data
----

Author:
    Mischback

Contributors:
    `agirardeaudale <https://github.com/agirardeuadale>`_,
    `jmrbcu <https://github.com/jmrbcu>`_

Status:
    maintained, in development

Version:
    1.4

Django Version:
    3.0, 2.2, 2.1, 2.0, 1.11


Usage
-----

To use this repository just use the ``template`` option of `django-admin
<https://docs.djangoproject.com/en/2.2/ref/django-admin/#startproject>`_::

    $ django-admin startproject --template=https://github.com/Mischback/django-project-skeleton/archive/master.zip [projectname]

If you wish to automagically fill the ``apache2_vhost.sample`` the command is::

    $ django-admin startproject --template=https://github.com/Mischback/django-project-skeleton/archive/master.zip --name apache2_vhost.sample [projectname]


Documentation
-------------

You can see the documentation over at **Read the Docs**: `django-project-skeleton
<http://django-project-skeleton.readthedocs.org/en/stable/>`_
