# -*- coding: utf-8 -*-
# Copyright 2016 - Ursa Information Systems <http://ursainfosystems.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)


from odoo import api, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def fetch_export_models(self):
        return []
        
