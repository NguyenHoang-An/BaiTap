from flask import Flask, render_template, request, redirect, url_for, flash, session
from db import get_db_connection
from forms import LoginForm, InsertForm, UpdateForm

app = Flask(__name__)
app.secret_key = '123456'  # Thay bằng secret key thực tế

# Đăng nhập
@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            conn = get_db_connection(form.db_name.data, form.user.data, form.password.data, form.host.data, form.port.data)
            flash('Connected to the database successfully!', 'success')
            session['db_name'] = form.db_name.data
            session['user'] = form.user.data
            session['password'] = form.password.data
            session['host'] = form.host.data
            session['port'] = form.port.data
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error connecting to the database: {e}', 'danger')
    return render_template('login.html', form=form)

# Hiển thị danh sách
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
        cursor.execute('SELECT * FROM dev_table')
        rows = cursor.fetchall()
        return render_template('index.html', rows=rows)
    except Exception as e:
        flash(f'Error accessing the database: {e}', 'danger')
        return redirect(url_for('login'))

# Chức năng thêm mới
@app.route('/insert', methods=['GET', 'POST'])
def insert():
    form = InsertForm()
    if form.validate_on_submit():
        try:
            conn = get_db_connection(
                db_name=session['db_name'],
                user=session['user'],
                password=session['password'],
                host=session['host'],
                port=session['port']
            )
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO dev_table (mssv, hoten, diachi, email, sodienthoai, gioitinh, ngaysinh) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (form.mssv.data, form.hoten.data, form.diachi.data, form.email.data, form.sodienthoai.data, form.gioitinh.data, form.ngaysinh.data)
            )
            conn.commit()
            flash('Data inserted successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error inserting data: {e}', 'danger')
    return render_template('insert.html', form=form)

# Chức năng xoá
@app.route('/delete/<mssv>', methods=['POST'])
def delete(mssv):
    try:
        conn = get_db_connection(
            db_name=session['db_name'],
            user=session['user'],
            password=session['password'],
            host=session['host'],
            port=session['port']
        )
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dev_table WHERE mssv = %s", (str(mssv),))
        conn.commit()
        flash('Record deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting record: {e}', 'danger')
    return redirect(url_for('index'))

# Chức năng sửa
@app.route('/update/<mssv>', methods=['GET', 'POST'])
def update(mssv):
    form = UpdateForm()
    try:
        conn = get_db_connection(
            db_name=session['db_name'],
            user=session['user'],
            password=session['password'],
            host=session['host'],
            port=session['port']
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dev_table WHERE mssv = %s", (str(mssv),))
        record = cursor.fetchone()

        if request.method == 'GET' and record:
            form.mssv.data = record[0]
            form.hoten.data = record[1]
            form.diachi.data = record[2]
            form.email.data = record[3]
            form.sodienthoai.data = record[4]
            form.gioitinh.data = record[5]
            form.ngaysinh.data = record[6]
        elif form.validate_on_submit():
            cursor.execute(
                "UPDATE dev_table SET mssv = %s, hoten = %s, diachi = %s, email = %s, sodienthoai = %s, gioitinh = %s, ngaysinh = %s WHERE mssv = %s",
                (form.mssv.data, form.hoten.data, form.diachi.data, form.email.data, form.sodienthoai.data,form.gioitinh.data, form.ngaysinh.data, str(mssv))
            )
            conn.commit()
            flash('Record updated successfully!', 'success')
            return redirect(url_for('index'))
    except Exception as e:
        flash(f'Error updating record: {e}', 'danger')
    return render_template('update.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
