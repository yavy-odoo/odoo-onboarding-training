from odoo import models, fields


class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motorcycle Registry"

    registry_number = fields.Char("Registry Number", required=True)
    vin = fields.Char("VIN", required=True)
    first_name = fields.Char("First Name", required=True)
    last_name = fields.Char("Last Name", required=True)
    picture = fields.Image("Picture")
    current_mileage = fields.Float("Current Mileage")
    license_plate = fields.Char("License Plate")
    certificate_title = fields.Binary("Certification Title")
    register_date = fields.Date("Registration Date")
