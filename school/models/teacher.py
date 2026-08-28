from odoo import models, fields


class teacher(models.Model):
    _name = 'school.teacher'
    _description = 'school.teacher'

    first_name= fields.Char(string="نام استاد",required=True)
    last_name= fields.Char(string="نام خانوادگی",required=True)
    birth_date= fields.Date(string="تاریح تولد")
    phone= fields.Char(string="شماره تماس")
    email= fields.Char(string="ایمیل")
    student_code= fields.Char(string="کد استادی ",required=True)
    is_active= fields.Boolean(string="فعال است؟",required=True)
    grade= fields.Selection(string="پایه تحصیلی",selection=[('1','اول'),('2','دوم'),('3','سوم'),('4','چهارم'),('5','پنجم'),('6','ششم')])
    lesson = fields.Many2many(
        'school.lesson',
        string="درس‌ها"
    ) 
    address= fields.Text(string="آدرس")
    description= fields.Text(string="توضیحات تکمیلی")
    gender= fields.Selection(string="جنسیت",selection=[('male','مرد'),('female','زن')])

    def name_get(self):
        result = []

        for record in self:
            name = f"{record.first_name or ''} {record.last_name or ''}".strip()
            result.append((record.id, name or "استاد بدون نام"))

        return result