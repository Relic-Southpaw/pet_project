from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "chickenzarelame"
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/', methods=["GET", "POST"])
def homepage():
    pets = Pet.query.all()
    return render_template('home.html', pets = pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Renders Pet form (GET)"""
    """Handles Pet Submission (POST)"""
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name,
            species = species, 
            photo_url = photo_url,
            age = age,
            notes=notes,
            available=available)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("add_pet_form.html", form = form)

@app.route('/<int:id>', methods=["GET", "POST"])
def edit_employee(id):
    pet = Pet.query.get_or_404(id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/<int:id>')
    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)

@app.route('/<int:id>/delete', methods=['POST'])
def delete_tag(id):
    pet = Pet.query.get_or_404(id)

    db.session.delete(pet)
    db.session.commit()
    return redirect('/')
