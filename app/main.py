from flask import Flask, render_template, request, redirect, url_for, session
import secrets, uuid, datetime
from app.models import db, Survey
from app.utils import get_db_uri


########################### APP SETUP ###########################

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = get_db_uri()
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = datetime.timedelta(days=1)

assigned_group_map = {
    1: "prototype08_g1",
    2: "prototype08_g2",
    3: "prototype08_g3_01"
}

assigned_group_map2 = {
    1: "prototype18_g1",
    2: "prototype18_g2_01",
    3: "prototype18_g3_01"
}

########################### DB SETUP ###########################

db.init_app(app)
with app.app_context():
    db.create_all()

########################### HELPER ###########################

@app.before_request
def track_user():
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
        session.permanent = True

########################### SURVEY ###########################

@app.route('/')
def index():
    return render_template('survey/survey_welcome.html')

@app.route('/question01', methods=['GET', 'POST'])
def question01():
    if request.method == 'GET':
        return render_template('survey/survey_question01.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        if not name:
            return "Please provide your name before proceeding."
        else:
            existing = Survey.query.filter_by(session_id=session["session_id"]).first()
            now = datetime.datetime.now(datetime.timezone.utc)
            if existing:
                existing.q1_response = name
                existing.q1_time = now
            else:
                new_ = Survey(session_id=session["session_id"], q1_response=name, q1_time=now)
                db.session.add(new_)

            db.session.commit()
            return redirect(url_for('question02'))


@app.route('/question02', methods=['GET', 'POST'])
def question02():
    if request.method == 'GET':
        return render_template('survey/survey_question02.html')
    elif request.method == 'POST':
        age = request.form.get('age')
        if not age:
            return "Please provide your age before proceeding."
        else:
            existing = Survey.query.filter_by(session_id=session["session_id"]).first()
            now = datetime.datetime.now(datetime.timezone.utc)
            if existing:
                existing.q2_response = age
                existing.q2_time = now
            else:
                new_ = Survey(session_id=session["session_id"], q2_response=age, q2_time=now)
                db.session.add(new_)

            db.session.commit()
            return redirect(url_for('question03'))


@app.route('/question03', methods=['GET', 'POST'])
def question03():
    if request.method == 'GET':
        return render_template('survey/survey_question03.html')
    elif request.method == 'POST':
        gender = request.form.get('gender')
        if not gender:
            return "Please provide your gender before proceeding."
        else:
            existing = Survey.query.filter_by(session_id=session["session_id"]).first()
            now = datetime.datetime.now(datetime.timezone.utc)
            if existing:
                existing.q3_response = gender
                existing.q3_time = now
            else:
                new_ = Survey(session_id=session["session_id"], q3_response=gender, q3_time=now)
                db.session.add(new_)

            db.session.commit()
            return redirect(url_for('question04'))


@app.route('/question04', methods=['GET', 'POST'])
def question04():
    if request.method == 'GET':
        return render_template('survey/survey_question04.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')
        if not answer:
            return "Please provide your answer before proceeding."
        else:
            existing = Survey.query.filter_by(session_id=session["session_id"]).first()
            now = datetime.datetime.now(datetime.timezone.utc)
            if existing:
                existing.q4_response = answer
                existing.q4_time = now
            else:
                new_ = Survey(session_id=session["session_id"], q4_response=answer, q4_time=now)
                db.session.add(new_)

            db.session.commit()
            return redirect(url_for('question05'))


@app.route('/question05', methods=['GET', 'POST'])
def question05():
    if request.method == 'GET':
        return render_template('survey/survey_question05.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')
        if not answer:
            return "Please provide your answer before proceeding."
        else:
            existing = Survey.query.filter_by(session_id=session["session_id"]).first()
            now = datetime.datetime.now(datetime.timezone.utc)
            if existing:
                existing.q5_response = answer
                existing.q5_time = now
            else:
                new_ = Survey(session_id=session["session_id"], q5_response=answer, q5_time=now)
                db.session.add(new_)

            db.session.commit()
            return redirect(url_for('question06'))


@app.route('/question06', methods=['GET', 'POST'])
def question06():
    if request.method == 'GET':
        return render_template('survey/survey_question06.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')
        if not answer:
            return "Please provide your answer before proceeding."
        else:
            existing = Survey.query.filter_by(session_id=session["session_id"]).first()
            now = datetime.datetime.now(datetime.timezone.utc)
            if existing:
                existing.q6_response = answer
                existing.q6_time = now
            else:
                new_ = Survey(session_id=session["session_id"], q6_response=answer, q6_time=now)
                db.session.add(new_)

            db.session.commit()
            return redirect(url_for('question07'))


@app.route('/question07', methods=['GET', 'POST'])
def question07():
    if request.method == 'GET':
        return render_template('survey/survey_question07.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')
        if not answer:
            return "Please provide your answer before proceeding."
        else:
            existing = Survey.query.filter_by(session_id=session["session_id"]).first()
            now = datetime.datetime.now(datetime.timezone.utc)
            if existing:
                existing.q7_response = answer
                existing.q7_time = now
            else:
                new_ = Survey(session_id=session["session_id"], q7_response=answer, q7_time=now)
                db.session.add(new_)

            db.session.commit()
            return redirect(url_for('question08'))


@app.route('/question08', methods=['GET', 'POST'])
def question08():
    if request.method == 'GET':
        return render_template('survey/survey_question08.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')
        if not answer:
            return "Please provide your answer before proceeding."
        else:
            existing = Survey.query.filter_by(session_id=session["session_id"]).first()
            now = datetime.datetime.now(datetime.timezone.utc)
            if existing:
                existing.q8_response = answer
                existing.q8_time = now
            else:
                new_ = Survey(session_id=session["session_id"], q8_response=answer, q8_time=now)
                db.session.add(new_)

            db.session.commit()
            return redirect(url_for('question09'))


@app.route('/question09', methods=['GET', 'POST'])
def question09():
    if request.method == 'GET':
        return render_template('survey/survey_question09.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')
        if not answer:
            return "Please provide your answer before proceeding."
        else:
            existing = Survey.query.filter_by(session_id=session["session_id"]).first()
            now = datetime.datetime.now(datetime.timezone.utc)
            if existing:
                existing.q9_response = answer
                existing.q9_time = now
            else:
                new_ = Survey(session_id=session["session_id"], q9_response=answer, q9_time=now)
                db.session.add(new_)

            db.session.commit()
            return redirect(url_for('question10'))


@app.route('/question10', methods=['GET', 'POST'])
def question10():
    if request.method == 'GET':
        return render_template('survey/survey_question10.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')
        if not answer:
            return "Please provide your answer before proceeding."
        else:
            existing = Survey.query.filter_by(session_id=session["session_id"]).first()
            now = datetime.datetime.now(datetime.timezone.utc)
            if existing:
                existing.q10_response = answer
                existing.q10_time = now
            else:
                new_ = Survey(session_id=session["session_id"], q10_response=answer, q10_time=now)
                db.session.add(new_)

            db.session.commit()
            return redirect(url_for('question11'))


@app.route('/question11', methods=['GET', 'POST'])
def question11():
    if request.method == 'GET':
        return render_template('survey/survey_question11.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')
        if not answer:
            return "Please provide your answer before proceeding."
        else:
            existing = Survey.query.filter_by(session_id=session["session_id"]).first()
            now = datetime.datetime.now(datetime.timezone.utc)
            if existing:
                existing.q11_response = answer
                existing.q11_time = now
            else:
                new_ = Survey(session_id=session["session_id"], q11_response=answer, q11_time=now)
                db.session.add(new_)

            db.session.commit()
            return redirect(url_for('prototype'))


########################### PROTOTYPE ###########################

@app.route('/prototype', methods=['GET'])
def prototype():
    return render_template('prototype/prototype_introduction.html')

@app.route('/prototype01', methods=['GET'])
def prototype01():
    return render_template('prototype/prototype_01.html')

@app.route('/prototype02', methods=['GET'])
def prototype02():
    return render_template('prototype/prototype_02.html')

@app.route('/prototype03', methods=['GET'])
def prototype03():
    return render_template('prototype/prototype_03.html')

@app.route('/prototype04', methods=['GET'])
def prototype04():
    return render_template('prototype/prototype_04.html')

@app.route('/prototype05', methods=['GET'])
def prototype05():
    return render_template('prototype/prototype_05.html')

@app.route('/prototype06', methods=['GET', 'POST'])
def prototype06():
    if request.method == 'GET':
        return render_template('prototype/prototype_06.html')
    elif request.method == 'POST':
        answer = request.form.get('emailInput')
        if not answer:
            return "Please provide your answer before proceeding."
        else:
            existing = Survey.query.filter_by(session_id=session["session_id"]).first()
            now = datetime.datetime.now(datetime.timezone.utc)
            if existing:
                existing.p6_response = answer
                existing.p6_time = now
            else:
                new_ = Survey(session_id=session["session_id"], p6_response=answer, p6_time=now)
                db.session.add(new_)

            db.session.commit()
            return redirect(url_for('prototype07'))
        
@app.route('/prototype07', methods=['GET', 'POST'])
def prototype07():
    if request.method == 'GET':
        return render_template('prototype/prototype_07.html')
    elif request.method == 'POST':
        answer = request.form.get('passwordInput')
        if not answer:
            return "Please provide your answer before proceeding."
        else:
            existing = Survey.query.filter_by(session_id=session["session_id"]).first()
            now = datetime.datetime.now(datetime.timezone.utc)
            if existing:
                existing.p7_response = answer
                existing.p7_time = now
            else:
                new_ = Survey(session_id=session["session_id"], p7_response=answer, p7_time=now)
                db.session.add(new_)

            db.session.commit()
            group_id = int(Survey.query.filter_by(session_id=session["session_id"]).first().assigned_group)
            return redirect(url_for(assigned_group_map[group_id])) # Split using round-robin logic


########################### PROTOTYPE GRP1 - 1 ###########################
        
@app.route('/prototype08_g1', methods=['GET', 'POST'])
def prototype08_g1():
    if request.method == 'GET':
        return render_template('prototype/prototype_08_g1.html')
    elif request.method == 'POST':

        tos_answer = str(request.form.get('termsOfUseToggle') == 'on')
        newsletter_answer = str(request.form.get('newsletterToggle') == 'on')
        data_donation_answer = str(request.form.get('dataDonationToggle') == 'on')

        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)

        if existing:
            existing.p8_tos_toggle = tos_answer
            existing.p8_newsletter_toggle = newsletter_answer
            existing.p8_data_donation_toggle = data_donation_answer
            existing.p8_time = now
        else:
            new_ = Survey(
                session_id=session["session_id"],
                p8_tos_toggle=tos_answer, 
                p8_newsletter_toggle=newsletter_answer, 
                p8_datadonation_toggle=data_donation_answer,
                p8_time=now
            )
            db.session.add(new_)

        db.session.commit()

        return redirect(url_for('prototype09'))

