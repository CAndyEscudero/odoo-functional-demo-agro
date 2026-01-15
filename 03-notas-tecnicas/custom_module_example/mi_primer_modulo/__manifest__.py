{
    "name": "Mi Primer Modulo",
    "version": "16.0.1.0.0",
    "category": "Tools",
    "summary": "Modulo de ejemplo para aprender Odoo",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/mi_modelo_views.xml",
        "views/menu.xml",
    ],
    "application": True,
    "installable": True,
}
