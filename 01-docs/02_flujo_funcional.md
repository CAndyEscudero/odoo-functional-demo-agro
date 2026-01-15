# Flujo Funcional – Odoo ERP

Este documento describe el flujo operativo implementado en Odoo
para compras, inventario y ventas.

---

## Compras

- Creación de Orden de Compra
- Confirmación de la orden
- Validación de la recepción

**Resultado:**  
El stock se incrementa al validar la recepción.

---

## Inventario

- Productos configurados como almacenables
- Control de stock en tiempo real

**Resultado:**  
El inventario refleja las entradas y salidas operativas.

---

## Ventas

- Creación de Orden de Venta
- Confirmación de la venta
- Generación automática de la entrega

**Resultado:**  
El stock se descuenta al validar la entrega.

---

## Facturación

- Generación de factura desde la orden de venta
- Estado Draft (Odoo Community)