########################### PROTOTYPE GRP2 - 1 ###########################

@app.route('/prototype08_g2', methods=['GET', 'POST'])
def prototype08_g2():
    if request.method == 'GET':
        return render_template('prototype/prototype_08_g2.html')
    elif request.method == 'POST':

        tos_answer = str(request.form.get('termsOfUseToggle') == 'on')
        newsletter_answer = str(request.form.get('newsletterToggle') == 'on')
        data_donation_answer = str(request.form.get('dataDonationToggle') == 'on')

        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)

        if existing:
            existing.p8_tos_toggle = tos_answer
            existing.p8_newsletter_toggle = newsletter_answer
            existing.p8_data_donation_toggle = data_donation_answer
            existing.p8_time = now
        else:
            new_ = Survey(
                session_id=session["session_id"], 
                p8_tos_toggle=tos_answer, 
                p8_newsletter_toggle=newsletter_answer,
                p8_data_donation_toggle=data_donation_answer,
                p8_time=now
            )
            db.session.add(new_)

        db.session.commit()

        return redirect(url_for('prototype09'))

########################### PROTOTYPE GRP3 - 1 ###########################

@app.route('/prototype08_g3_01', methods=['GET', 'POST'])
def prototype08_g3_01():
    if request.method == 'GET':
        return render_template('prototype/prototype_08_g3_01.html')
    elif request.method == 'POST':
        button_pressed = request.form.get('button_pressed')
        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)

        if button_pressed == 'accept_all':
            if existing:
                existing.p8_tos_toggle = "True"
                existing.p8_newsletter_toggle = "True"
                existing.p8_data_donation_toggle = "True"
                existing.p8_time = now
                existing.p8_g3_01_view = "True"
            else:
                new_ = Survey(
                    session_id=session["session_id"],
                    p8_tos_toggle="True",
                    p8_newsletter_toggle="True",
                    p8_data_donation_toggle="True",
                    p8_time=now,
                    p8_g3_01_view="True"
                )
                db.session.add(new_)
            db.session.commit()
            return redirect(url_for('prototype09'))
        elif button_pressed == 'read_terms':
            return redirect(url_for('prototype08_g3_02'))
    
