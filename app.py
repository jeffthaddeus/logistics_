from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loads.db' 
app.config['SECRET_KEY'] = 'your_secret_key' 
db = SQLAlchemy(app)

class Load(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    load_id = db.Column(db.String(50), nullable=False)
    delivery_date = db.Column(db.Date)
    origin = db.Column(db.String(100))
    destination = db.Column(db.String(100))
    miles = db.Column(db.Integer)
    dh = db.Column(db.Float)
    rate = db.Column(db.Float)
    load_status = db.Column(db.String(50))
    broker_email = db.Column(db.String(100))
    broker_phone = db.Column(db.String(20))
    driver = db.Column(db.String(50))
    dispatcher = db.Column(db.String(50))

    def __repr__(self):
        return f'<Load {self.load_id}>'

@app.route('/')
def index():
    loads = Load.query.all()
    return render_template('index.html', loads=loads)

@app.route('/add', methods=['GET', 'POST'])
def add_load():
    if request.method == 'POST':
        load_id = request.form['load_id']
        delivery_date = request.form['delivery_date']
        origin = request.form['origin']
        destination = request.form['destination']
        miles = request.form['miles']
        dh = request.form['dh']
        rate = request.form['rate']
        load_status = request.form['load_status']
        broker_email = request.form['broker_email']
        broker_phone = request.form['broker_phone']
        driver = request.form['driver']
        dispatcher = request.form['dispatcher']

        new_load = Load(load_id=load_id, delivery_date=delivery_date, 
                        origin=origin, destination=destination, 
                        miles=miles, dh=dh, rate=rate, 
                        load_status=load_status, broker_email=broker_email, 
                        broker_phone=broker_phone, driver=driver, 
                        dispatcher=dispatcher)
        db.session.add(new_load)
        db.session.commit()
        flash('Load added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_load.html')

@app.route('/delete/<int:id>')
def delete_load(id):
    load = Load.query.get_or_404(id)
    db.session.delete(load)
    db.session.commit()
    flash('Load deleted successfully!', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)