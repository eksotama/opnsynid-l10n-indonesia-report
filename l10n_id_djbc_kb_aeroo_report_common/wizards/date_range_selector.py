# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class DateRangeSelector(models.AbstractModel):
    _inherit = "l10n_id.date_range_selector"

    output_format = fields.Selection(
        selection_add=[
            ('ods', 'ODS'),
            ('xls', 'XLS')
        ]
    )