@app.route('/prototype08_g3_02', methods=['GET', 'POST'])
def prototype08_g3_02():
    if request.method == 'GET':
        return render_template('prototype/prototype_08_g3_02.html')
    elif request.method == 'POST':
        button_pressed = request.form.get('button_pressed')
        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)

        if button_pressed == 'accept_all':
            if existing:
                existing.p8_tos_toggle = "True"
                existing.p8_newsletter_toggle = "True"
                existing.p8_data_donation_toggle = "True"
                existing.p8_time = now
                existing.p8_g3_02_view = "True"
                existing.p8_g3_01_view = "True"
            else:
                new_ = Survey(
                    session_id=session["session_id"],
                    p8_tos_toggle="True",
                    p8_newsletter_toggle="True",
                    p8_data_donation_toggle="True",
                    p8_time=now,
                    p8_g3_02_view="True",
                    p8_g3_01_view="True"
                )
                db.session.add(new_)
            db.session.commit()
            return redirect(url_for('prototype09'))
        elif button_pressed == 'read_terms':
            return redirect(url_for('prototype08_g3_03'))

@app.route('/prototype08_g3_03', methods=['GET', 'POST'])
def prototype08_g3_03():
    if request.method == 'GET':
        return render_template('prototype/prototype_08_g3_03.html')
    elif request.method == 'POST':
        tos_answer = str(request.form.get('termsOfUseToggle') == 'on')
        newsletter_answer = str(request.form.get('newsletterToggle') == 'on')
        data_donation_answer = str(request.form.get('dataDonationToggle') == 'on')

        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)

        if existing:
            existing.p8_tos_toggle = tos_answer
            existing.p8_newsletter_toggle = newsletter_answer
            existing.p8_data_donation_toggle = data_donation_answer
            existing.p8_time = now
            existing.p8_g3_03_view = "True"
            existing.p8_g3_02_view = "True"
            existing.p8_g3_01_view = "True"
        else:
            new_ = Survey(
                session_id=session["session_id"],
                p8_tos_toggle=tos_answer,
                p8_newsletter_toggle=newsletter_answer,
                p8_data_donation_toggle=data_donation_answer,
                p8_time=now,
                p8_g3_03_view="True",
                p8_g3_02_view="True",
                p8_g3_01_view="True"
            )
            db.session.add(new_)
        db.session.commit()
        return redirect(url_for('prototype09'))


