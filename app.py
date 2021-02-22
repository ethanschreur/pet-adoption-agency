from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, connect_db, db
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.debug=True
app.config['SECRET_KEY'] = 'shhhhhhhhhh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

toolbar = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home():
    """lists the pets, their names and picture as wella s a button to ge to more details about them
    and a button to go to add new pet page"""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=['POST', 'GET'])
def add():
    """
    load the add new pet form and handle the get and submission post requests
    """
    form = AddPetForm()
    if form.validate_on_submit():
        name = request.form['name']
        species = request.form['species']
        photo_url = request.form['photo_url']
        age = request.form['age']
        notes = request.form['notes']
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def pet(pet_id):
    """see details about the pet and see an edit form for the pet, handle the get and post request of edit form submission"""
    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        return redirect(f'/{pet_id}')
    return render_template('pet.html', pet=pet, form=form)