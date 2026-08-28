from odoo import models, fields


class lesson(models.Model):
    _name = 'school.lesson'
    _description = 'school.lesson'

    lesson_name=fields.Text(string="نام درس")
    lesson_unit=fields.Integer(string="واحد")
    lesson_teacher = fields.Many2many(
        "school.teacher",
        string="استاد"
    )

    lesson_student = fields.Many2many(
        "school.student",
        string="دانشجو"
    )
    
    def name_get(self):
        result = []

        for record in self:
            name = f"{record.lesson_name or ''}".strip()
            result.append((record.id, name or "درس بدون نام"))

        return result