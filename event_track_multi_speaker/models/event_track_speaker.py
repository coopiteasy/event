# Copyright 2017 David Vidal<david.vidal@tecnativa.com>
# Copyright 2017 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class EventTrackSpeaker(models.Model):
    _name = "event.track.speaker"
    _description = "Track Speaker"

    name = fields.Char(related="partner_id.name")
    partner_id = fields.Many2one("res.partner", string="Contact")
    status = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("waiting", "Waiting"),
            ("validated", "Validated"),
        ]
    )