########################### PROTOTYPE ###########################

@app.route('/prototype09', methods=['GET', 'POST'])
def prototype09():
    if request.method =='GET':
        return render_template('prototype/prototype_09.html')
    elif request.method == 'POST':
        return redirect(url_for('prototype10'))
    
@app.route('/prototype10', methods=['GET', 'POST'])
def prototype10():
    if request.method =='GET':
        return render_template('prototype/prototype_10.html')
    elif request.method == 'POST':
        return redirect(url_for('prototype11'))
    
@app.route('/prototype11', methods=['GET', 'POST'])
def prototype11():
    if request.method =='GET':
        return render_template('prototype/prototype_11.html')
    elif request.method == 'POST':
        return redirect(url_for('prototype12'))
    
@app.route('/prototype12', methods=['GET', 'POST'])
def prototype12():
    if request.method =='GET':
        return render_template('prototype/prototype_12.html')
    elif request.method == 'POST':
        return redirect(url_for('prototype13'))
    
@app.route('/prototype13', methods=['GET', 'POST'])
def prototype13():
    if request.method =='GET':
        return render_template('prototype/prototype_13.html')
    elif request.method == 'POST':
        return redirect(url_for('prototype14'))
    
@app.route('/prototype14', methods=['GET', 'POST'])
def prototype14():
    if request.method =='GET':
        return render_template('prototype/prototype_14.html')
    elif request.method == 'POST':
        return redirect(url_for('prototype15'))
    
