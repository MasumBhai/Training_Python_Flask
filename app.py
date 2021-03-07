from flask import Flask, redirect, url_for, render_template, make_response, request
from BluePrint_Testing import my_first_blueprint
import random
import time

app = Flask(__name__)
app.debug = True
app.register_blueprint(my_first_blueprint)


# app.add_url_rule("/","hello",hello_world)
# flask constructor takes name of current module like __name__ as argument
# @my_first_blueprint.route('/')
@app.route('/')
def home():
    content = "Masum Bhai is Learning Python Flask"
    return render_template('index.html', valu=content)


@app.route('/setcookie/', methods=['POST', 'GET'])
def set_cookie():
    response = make_response("cookie setted")
    response.set_cookie(key="MasumBhai's_flask_Cookie",
                        value="I will hack into your computer in a few days,let me learn hacking first",
                        max_age=60 * 60 * 24
                        )
    return render_template('Set_Cookies.html', value_for_set_cookie=response)


@app.route('/getcookie/')
def get_cookie():
    rsp = request.cookies.get("MasumBhai's_flask_Cookie")
    info = "The Cookie content is: " + rsp;
    return render_template('Get_Cookie.html', value_for_cookie=info)


@app.route('/delete_cookie/')
def deleteCookie():
    res = make_response("Cookie has been Removed,refresh your browser cookie")
    res.set_cookie(key="MasumBhai's_flask_Cookie", max_age=0)
    return render_template('Deletion_Cookies.html', value_for_deleting_cookie=res)


if __name__ == '__main__':
    # app.run(host="'0.0.0.0'", port=5000, debug=True)
    app.run(debug=True)
