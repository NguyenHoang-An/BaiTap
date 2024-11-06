from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import DataRequired 

class LoginForm(FlaskForm):
    db_name = StringField('Database Name', validators=[DataRequired()], default='dev_database') 
    user = StringField('User', validators=[DataRequired()], default= 'postgres')
    password = PasswordField('Password', validators=[DataRequired()], default='0963631472') 
    host = StringField('Host', validators=[DataRequired()], default='localhost')
    port = StringField('Port', validators=[DataRequired()], default='5432')
    submit = SubmitField('Login') 

class InsertForm(FlaskForm):
    mssv = StringField('MSSV', validators=[DataRequired()]) 
    hoten = StringField('Họ tên', validators=[DataRequired()]) 
    diachi = StringField('Địa chi', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    sodienthoai = StringField('Số điện thoại', validators=[DataRequired()])
    submit = SubmitField('Insert Data')
    
class UpdateForm(FlaskForm):
    mssv = StringField('MSSV', validators=[DataRequired()]) 
    hoten = StringField('Họ tên', validators=[DataRequired()])  
    diachi = StringField('Địa chi', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    sodienthoai = StringField('Số điện thoại', validators=[DataRequired()])
    submit = SubmitField('Update Data')
     