@app.route('/prototype15', methods=['GET', 'POST'])
def prototype15():
    if request.method =='GET':
        return render_template('prototype/prototype_15.html')
    elif request.method == 'POST':
        return redirect(url_for('prototype16'))
    
@app.route('/prototype16', methods=['GET', 'POST'])
def prototype16():
    if request.method =='GET':
        return render_template('prototype/prototype_16.html')
    elif request.method == 'POST':
        return redirect(url_for('prototype17'))
    
@app.route('/prototype17', methods=['GET'])
def prototype17():
        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        if existing:
            group = assigned_group_map2[existing.assigned_group]
        else:
            group = "prototype18_g1"
        return render_template('prototype/prototype_17.html', group=group)

########################### PROTOTYPE GRP1 - 2 ###########################

@app.route('/prototype18_g1', methods=['GET', 'POST'])
def prototype18_g1():
    if request.method == 'GET':
        return render_template('prototype/prototype_18_g1.html')
    elif request.method == 'POST':
        button_pressed = request.form.get('button_pressed')
        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        free_trial = str(button_pressed == "free_trial")
        if existing:
            existing.free_trial = free_trial
            existing.p18_time = now
        else:
            new_ = Survey(
                session_id=session["session_id"],
                free_trial=free_trial,
                p18_time=now
            )
            db.session.add(new_)
        db.session.commit()
        return redirect(url_for('prototype_end'))

########################### PROTOTYPE GRP2 - 2 ###########################

@app.route('/prototype18_g2_01', methods=['GET', 'POST'])
def prototype18_g2_01():
    if request.method == 'GET':
        return render_template('prototype/prototype_18_g2_01.html')
    elif request.method == 'POST':
        button_pressed = request.form.get('button_pressed')
        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        free_trial = button_pressed == "free_trial"
        if free_trial:
            if existing:
                existing.free_trial = str(free_trial)
                existing.p18_time = now
                existing.p18_g2_01_view = "True"
            else:
                new_ = Survey(
                    session_id=session["session_id"],
                    free_trial=str(free_trial),
                    p18_time=now,
                    p18_g2_01_view = "True"
                )
                db.session.add(new_)
            db.session.commit()
            return redirect(url_for('prototype_end'))
        else:
            return redirect(url_for('prototype18_g2_02'))
    
@app.route('/prototype18_g2_02', methods=['GET', 'POST'])
def prototype18_g2_02():
    if request.method == 'GET':
        return render_template('prototype/prototype_18_g2_02.html')
    elif request.method == 'POST':
        button_pressed = request.form.get('button_pressed')
        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        free_trial = str(button_pressed == "free_trial")
        if existing:
            existing.free_trial = free_trial
            existing.p18_time = now
            existing.p18_g2_01_view = "True"
            existing.p18_g2_02_view = "True"
        else:
            new_ = Survey(
                session_id=session["session_id"],
                free_trial=free_trial,
                p18_time=now,
                p18_g2_01_view = "True",
                p18_g2_02_view = "True"
            )
            db.session.add(new_)
        db.session.commit()
        return redirect(url_for('prototype_end'))

