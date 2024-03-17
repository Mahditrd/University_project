from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class student(BaseModel):
    code_meli : str
@app.post("/")
def check(st:student):
    code_meli = st.code_meli
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