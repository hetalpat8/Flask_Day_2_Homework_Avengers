# Import the app variable from the init 
from day_2_homework_app import app 

# Import specific packages from flask
from flask import render_template,request

# Import Our Form(s)**
from day_2_homework_app.forms import UserInfoForm

# Default Home Route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/fav')
def favRoute():
    avengers = ['Iron Man','Captain America','Hulk','Thor','Spider Man']
    return render_template('fav.html',list_avengers = avengers)


# GET == Gathering Info**
# POST == Sending Info**
@app.route('/register', methods = ['GET', 'POST'])
def register():
    # Init our form**
    form = UserInfoForm()
    # Validation of our form**
    if request.method == 'POST' and form.validate():
        #Get Information from the form**
        name = form.name.data
        phone_number = form.phone_number.data
        email = form.email.data
        password = form.password.data
        #Print the data to the server that comes from the form**
        print(name,phone_number,email,password)
    else:
        print('nothing')

    return render_template('register.html',user_form = form)