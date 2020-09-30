from flask import render_template, request, redirect
from app import app, db
from app.models import Entry


@app.route('/')
@app.route('/index')
def index():
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        description = form.get('description')
        if not title or description:
            entry = Entry(title = title, description = description)
            db.session.add(entry)
            db.session.commit()
            return redirect('/')


@app.route('/update/<int:id>')
def updateRoute(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            return render_template('update.html', entry=entry, id=id)


@app.route('/upd/<int:id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        description = form.get('description')
        if title and description:
            entry = Entry.query.filter_by(id=id).first()
            entry.title = title
            entry.description = description
            db.session.commit()
            return redirect('/')


@app.route('/delete/<int:id>')
def delete(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')


@app.route('/turn/<int:id>')
def turn(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            entry.status = not entry.status
            db.session.commit()
        return redirect('/')