########################### PROTOTYPE GRP3 - 2 ###########################

@app.route('/prototype18_g3_01', methods=['GET', 'POST'])
def prototype18_g3_01():
    if request.method == 'GET':
        return render_template('prototype/prototype_18_g3_01.html')
    elif request.method == 'POST':
        button_pressed = request.form.get('button_pressed')
        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        free_trial = button_pressed == "free_trial"
        if free_trial:
            if existing:
                existing.free_trial = str(free_trial)
                existing.p18_time = now
                existing.p18_g3_01_view = "True"
            else:
                new_ = Survey(
                    session_id=session["session_id"],
                    free_trial=str(free_trial),
                    p18_time=now,
                    p18_g3_01_view = "True"
                )
                db.session.add(new_)
            db.session.commit()
            return redirect(url_for('prototype_end'))
        else:
            return redirect(url_for('prototype18_g3_02'))
    
@app.route('/prototype18_g3_02', methods=['GET', 'POST'])
def prototype18_g3_02():
    if request.method == 'GET':
        return render_template('prototype/prototype_18_g3_02.html')
    elif request.method == 'POST':
        button_pressed = request.form.get('button_pressed')
        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        free_trial = button_pressed == "free_trial"
        if free_trial:
            if existing:
                existing.free_trial = str(free_trial)
                existing.p18_time = now
                existing.p18_g3_01_view = "True"
                existing.p18_g3_02_view = "True"
            else:
                new_ = Survey(
                    session_id=session["session_id"],
                    free_trial=str(free_trial),
                    p18_time=now,
                    p18_g3_01_view = "True",
                    p18_g3_02_view = "True"
                )
                db.session.add(new_)
            db.session.commit()
            return redirect(url_for('prototype_end'))
        else:
            return redirect(url_for('prototype18_g3_03'))

@app.route('/prototype18_g3_03', methods=['GET', 'POST'])
def prototype18_g3_03():
    if request.method == 'GET':
        return render_template('prototype/prototype_18_g3_03.html')
    elif request.method == 'POST':
        button_pressed = request.form.get('button_pressed')
        answer = request.form.get('radioAnswer')
        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        if button_pressed:
            if existing:
                existing.free_trial = "True"
                existing.p18_time = now
                existing.p18_g3_01_view = "True"
                existing.p18_g3_02_view = "True"
                existing.p18_g3_03_view = "True"
            else:
                new_ = Survey(
                    session_id=session["session_id"],
                    free_trial="True",
                    p18_cancellation_reason="None",
                    p18_time=now,
                    p18_g3_01_view = "True",
                    p18_g3_02_view = "True",
                    p18_g3_03_view = "True"
                )
                db.session.add(new_)
            db.session.commit()
            return redirect(url_for('prototype_end'))
        else:
            if existing:
                existing.p18_cancellation_reason = answer
                existing.p18_time = now
                existing.p18_g3_01_view = "True"
                existing.p18_g3_02_view = "True"
                existing.p18_g3_03_view = "True"
            else:
                new_ = Survey(
                    session_id=session["session_id"],
                    free_trial="False",
                    p18_cancellation_reason=answer,
                    p18_time=now,
                    p18_g3_01_view = "True",
                    p18_g3_02_view = "True",
                    p18_g3_03_view = "True"
                )
                db.session.add(new_)
            db.session.commit()
            return redirect(url_for('prototype18_g3_04'))

