from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class student(BaseModel):
    reshte : str
reshteha = {
    "مهندسی معدن" , "مهندسی برق" , "مهندسی عمران" , "حرفه و فن فرهنگیان" ,
      "مهندسی کامپیوتر" , "مهندسی شهرسازی" , "مهندسی مکانیک و پلیمر"
}
@app.post("/")
def check_reshte(st:student):
    reshte = st.reshte
    if len(reshte) > 0 :
        for n in reshte :
            if ord(n) > 122 :
                if reshte in reshteha:
                    return f'رشته شما ثبت شد'
                else:
                    return f'رشته انتخوابی باید یکی از رشته های موجود باشد'
            return f'نام رشته را به فارسی وارد کنید'
    return f'فیلد رشته نباید خالی باشد'