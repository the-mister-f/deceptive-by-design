from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Computed
import datetime

db = SQLAlchemy()

class Survey(db.Model):
    __tablename__ = "survey_questions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # My uncle's birthday
    default_time = datetime.datetime(2069, 5, 26)
    default_response = "NONE"

    session_id = db.Column(db.String(200), unique=True, nullable=False)
    assigned_group = db.Column(db.Integer, Computed("(id - 1) % 3 + 1"))

    q1_response = db.Column(db.String(50), default=default_response)
    q1_time = db.Column(db.DateTime, default=default_time)

    q2_response = db.Column(db.String(50), default=default_response)
    q2_time = db.Column(db.DateTime, default=default_time)

    q3_response = db.Column(db.String(50), default=default_response)
    q3_time = db.Column(db.DateTime, default=default_time)

    q4_response = db.Column(db.String(100), default=default_response)
    q4_time = db.Column(db.DateTime, default=default_time)

    q5_response = db.Column(db.String(100), default=default_response)
    q5_time = db.Column(db.DateTime, default=default_time)

    q6_response = db.Column(db.String(100), default=default_response)
    q6_time = db.Column(db.DateTime, default=default_time)

    q7_response = db.Column(db.String(100), default=default_response)
    q7_time = db.Column(db.DateTime, default=default_time)

    q8_response = db.Column(db.String(100), default=default_response)
    q8_time = db.Column(db.DateTime, default=default_time)

    q9_response = db.Column(db.String(100), default=default_response)
    q9_time = db.Column(db.DateTime, default=default_time)

    q10_response = db.Column(db.String(100), default=default_response)
    q10_time = db.Column(db.DateTime, default=default_time)

    q11_response = db.Column(db.String(100), default=default_response)
    q11_time = db.Column(db.DateTime, default=default_time)

    p6_response = db.Column(db.String(100), default=default_response)
    p6_time = db.Column(db.DateTime, default=default_time)

    p7_response = db.Column(db.String(100), default=default_response)
    p7_time = db.Column(db.DateTime, default=default_time)

    p8_tos_toggle = db.Column(db.String(100), default=default_response)
    p8_newsletter_toggle = db.Column(db.String(100), default=default_response)
    p8_data_donation_toggle = db.Column(db.String(100), default=default_response)
    p8_time = db.Column(db.DateTime, default=default_time)

    p8_g3_01_view = db.Column(db.String(100), default=default_response)
    p8_g3_02_view = db.Column(db.String(100), default=default_response)
    p8_g3_03_view = db.Column(db.String(100), default=default_response)

    p18_time = db.Column(db.DateTime, default=default_time)
    free_trial = db.Column(db.String(100), default=default_response)

    p18_cancellation_reason = db.Column(db.String(100), default=default_response)

    p18_g2_01_view = db.Column(db.String(100), default=default_response)
    p18_g2_02_view = db.Column(db.String(100), default=default_response)

    p18_g3_01_view = db.Column(db.String(100), default=default_response)
    p18_g3_02_view = db.Column(db.String(100), default=default_response)
    p18_g3_03_view = db.Column(db.String(100), default=default_response)
    p18_g3_04_view = db.Column(db.String(100), default=default_response)

    q12_response = db.Column(db.String(100), default=default_response)
    q12_time = db.Column(db.DateTime, default=default_time)  

    q13_response = db.Column(db.String(100), default=default_response)
    q13_time = db.Column(db.DateTime, default=default_time)
    
    q14_response = db.Column(db.String(100), default=default_response)
    q14_time = db.Column(db.DateTime, default=default_time) 

    q15_response = db.Column(db.String(100), default=default_response)
    q15_time = db.Column(db.DateTime, default=default_time) 

    q16_response = db.Column(db.String(100), default=default_response)
    q16_time = db.Column(db.DateTime, default=default_time) 

    q17_response = db.Column(db.String(100), default=default_response)
    q17_time = db.Column(db.DateTime, default=default_time) 

    q18_response = db.Column(db.String(100), default=default_response)
    q18_time = db.Column(db.DateTime, default=default_time) 

    q19_response = db.Column(db.String(100), default=default_response)
    q19_time = db.Column(db.DateTime, default=default_time) 

    q20_response = db.Column(db.String(100), default=default_response)
    q20_time = db.Column(db.DateTime, default=default_time) 

    q21_response = db.Column(db.String(100), default=default_response)
    q21_time = db.Column(db.DateTime, default=default_time) 

    q22_response = db.Column(db.String(100), default=default_response)
    q22_time = db.Column(db.DateTime, default=default_time)

    q23_response = db.Column(db.String(100), default=default_response)
    q23_time = db.Column(db.DateTime, default=default_time) 

    q24_response = db.Column(db.String(100), default=default_response)
    q24_time = db.Column(db.DateTime, default=default_time) 

    q25_response = db.Column(db.String(100), default=default_response)
    q25_time = db.Column(db.DateTime, default=default_time) 

    q26_response = db.Column(db.String(100), default=default_response)
    q26_time = db.Column(db.DateTime, default=default_time) 

    q27_response = db.Column(db.String(100), default=default_response)
    q27_time = db.Column(db.DateTime, default=default_time) 

    def __repr__(self):
        return f"<Question {self.name}>"