from flask import Flask,flash, redirect, url_for, render_template, make_response, request, session, escape
from BluePrint_Testing import my_first_blueprint
from datetime import timedelta
from werkzeug.exceptions import HTTPException
import random
import time

app = Flask(__name__)
app.secret_key = "ILoveMasumBhai"
app.permanent_session_lifetime = timedelta(minutes=5)
app.debug = True
app.register_blueprint(my_first_blueprint)


# app.add_url_rule("/","hello",hello_world)
# flask constructor takes name of current module like __name__ as argument
# @my_first_blueprint.route('/')
@app.route('/', methods=['POST', 'GET'])
def home():
    content = "Masum Bhai is Learning Python Flask"
    return render_template('index.html', valu=content)


@app.route('/admin_page/<admin_name>')
def admin_section(admin_name):
    return "%s You can change anything,block anyone. Cause You are ADMIN now." % admin_name


@app.route('/guest_page/<username>')
def guest_section(username):
    if 'visits' in session:
        session['visits'] = int(session.get('visits')) + 1  # reading and updating session data
    else:
        session['visits'] = 1  # setting session data
    user_id = random.randint(1, 1000001)
    print("Guest's user id is: %d" % user_id)
    return render_template('guest_page.html', visitors=session['visits'], id=user_id, welcome=username)


# in web browser console copy session data upto first dot and in console type: atob("that copied session")
# Then see the Boom,Magic
@app.route('/login/', methods=["POST", "GET"])
def login_page():
    if request.method == "POST":
        session.permanent = True
        u_name = request.form['user_name']
        session['userName'] = u_name
        print(session)
        if u_name == "admin":
            return redirect(url_for('admin_section', admin_name='MasumBhai'))
        else:
            return redirect(url_for('guest_section', username=u_name))
    return render_template('LogIn_Page.html')


@app.route('/logout/')
def logout():
    # remove the username from the session if it is there
    if "userName" in session:
        usr = session['userName']
        session.pop('userName', None)
        flash(f"{usr} , You have been Logged Out Successfully","info")
    return redirect(url_for('login_page'))


# when stting session,it seems user_defined Cookie gets suppressed by session cookie
# and that's why may be,we can not see our defined cookies in console rather only session cookie
@app.route('/setcookie/', methods=['POST', 'GET'])
def set_cookie():
    response = make_response(f"cookie setted")
    # if "userName" in session:
    #     response.set_cookie(key="Flask_Cookie",
    #                         value=session['userName'],  # + "You will be hacked , mark my word."
    #                         max_age=60 * 60 * 24)
    # else:
    response.set_cookie(key="MasumBhai's_flask_Cookie",
                        value="I will hack into your computer in a few days,let me learn hacking first",
                        max_age=60 * 60 * 24
                        )
    return render_template('Set_Cookies.html', value_for_set_cookie=response)


@app.route('/getcookie/')
def get_cookie():
    # if request.cookies.get("Flask_Cookie"):
    #     rsp = request.cookies.get("Flask_Cookie")
    # else:
    rsp = request.cookies.get("MasumBhai's_flask_Cookie")
    info = "The Cookie content is: " + rsp;
    return render_template('index.html', value_for_cookie=info)


@app.route('/delete_cookie/')
def deleteCookie():
    res = make_response(f"Cookie has been Removed,refresh your browser cookie")
    if "userName" in session:
        res.set_cookie(key="Flask_Cookie", max_age=0)
    else:
        res.set_cookie(key="MasumBhai's_flask_Cookie", max_age=0)
    return render_template('Deletion_Cookies.html', value_for_deleting_cookie=res)


@app.errorhandler(HTTPException)
def handle_bad_request(e):
    return render_template('404.html')


if __name__ == '__main__':
    # app.run(host="'0.0.0.0'", port=5000, debug=True)
    app.run(debug=True)
