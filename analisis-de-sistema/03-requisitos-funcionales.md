# ⚙️ Requisitos Funcionales

## Objetivo
Traducir las historias de usuario en funciones concretas que el sistema
debe proporcionar, agrupadas por proceso de negocio.

---

## Requisitos funcionales

| ID | Proceso | Requisito funcional |
|---|---|---|
| **RF01** | Cuentas y Sucursales | El sistema deberá permitir al Superadministrador registrar nuevas cuentas de pastelería o cadena. |
| **RF02** | Cuentas y Sucursales | El sistema deberá permitir al Administrador de Cadena registrar una o más sucursales, cada una con su dirección, horario y datos de contacto. |
| **RF03** | Cuentas y Sucursales | El sistema deberá garantizar el aislamiento lógico de los datos entre cuentas de pastelería distintas (multi-tenant). |
| **RF04** | Catálogo e Inventario | El sistema deberá permitir registrar el catálogo de productos con precio, categoría y foto. |
| **RF05** | Catálogo e Inventario | El sistema deberá permitir registrar y actualizar el stock de cada producto por sucursal. |
| **RF06** | Catálogo e Inventario | El sistema deberá alertar cuando el stock se encuentre por debajo de un mínimo configurado. |
| **RF07** | Traslados | El sistema deberá permitir registrar un traslado de mercadería entre sucursales. |
| **RF08** | Traslados | El sistema deberá actualizar automáticamente el inventario de origen y destino al confirmarse un traslado. |
| **RF09** | Empleados, Turnos y Caja | El sistema deberá permitir registrar empleados y asignarlos a un turno. |
| **RF10** | Empleados, Turnos y Caja | El sistema deberá permitir el cierre de caja por turno, desglosado por método de pago. |
| **RF11** | Ventas y Pedidos | El sistema deberá permitir registrar una venta directa en mostrador, descontando el stock correspondiente. |
| **RF12** | Ventas y Pedidos | El sistema deberá permitir registrar pedidos anticipados con fecha de entrega y estado. |
| **RF13** | Ventas y Pedidos | El sistema deberá garantizar que un mismo producto no se comprometa en dos pedidos simultáneos (control de concurrencia). |
| **RF14** | Sitio Web | El sistema deberá permitir activar un sitio web público de catálogo y pedidos por sub-ruta propia. |
| **RF15** | Sitio Web | El sistema deberá sincronizar en tiempo real el stock entre el panel interno y el sitio web. |
| **RF16** | Reportes | El sistema deberá emitir reportes de ventas, traslados e inventario, exportables en Excel o PDF. |

## Relación entre Historias de Usuario y Requisitos Funcionales

| Historia de usuario | Requisitos funcionales relacionados |
|---|---|
| HU01 Registrar cuentas | RF01, RF03 |
| HU02 Registrar sucursales | RF02 |
| HU03 Registrar catálogo | RF04, RF05 |
| HU04 Alertas de stock | RF06 |
| HU05 Registrar traslados | RF07, RF08 |
| HU06 Asignar turnos | RF09 |
| HU07 Venta en mostrador | RF11, RF13 |
| HU08 Cierre de caja | RF10 |
| HU09 Pedido desde sitio web | RF12, RF14, RF15 |
| HU10 Reportes consolidados | RF16 |