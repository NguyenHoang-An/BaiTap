from flask import Flask, render_template, redirect, url_for, request, flash, session
from db import get_db_connection
from forms import LoginForm, InsertForm

app = Flask(__name__) 
app.secret_key = '12345678'

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            # Lưu thông tin kết nối vào session
            session['db_name'] = form.db_name.data
            session['user'] = form.user.data
            session['password'] = form.password.data
            session['host'] = form.host.data
            session['port'] = form.port.data

            conn = get_db_connection(
                db_name=session['db_name'],
                user=session['user'],
                password=session['password'],
                host=session['host'],
                port=session['port']
            )
            flash('Connected to the database successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error connecting to the database: {e}', 'danger')
    return render_template('login.html', form=form)


@app.route('/index', methods=['GET', 'POST'])
def index():  
    try:
        conn = get_db_connection(
            db_name=session['db_name'],
            user=session['user'],
            password=session['password'],
            host=session['host'],
            port=session['port']
        )
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM list')  # Lấy dữ liệu từ bảng 'list'
        rows = cursor.fetchall()
        return render_template('index.html', rows=rows)
    except Exception as e:
        flash(f'Error accessing the database: {e}', 'danger')
        return redirect(url_for('login'))

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    form = InsertForm()
    if form.validate_on_submit():
        conn = get_db_connection(
            db_name=session['db_name'],
            user=session['user'],
            password=session['password'],
            host=session['host'],
            port=session['port']
        )
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO list (mssv, hoten, diachi, email, sodienthoai) VALUES (%s, %s, %s, %s, %s)",
            (form.mssv.data, form.hoten.data, form.diachi.data, form.email.data, form.sodienthoai.data)
        )
        conn.commit()
        flash('Data inserted successfully!', 'success')
        return redirect(url_for('index'))  # Kiểm tra xem tên hàm này có chính xác không
    return render_template('insert.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)               