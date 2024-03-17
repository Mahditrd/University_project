from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class student(BaseModel):
    daneshkade : str
daneshkadeha = {"فنی و مهندسی" , "علوم پایه"  , "علوم انسانی" , "دامپزشکی"  , "اقتصاد" "کشاورزی" , "منابع طبیعی"}
@app.post("/")
def check_city(st:student):
    daneshkade = st.daneshkade
    if len(daneshkade) > 0 :
        for n in daneshkade :
            if ord(n) > 122 :
                if daneshkade in daneshkadeha:
                    return f'دانشکده شما ثبت شد'
                else:
                    return f'دانشکده انتخوابی باید یکی از دانشکده های موجود باشد'
            return f'نام دانشکده را به فارسی وارد کنید'
    return f'فیلد دانشکده نباید خالی باشد'