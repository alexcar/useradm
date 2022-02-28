import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dncfIOVvftfFF*&5$_+1!!'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM tbl_user WHERE id = ?',
        (user_id,)).fetchone()
    conn.close()
    
    if user is None:
        abort(404)
    
    return user

@app.route('/')
def index():
    conn = get_db_connection()
    usuarios = conn.execute('SELECT * FROM tbl_user').fetchall()
    conn.close()
    return render_template('index.html', usuarios=usuarios)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['user_name']
        userName = request.form['user_username']
        password = request.form['user_password']
    
        if not name:
            flash('Nome é obrigatório!')
        elif not userName:
            flash('Nome do usuário é obrigatório!')
        elif not password:
            flash('Senha é obrigatório!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO tbl_user (user_name, user_username, user_password) VALUES (?, ?, ?)',
                (name, userName, password))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))    
    
    return render_template('create.html')

@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    usuario = get_user(id)

    if request.method == 'POST':
        name = request.form['user_name']
        userName = request.form['user_username']
        password = request.form['user_password']

        if not name:
            flash('Nome é obrigatório!')
        elif not userName:
            flash('Nome do usuário é obrigatório!')
        elif not password:
            flash('Senha é obrigatório!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE tbl_user SET user_name = ?, user_username = ?, user_password = ?'
                         ' WHERE id = ?',
                         (name, userName, password, id))
            
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', usuario=usuario)

@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    post = get_user(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM tbl_user WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" foi excluído com sucesso!'.format(post['user_name']))
    return redirect(url_for('index'))
