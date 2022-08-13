from odoo import models, fields, api
class Chambre(models.Model):
	_name="hotel.chambre"
	_description="Chambre"

	numero = fields.Char(string='Numéro Chambre', readonly=True)
	infor=fields.Html(string="Description Chambre")
	profile = fields.Binary(string="Image")

	def name_get(self):
		result = []
		for record in self:
			rec_name = "%s" % (record.numero)
			result.append((record.id, rec_name))
		return result

	@api.model
	def create(self, vals):
		vals["numero"] = (
			self.env["ir.sequence"].next_by_code("hotel.chambre") or "/"
			)
		res = super(Chambre, self).create(vals)
		return res

