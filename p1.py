from fastapi import FastAPI
app = FastAPI()
@app.get("/{st_id}")
def check(st_id):
    L = len(st_id)
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