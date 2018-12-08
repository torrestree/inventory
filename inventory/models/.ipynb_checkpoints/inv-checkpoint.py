from odoo import api, fields, models

class Inv(models.Model):
    _name='inventory.inv'
    _description='仓库信息'
    
    name=fields.Char(string='仓库编号')
    start_date=fields.Date(string='启用日期')
    state=fields.Selection([('inuse','正常使用'),('rebuild','正在翻修'),('obsolete','已废弃')],string='状态',readonly=True,default='inuse')