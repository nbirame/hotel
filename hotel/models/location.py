from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Location(models.Model):
    _name = "hotel.location"
    _description = "Location"

    dateloc = fields.Date(string="Date debut location")
    nombre = fields.Integer(string='Nombre de jours')
    datefinloc = fields.Date(string="Date fin location")
    prix = fields.Integer(string="Montant location")
    chambre_id = fields.Many2one("hotel.chambre",string="Chambre")
    total = fields.Integer(string="Prix total", compute="_compute_total")
    _sql_constraints = [
        ('dateloc_chambre_id_unique', 'unique (dateloc, chambre_id)', "Cette chambre est déja occuper")
    ]

    @api.depends("prix", "nombre")
    def _compute_total(self):
        for record in self:
            record.total = record.prix * record.nombre

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s-%s" % (record.dateloc, record.total)
            result.append((record.id, rec_name))
        return result

    @api.onchange('dateloc', 'datefinloc', 'nombre')
    def _onchange_datefinloc(self):
        for record in self:
            nb = record.nombre
            record.datefinloc = record.dateloc + relativedelta(days=nb)

    @api.constrains("chambre_id", "dateloc", "datefinloc", "numero")
    def _check_chambre_id(self):
        chambre_louer = self.env['hotel.location'].sudo().search([('chambre_id', '=', self.chambre_id.id)])
        for record in self:
            for chambre_loc in chambre_louer[1::]:
                print(chambre_loc.dateloc)
                if record.chambre_id.numero == chambre_loc.chambre_id.numero:
                    if (chambre_loc.dateloc <= record.dateloc < chambre_loc.datefinloc) or (chambre_loc.dateloc <= record.datefinloc < chambre_loc.datefinloc) or (record.dateloc <= chambre_loc.dateloc < record.datefinloc):
                        raise ValidationError(_("La chambre est occuper pendant cette période"))



