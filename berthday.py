from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class student(BaseModel):
    day : str
    month : str
    year : str
@app.post("/")
def check_name(st:student):
    day = st.day
    month = st.month
    year = st.year
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