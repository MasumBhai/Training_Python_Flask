from flask import Flask, redirect, url_for
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
    info_about_me = "<a href='https://fsb.zobj.net/crop.php?r=On715xGxf2MyvMxF1eoHtLnInVKn6DNJuCezJBG8DDHCy8YavW7gykenvfln_OtfLZKmsHU64tmzAc1NMc3ZBu0UOG85gBf_aKXKH6U243AqD5_pa1bkxwlnTZpxLhe9O3oiQEIguwFOR24L'>Just Know Me</a>"
    return "Welcome To The Home Page.Thanks for visiting.and also see about developer MasumBhai <br> %s" % info_about_me


if __name__ == '__main__':
    # app.run(host="'0.0.0.0'", port=5000, debug=True)
    app.run(debug=True)