@app.route('/prototype18_g3_04', methods=['GET', 'POST'])
def prototype18_g3_04():
    if request.method == 'GET':
        return render_template('prototype/prototype_18_g3_04.html')
    elif request.method == 'POST':
        button_pressed = request.form.get('button_pressed')
        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        free_trial = str(button_pressed == "free_trial")
        if existing:
            existing.free_trial = free_trial
            existing.p18_time = now
            existing.p18_g3_01_view = "True"
            existing.p18_g3_02_view = "True"
            existing.p18_g3_03_view = "True"
            existing.p18_g3_04_view = "True"

        else:
            new_ = Survey(
                session_id=session["session_id"],
                free_trial=free_trial,
                p18_time=now,
                p18_g3_01_view = "True",
                p18_g3_02_view = "True",
                p18_g3_03_view = "True",
                p18_g3_04_view = "True"
            )
            db.session.add(new_)
        db.session.commit()
        return redirect(url_for('prototype_end'))

@app.route('/prototype_end', methods=['GET', 'POST'])
def prototype_end():
        return render_template('prototype/prototype_end.html')

########################### QUESTIONS ###########################

@app.route('/question12', methods=['GET', 'POST'])
def question12():
    if request.method == 'GET':
        return render_template('survey/survey_question12.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')

        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        if existing:
            existing.q12_response = answer
            existing.q12_time = now
        else:
            new_ = Survey(session_id=session["session_id"], q12_response=answer, q12_time=now)
            db.session.add(new_)

        db.session.commit()
        return redirect(url_for('question13'))
    
@app.route('/question13', methods=['GET', 'POST'])
def question13():
    if request.method == 'GET':
        return render_template('survey/survey_question13.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')

        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        if existing:
            existing.q13_response = answer
            existing.q13_time = now
        else:
            new_ = Survey(session_id=session["session_id"], q13_response=answer, q13_time=now)
            db.session.add(new_)

        db.session.commit()
        return redirect(url_for('question14'))

@app.route('/question14', methods=['GET', 'POST'])
def question14():
    if request.method == 'GET':
        return render_template('survey/survey_question14.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')

        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        if existing:
            existing.q14_response = answer
            existing.q14_time = now
        else:
            new_ = Survey(session_id=session["session_id"], q14_response=answer, q14_time=now)
            db.session.add(new_)

        db.session.commit()
        return redirect(url_for('question15'))
    
@app.route('/question15', methods=['GET', 'POST'])
def question15():
    if request.method == 'GET':
        return render_template('survey/survey_question15.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')

        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        if existing:
            existing.q15_response = answer
            existing.q15_time = now
        else:
            new_ = Survey(session_id=session["session_id"], q15_response=answer, q15_time=now)
            db.session.add(new_)

        db.session.commit()
        return redirect(url_for('question16'))
    
@app.route('/question16', methods=['GET', 'POST'])
def question16():
    if request.method == 'GET':
        return render_template('survey/survey_question16.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')

        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        if existing:
            existing.q16_response = answer
            existing.q16_time = now
        else:
            new_ = Survey(session_id=session["session_id"], q16_response=answer, q16_time=now)
            db.session.add(new_)

        db.session.commit()
        return redirect(url_for('question17'))
    
@app.route('/question17', methods=['GET', 'POST'])
def question17():
    if request.method == 'GET':
        return render_template('survey/survey_question17.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')

        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        if existing:
            existing.q17_response = answer
            existing.q17_time = now
        else:
            new_ = Survey(session_id=session["session_id"], q17_response=answer, q17_time=now)
            db.session.add(new_)

        db.session.commit()
        return redirect(url_for('question18'))
    
@app.route('/question18', methods=['GET', 'POST'])
def question18():
    if request.method == 'GET':
        return render_template('survey/survey_question18.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')

        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        if existing:
            existing.q18_response = answer
            existing.q18_time = now
        else:
            new_ = Survey(session_id=session["session_id"], q18_response=answer, q18_time=now)
            db.session.add(new_)

        db.session.commit()
        return redirect(url_for('question19'))
    
