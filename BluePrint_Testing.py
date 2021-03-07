from flask import Flask,Blueprint,render_template,redirect,url_for
import random
my_first_blueprint = Blueprint('my_first_blueprint',__name__,static_folder=None,template_folder=None)

# @my_first_blueprint.route('/')
@my_first_blueprint.route('/Home/<user>')
def home(user):
    return 'We are very delighted for your visit in this site, user id: %s' % user


@my_first_blueprint.route('/Blog/<int:page_no>')
def Blog_Post(page_no):
    return "We are on Blog page {}".format(page_no)


@my_first_blueprint.route('/admin/<admin_name>')
def admin(admin_name):
    return "%s You can change anything,block anyone. Cause You are ADMIN now." % admin_name


@my_first_blueprint.route('/guest')
def guest():
    user_id = random.randint(1, 1000001)
    print("Guest's user id is: %d" % user_id)
    return home(user_id)


@my_first_blueprint.route('/user/<id>')
def redirecting_url(id):
    if id == "admin":
        return redirect(url_for('my_first_blueprint.admin', admin_name='MasumBhai'))
    else:
        return redirect(url_for('my_first_blueprint.guest'))

