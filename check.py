

"""چک کردن کد دانشجویی"""

def st_id(st_id):
    L = len(st_id)
    if L == 0 :
        return f'فیلد شماره دانشجویی نمی تواند خالی باشد'
    if st_id.isdigit() == False:
        return f'شماره دانشجویی نمیتواند شامل حروف و کاراکتر هایی جز عدد باشد'
    st_id = int(st_id)
    if L == 11:
        year = st_id // 100000000
        if 399<year<403:
            sabet = (st_id // 100) - (year * 1000000)
            if sabet == 114150:
                last = st_id % 100
                if 0 < last <100 :
                    return f'شماره دانشجویی درست است ' , st_id
                return f'قسمت اندیس نادرست است'
            return f'قسمت ثابت اشتباه است'
        return f'قسمت سال اشتباه است'
    return f'شماره دانشجویی باید 11 رقم باشد . تعداد ارقام شماره دانشجویی وارد شده نادرست است'



"""چک کردن شهر و استان دانشجو"""

def city(city):
    iran_provinces = {
        "آذربایجان شرقی": "تبریز",
        "آذربایجان غربی": "ارومیه",
        "اردبیل": "اردبیل",
        "اصفهان": "اصفهان",
        "البرز": "کرج",
        "ایلام": "ایلام",
        "بوشهر": "بوشهر",
        "تهران": "تهران",
        "چهارمحال و بختیاری": "شهرکرد",
        "خراسان جنوبی": "بیرجند",
        "خراسان رضوی": "مشهد",
        "خراسان شمالی": "بجنورد",
        "خوزستان": "اهواز",
        "زنجان": "زنجان",
        "سمنان": "سمنان",
        "سیستان و بلوچستان": "زاهدان",
        "فارس": "شیراز",
        "قزوین": "قزوین",
        "قم": "قم",
        "کردستان": "سنندج",
        "کرمان": "کرمان",
        "کرمانشاه": "کرمانشاه",
        "کهگیلویه و بویراحمد": "یاسوج",
        "گلستان": "گرگان",
        "گیلان": "رشت",
        "لرستان": "خرم‌آباد",
        "مازندران": "ساری",
        "مرکزی": "اراک",
        "هرمزگان": "بندرعباس",
        "همدان": "همدان",
        "یزد": "یزد"
    }
    if len(city) > 0 :
        for n in city :
            if ord(n) > 122 :
                provinces_list = list(iran_provinces.values())
                if city in provinces_list:
                    return f'استان شما ثبت شد'
                else:
                    return f'استان شما باید مرکز یکی از استان ها باشد'
            return f'نام استان را به فارسی وارد کنید'
    return f'فیلد استان نباید خالی باشد'



"""چک کردن سریال شناسنامه"""


def serial_number(serial):
    if len(serial) == 0 :
        return f'فیلد سریال شناسنامه خالی است . لطفا همه فیلد ها را پر کنید'
    if len(serial) < 11:
        return f'حداقل میزان مجاز برای کاراکتر های فیلد سریال شناسنامه 11 عدد است'
    
    parts = serial.split('-')

    if len(parts) != 3:
        return f'سریال شناسنامه باید دارا سه بخش باشد که با بک اسلش از هم جدا شده اند'
    
    if len(parts[0]) != 6:
        return f'بخش اول سریال شناسنامه باید شیش رقم باشد'
    
    if not parts[0].isdigit():
        return f'مقدار وارد شده در بخش اول باید فقط شامل عدد باشد'
    
    if len(parts[1]) != 1 or not parts[1].isalpha():
            return f'بخش دوم باید شامل یک حرف فارسی باشد'
    if ord(parts[1]) < 400:
        return f'بخش دوم باید شامل حرف فارسی باشد'
    if len(parts[2]) != 2 or not parts[2].isdigit():
        return f'بخش سوم باید عددی دو رقمی باشد'
    else:
        return f'سریال شناسنامه شما ثبت شد'
    

"""چک کردن رشته تحصیلی دانشجو"""


def reshte(reshte):
    reshteha = {
    "مهندسی معدن" , "مهندسی برق" , "مهندسی عمران" , "حرفه و فن فرهنگیان" ,
      "مهندسی کامپیوتر" , "مهندسی شهرسازی" , "مهندسی مکانیک و پلیمر"
    }
    if len(reshte) > 0 :
        for n in reshte :
            if ord(n) > 122 :
                if reshte in reshteha:
                    return f'رشته شما ثبت شد'
                else:
                    return f'رشته انتخوابی باید یکی از رشته های موجود باشد'
            return f'نام رشته را به فارسی وارد کنید'
    return f'فیلد رشته نباید خالی باشد'



"""چک کردن نام دانشجو """


def name(f_name , l_name):
    if len(f_name) <= 10 and len(l_name) <=10 :
        if len(f_name) == 0 or len(l_name) == 0:
            return "لظفا نام ها را ارسال کنید . هیچ کادری نباید خالی باشد"
        if f_name.isalpha() == True and l_name.isalpha() == True :
            for n in f_name :
                if ord(n)>122 :
                    for m in l_name:
                        if ord(m)>122:
                            return f'نام شما تایید شد'
                        return f'نام خانوادگی را به حروف فارسی وارد کنید'
                return f'نام شما باید با حروف فارسی مشخص شود'
        return f'نام نباید شامل علاعم یا حروف باشد'
    return f'حداکثر کاراکتر مجاز برای نام 10 کاراکتر به اضای هر مقدار ارسالی است'



"""چک کردن کد ملی دانشجو"""


def code_meli(code_meli):
    l = len(code_meli)
    sum = 0
    if l == 0:
        return f'فیلد کد ملی نباید خالی باشد'
    if l == 10 :
        if code_meli.isdigit() == True :
            for i in range(0 , l - 1):
                c = ord(code_meli[i])
                c -= 48
                sum = sum + c *(l - i)
            r = sum % 11
            c = ord(code_meli[l - 1])
            c -= 48
            if r > 2:
                r = 11 - r
            if r == c:
                return f'کد ملی شما ثبت شد'
            else : 
                return f'کد ملی وارد شده اشتباه است لطفا در وارد کردن ارقام دقت فرمایید'    
        return f'کد ملی باید فقط شامل ارقام باشد'       
    return f'میزان مجاز برای فیلد کد ملی 10 رقم است'




"""چک کردن تاریخ تولد"""


def Birthday(day , month , year):
    if len(day) == 0 or len(month) == 0 or len(year) == 0 :
        return f'هیچ یک از مقادیر سال و ماه و روز نباید خالی باشند'
    if len(day) == 2 and len(month) == 2:
        day = int(day)
        month = int(month)
        year = int(year)
        if 1350 < year < 1390 :
            if 0 < month <= 6 :
                if 0 < day < 32 :
                    return f'تارخ تولد شما تایید شد'
                else :
                    return f'روز وارد شده نا درست است مقدار وارد شده باید بسته به ماه تولد شما عددی بین 1 تا 31 باشد'
            elif 6 < month < 12 :
                if 0 < day < 31:
                    return f'تارخ تولد شما تایید شد'
                else :
                    return f'روز وارد شده نا درست است مقدار وارد شده باید بسته به ماه تولد شما عددی بین 1 تا 30 باشد'
            elif month == 12 :
                if 0 < day < 30 :
                    return f'تارخ تولد شما تایید شد'
                else :
                    return f'روز وارد شده نا درست است مقدار وارد شده باید بسته به ماه تولد شما عددی بین 1 تا 29 باشد'
            else :
                return f'ماه وارد شده نا درست است مقدار ماه وارد شده باسد بین 1 تا 12 باشد'
        return f'سال وارد شده باید به صورت عددی چهار رقمی و بین سال های 1350 تا 1390 باشد . مثال درست : 1383'
    return f'روز و ماه باید به صورت یک مقدار دو رقمی ارسال شوند . برای مثال برای ارسال عدد 5 لازم است به صورت 05 انرا ارسال کنید'



"""چک کردن شماره تماس"""


def phon_number(phon_number):
    if len(phon_number) == 0 :
        return f'لطفا فیلد شماره را پرکنید'
    if len(phon_number) == 11 and phon_number.isdigit() == True:
        if int(phon_number[0]) == 0 and int(phon_number[1]) == 9 :
            return f'شماره تلفن شما ثبت شد'
        return f'شماره وارد شده باید با 09 شروع شود'
    return f'شماره تلفن عددی یازده رقمی است لطفا در وارد کردن رقم ها دقت فرمایید'


"""چک کردن شماره منزل"""

def home_phon_number(phon_number):
    if len(phon_number) == 0 :
        return f'لطفا فیلد شماره را پرکنید'
    if len(phon_number) == 11 and phon_number.isdigit() == True:
        if int(phon_number[0]) == 0:
            return f'شماره تلفن شما ثبت شد'
        return f'شماره وارد شده باید با 0 شروع شود'
    return f'شماره تلفن عددی یازده رقمی است لطفا در وارد کردن رقم ها دقت فرمایید'


"""چک کردن دانشکده"""


def daneshkade(daneshkade):
    daneshkadeha = {"فنی و مهندسی" , "علوم پایه"  , "علوم انسانی" , "دامپزشکی"  , "اقتصاد" "کشاورزی" , "منابع طبیعی"}
    if len(daneshkade) > 0 :
        for n in daneshkade :
            if ord(n) > 122 :
                if daneshkade in daneshkadeha:
                    return f'دانشکده شما ثبت شد'
                else:
                    return f'دانشکده انتخوابی باید یکی از دانشکده های موجود باشد'
            return f'نام دانشکده را به فارسی وارد کنید'
    return f'فیلد دانشکده نباید خالی باشد'



"""چک کردن آدرس"""


def addres(addres):
    if len(addres) > 0 :
        if len(addres) < 100 :
            return f'آدرس شما ثبت شد'
        return f'حداکثر مقدار مجاز برای این ففیلد 100 کاراکتر است'
    return f'فیلد آدرس نباید خالی باشد'


"""چک کردن کد پستی"""


def code_posty(code_posty):
    if len(code_posty) == 10 and code_posty.isdigit() == True:
        if int(code_posty[0]) != 0 :
            return f'کد پستی شما ثبت شد'
        return f'کد پستی نباید با صفر شروع شود'
    return f'کد پستی عددی ده رقمی است لطفا در وارد کردن رقم ها دقت فرمایید'