@app.route('/question19', methods=['GET', 'POST'])
def question19():
    if request.method == 'GET':
        return render_template('survey/survey_question19.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')

        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        if existing:
            existing.q19_response = answer
            existing.q19_time = now
        else:
            new_ = Survey(session_id=session["session_id"], q19_response=answer, q19_time=now)
            db.session.add(new_)

        db.session.commit()
        return redirect(url_for('question20'))

@app.route('/question20', methods=['GET', 'POST'])
def question20():
    if request.method == 'GET':
        return render_template('survey/survey_question20.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')

        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        if existing:
            existing.q20_response = answer
            existing.q20_time = now
        else:
            new_ = Survey(session_id=session["session_id"], q20_response=answer, q20_time=now)
            db.session.add(new_)

        db.session.commit()
        return redirect(url_for('question21'))
    
@app.route('/question21', methods=['GET', 'POST'])
def question21():
    if request.method == 'GET':
        return render_template('survey/survey_question21.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')

        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        if existing:
            existing.q21_response = answer
            existing.q21_time = now
        else:
            new_ = Survey(session_id=session["session_id"], q21_response=answer, q21_time=now)
            db.session.add(new_)

        db.session.commit()
        return redirect(url_for('question22'))
    
@app.route('/question22', methods=['GET', 'POST'])
def question22():
    if request.method == 'GET':
        return render_template('survey/survey_question22.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')

        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        if existing:
            existing.q22_response = answer
            existing.q22_time = now
        else:
            new_ = Survey(session_id=session["session_id"], q22_response=answer, q22_time=now)
            db.session.add(new_)

        db.session.commit()
        return redirect(url_for('question23'))
    
@app.route('/question23', methods=['GET', 'POST'])
def question23():
    if request.method == 'GET':
        return render_template('survey/survey_question23.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')

        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        if existing:
            existing.q23_response = answer
            existing.q23_time = now
        else:
            new_ = Survey(session_id=session["session_id"], q23_response=answer, q23_time=now)
            db.session.add(new_)

        db.session.commit()
        return redirect(url_for('question24'))
    
@app.route('/question24', methods=['GET', 'POST'])
def question24():
    if request.method == 'GET':
        return render_template('survey/survey_question24.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')

        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        if existing:
            existing.q24_response = answer
            existing.q24_time = now
        else:
            new_ = Survey(session_id=session["session_id"], q24_response=answer, q24_time=now)
            db.session.add(new_)

        db.session.commit()
        return redirect(url_for('question25'))
    
@app.route('/question25', methods=['GET', 'POST'])
def question25():
    if request.method == 'GET':
        return render_template('survey/survey_question25.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')

        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        if existing:
            existing.q25_response = answer
            existing.q25_time = now
        else:
            new_ = Survey(session_id=session["session_id"], q25_response=answer, q25_time=now)
            db.session.add(new_)

        db.session.commit()
        return redirect(url_for('question26'))
    
@app.route('/question26', methods=['GET', 'POST'])
def question26():
    if request.method == 'GET':
        return render_template('survey/survey_question26.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')

        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        if existing:
            existing.q26_response = answer
            existing.q26_time = now
        else:
            new_ = Survey(session_id=session["session_id"], q26_response=answer, q26_time=now)
            db.session.add(new_)

        db.session.commit()
        return redirect(url_for('question27'))
    
@app.route('/question27', methods=['GET', 'POST'])
def question27():
    if request.method == 'GET':
        return render_template('survey/survey_question27.html')
    elif request.method == 'POST':
        answer = request.form.get('radioAnswer')

        existing = Survey.query.filter_by(session_id=session["session_id"]).first()
        now = datetime.datetime.now(datetime.timezone.utc)
        if existing:
            existing.q27_response = answer
            existing.q27_time = now
        else:
            new_ = Survey(session_id=session["session_id"], q27_response=answer, q27_time=now)
            db.session.add(new_)

        db.session.commit()
        return redirect(url_for('survey_end'))
    
@app.route('/survey_end', methods=['GET', 'POST'])
def survey_end():
    return render_template('survey/survey_end.html')


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
