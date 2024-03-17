from fastapi import FastAPI
from pydantic import BaseModel
class student(BaseModel):
    srial_number : str
app = FastAPI()

@app.post("/")
def validate_serial(st:student):
    serial = st.srial_number
    if len(serial) < 11:
        return f'حداقل میزان مجاز برای کاراکتر های این فیلد 11 عدد است'
    
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