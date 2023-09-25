Mofid DE enterance problem
=======================
برای پیدا کردن افراد یکسانی که در جداول سال های ۹۹ و ۴۰۰ وجود داشتند، از کوئری زیر استفاده شده است.

::

    $ select p99."ID" personID_1399, p00."ID" personID_1400 from people_people1399 p99 join people_people1400 p00 on (p99."BirthDate" = p00."BirthDate" and p99."GenderId" = p00."GenderId" and p99."AmCrdtr_95" = p00."AmCrdtr_95" and p99."Amdbtr_95" = p00."Amdbtr_95" and p99."frstPrd_95" = p00."frstPrd_95" and p99."lstPrd_95" = p00."lstPrd_95" and p99."SmBnft_95" = p00."SmBnft_95" and p99."Amdbtr_96" = p00."Amdbtr_96" and p99."frstPrd_96" = p00."frstPrd_96" and p99."lstPrd_96" = p00."lstPrd_96" and p99."SmBnft_96" = p00."SmBnft_96" and p99."SmBnft_96" = p00."SmBnft_96" and p99."Amdbtr_97" = p00."Amdbtr_97" and p99."frstPrd_97" = p00."frstPrd_97" and p99."lstPrd_97" = p00."lstPrd_97" and p99."SmBnft_97" = p00."SmBnft_97" and p99."SmBnft_97" = p00."SmBnft_97" and p99."Amdbtr_98" = p00."Amdbtr_98" and p99."frstPrd_98" = p00."frstPrd_98" and p99."lstPrd_98" = p00."lstPrd_98" and p99."SmBnft_98" = p00."SmBnft_98" and p99."SmBnft_98" = p00."SmBnft_98") or (p99."BirthDate" = p00."BirthDate" and p99."GenderId" = p00."GenderId" and p99."Amdbtr_98" = p00."Amdbtr_98" and p99."frstPrd_98" = p00."frstPrd_98" and p99."lstPrd_98" = p00."lstPrd_98" and p99."SmBnft_98" = p00."SmBnft_98" and p99."SmBnft_98" = p00."SmBnft_98" and p99."postalcode" = p00."postalcode" and p99."IsBiamrKhas" = p00."IsBiamrKhas" and p99."IsMalool" = p00."IsMalool" and p99."Provincename" = p00."Provincename" and p99."countyname" = p00."countyname" and p99."Senf" = p00."Senf" and p99."HasBimeSalamat" = p00."HasBimeSalamat")

البته برای پیدا کردن افرادی یکسان می توانستیم از فیچر های دیگری نیز استفاده کنیم ولی احتمال خطا در آن ها بیشتر از حالت فعلی بود. در نظر داشته باشید که متاسفانه کوئری فوق نمی تواند تمامی افراد یکسان در این دو سال را استخراج کند.


با فرض اینکه خروجی کوئری بالا صحیح است، صرفا با بررسی آی دی سرپرستان، می توانیم خانوار هایی که در این دو سال یکسان هستند را استخراج کنیم.

::

    $ select f99."ParentID", f00."ParentID", f99."MembersID", f00."MembersID" from people_family1399 f99  join people_samepeople ps on f99."ParentID" = ps."id_1399" join people_family1400 f00 on f00."ParentID" = ps."id_1400";


Finding families
----
برای پیدا کردن خانوار ها، از آی دی سرپرست استفاده شده. به طوریکه افرادی که سرپرست یکسان داشتند در یک خانوار قرار گرفته اند.
::

    $ select "ParentID", array_agg("ID") members from people_people1399 group by "ParentID" having array_length(array_agg("ID"), 1) > 1;

در کوئری فوق، خانوار هایی که تعدادشان ۱ نفر می باشد، لحاظ نشده (زیرا فرض شده که ۱ نفر به تنهایی یک خانواده حساب نمی شود).




Anomalies in data
----
برای پیدا کردن ناسازگاری در داده ها موارد زیر بررسی شدند.

کاربرانی که بیش از یک سرپرست دارند. این مورد در هیچکدام از جداول مشاهده نشد.

مقادیر فیلد مربوط به جنسیت نیز بررسی شد و ناسازگاری مشاهده نشد.

در مقادیر تاریخ تولد، ناسازگاری وجود داشت. برای مثال با اجرای کوئری زیر، مقادیری بدست آمد که واضحا دارای خطا می باشند.
::

    $ select max("BirthDate") from people_people1399;

        3221-03-06

منظقا تعداد کاراکتر های کدپستی باید ثابت باشد. اما در این جداول در برخی موارد ۶ و در برخی دیگر ۷ کاراکتر بود.

بررسی شد که مقادیر ستون های مالی در جداول نامنفی باشند.

اگر جدول مربوط به شهرستان های هر استان در دسترس بود، می توانستیم بررسی کنیم که واقعا شهرستان مذکور در استان مذکور وجود داشته باشد.

در صورت وجود جدول فوق، می توانستیم بررسی کنیم که شخصی که در روستا زندگی می کند، آیا فیلد مربوطه به آن ۱ هست یا نه.

بررسی شد افراد خردسال درآمدی نداشته باشند.

بررسی شد افراد خردسال وامی دریافت نکرده باشند.

بررسی شد آیا افرادی که درآمدی ندارند وام دریافت کرده اند.

مجموع مانده اول سال و واریز و سود سال با کسر برداشت ها باید برابر مانده آخر سال باشد.

مانده آخر هر سال باید برابر مانده اول سال بعدی باشد.

افرادی که ماشین دارند، باید قیمت ماشین هایشان مشخص باشد (همیشه اینطور نبود).
