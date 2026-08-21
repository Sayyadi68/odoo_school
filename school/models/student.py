from odoo import models, fields


class student(models.Model):
    _name = 'school.student'
    _description = 'school.student'

    first_name= fields.Char(string="نام دانش اموز",required=True)
    last_name= fields.Char(string="نام خانوادگی",required=True)
    birth_date= fields.Date(string="تاریح تولد")
    phone= fields.Char(string="شماره تماس")
    email= fields.Char(string="ایمیل")
    student_code= fields.Char(string="کد دانش اموزی",required=True)
    average= fields.Float(string="معدل")
    is_active= fields.Boolean(string="فعال است؟",required=True)
    grade= fields.Selection(string="پایه تحصیلی",selection=[('1','اول'),('2','دوم'),('3','سوم'),('4','چهارم'),('5','پنجم'),('6','ششم')])
    address= fields.Text(string="آدرس")
    description= fields.Text(string="توضیحات تکمیلی")
    gender= fields.Selection(string="جنسیت",selection=[('male','مرد'),('female','زن')])

