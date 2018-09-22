from flask import Blueprint
from flask import request, redirect, url_for, render_template, flash
from app.models import db
from app.models.entry import Entry


app = Blueprint('entry', __name__, url_prefix='/')


@app.route('/')
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('entries/show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    entry = Entry(title=request.form['title'],
                  text=request.form['text'])
    db.session.add(entry)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('entry.show_entries'))
