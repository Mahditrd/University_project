from fastapi import FastAPI
from pydantic import BaseModel
import check
class student(BaseModel):
    st_id : str
    f_name : str
    l_name :str
    code_meli : str
    srial_number : str
    year : str
    month : str
    day : str
    phon_number : str
    home_phon_number : str
    daneshkade : str
    reshte : str
    state : str
    city : str
    addres : str
    code_posty : str
app = FastAPI()
@app.post("/")
def check_all(st:student):
    return check.st_id(st.st_id) , check.name(st.f_name , st.l_name) , check.code_meli(st.code_meli) ,check.serial_number(st.srial_number) ,  check.Birthday(st.day , st.month , st.year) ,check.phon_number(st.phon_number) ,check.home_phon_number(st.home_phon_number) , check.daneshkade(st.daneshkade) ,  check.reshte(st.reshte) ,  check.city(st.state) ,check.city(st.city) , check.addres(st.addres) , check.code_posty(st.code_posty)