from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class student(BaseModel):
    phon_number : str
@app.post("/")
def check(st:student):
    phon_number = st.phon_number
    if len(phon_number) == 11 and phon_number.isdigit() == True:
        if int(phon_number[0]) == 0:
            return f'شماره تلفن ثابت شما ثبت شد'
        return f'شماره وارد شده باید با 0 شروع شود'
    return f'شماره تلفن عددی یازده رقمی است لطفا در وارد کردن رقم ها دقت فرمایید'