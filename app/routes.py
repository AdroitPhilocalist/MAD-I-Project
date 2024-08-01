from flask import render_template, request, redirect, url_for
from app import app

@app.route('/')
def role_selection():
    return render_template('role_selection.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    role = request.args.get('role')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Redirect to respective dashboard based on role
        if role == 'admin':
            return redirect(url_for('admin_dashboard'))
        elif role == 'sponsor':
            return redirect(url_for('sponsor_dashboard'))
        elif role == 'influencer':
            return redirect(url_for('influencer_dashboard'))
    
    if role == 'admin':
        return render_template('admin_login.html')
    elif role == 'sponsor':
        return render_template('sponsor_login.html')
    elif role == 'influencer':
        return render_template('influencer_login.html')
    return redirect(url_for('role_selection'))

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Redirect to admin dashboard
        return redirect(url_for('admin_dashboard'))
    return render_template('admin_login.html')

@app.route('/sponsor_login', methods=['GET', 'POST'])
def sponsor_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Redirect to sponsor dashboard
        return redirect(url_for('sponsor_dashboard'))
    return render_template('sponsor_login.html')

@app.route('/influencer_login', methods=['GET', 'POST'])
def influencer_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Redirect to influencer dashboard
        return redirect(url_for('influencer_dashboard'))
    return render_template('influencer_login.html')

@app.route('/sponsor_registration', methods=['GET', 'POST'])
def sponsor_registration():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        industry = request.form['industry']
        # Save sponsor details to database here (placeholder comment)
        return redirect(url_for('sponsor_login'))
    return render_template('sponsor_registration.html')

@app.route('/influencer_registration', methods=['GET', 'POST'])
def influencer_registration():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        platforms = request.form.getlist('social_media')
        # Save influencer details to database here (placeholder comment)
        return redirect(url_for('influencer_login'))
    return render_template('influencer_registration.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    # Fetch relevant statistics from the database (placeholder comment)
    return render_template('admin_dashboard.html')

@app.route('/sponsor_dashboard')
def sponsor_dashboard():
    return render_template('sponsor_dashboard.html')

@app.route('/influencer_dashboard')
def influencer_dashboard():
    return render_template('influencer_dashboard.html')

@app.route('/update_profile', methods=['GET', 'POST'])
def update_profile():
    if request.method == 'POST':
        # Logic to update profile details
        return redirect(url_for('influencer_dashboard'))
    return render_template('update_profile.html')

@app.route('/logout')
def logout():
    # Here you can implement any session clearing or logout logic if necessary
    return redirect(url_for('role_selection'))