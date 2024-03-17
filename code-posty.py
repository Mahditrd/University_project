from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class student(BaseModel):
    code_posty : str
@app.post("/")
def check(st:student):
    code_posty = st.code_posty
    if len(code_posty) == 10 and code_posty.isdigit() == True:
        if int(code_posty[0]) != 0 :
            return f'کد پستی شما ثبت شد'
        return f'کد پستی نباید با صفر شروع شود'
    return f'کد پستی عددی ده رقمی است لطفا در وارد کردن رقم ها دقت فرمایید'


