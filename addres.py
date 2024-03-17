from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class student(BaseModel):
    addres : str
@app.post("/")
def check_city(st:student):
    addres = st.addres
    if len(addres) > 0 :
        if len(addres) > 100 :
            return f'آدرس شما ثبت شد'
        return f'حداکثر مقدار مجاز برای این ففیلد 100 کاراکتر است'
    return f'فیلد آدرس نباید خالی باشد'

