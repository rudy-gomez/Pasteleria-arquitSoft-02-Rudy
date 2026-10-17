# Requisitos funcionales

## Requisitos funcionales

| ID | Requisito funcional |
|---|---|
| RF01 | El sistema debe permitir registrar negocios, asignar a su administrador y gestionar su estado y límites de servicio. |
| RF02 | El sistema debe permitir registrar sucursales y ubicaciones de abastecimiento dentro de cada negocio. |
| RF03 | El sistema debe permitir registrar personal, asignarle sucursales y permisos, y programar sus turnos de trabajo con fecha y hora de inicio y fin. |
| RF04 | El sistema debe permitir registrar productos y presentaciones con categoría, precio, fotografía y código de barras opcional. |
| RF05 | El sistema debe permitir consultar existencias por ubicación e identificar productos por debajo del mínimo configurado. |
| RF06 | El sistema debe permitir registrar ingresos, mermas y ajustes de inventario con cantidad, responsable y motivo. |
| RF07 | El sistema debe permitir registrar el envío y la recepción de productos entre ubicaciones del mismo negocio, identificar diferencias de cantidad y permitir su resolución autorizada con motivo e historial. |
| RF08 | El sistema debe permitir abrir una sesión de caja vinculada al empleado, la sucursal y su turno, con fondo inicial y hora de apertura, evitando dos sesiones abiertas en la misma caja. |
| RF09 | El sistema debe permitir mostrar productos con imagen, precio y disponibilidad, buscarlos por nombre, categoría o código de barras y agregarlos a un carrito de venta. |
| RF10 | El sistema debe permitir confirmar una venta, registrar el cobro y descontar las existencias de la sucursal en una operación atómica. |
| RF11 | El sistema debe permitir cerrar la sesión de caja al finalizar la atención o cambiar de responsable, registrando hora de cierre, efectivo contado y diferencia respecto de los movimientos y cobros de la sesión. |
| RF12 | El sistema debe permitir registrar retiros y entregas de efectivo con importe, responsable y receptor, sin duplicar ingresos por ventas. |
| RF13 | El sistema debe permitir consultar reportes de ventas, cobros, existencias, mermas y traslados por periodo y sucursal, y exportarlos en Excel. |
| RF14 | El sistema debe permitir descontar una torta entera e ingresar sus porciones mediante un fraccionamiento registrado. |
| RF15 | El sistema debe permitir anular una venta completa con autorización y motivo, registrando la devolución del cobro y el destino de los productos. |
| RF16 | El sistema debe permitir iniciar y cerrar sesión, cambiar la contraseña y restablecer el acceso mediante una credencial temporal de un solo uso emitida por un administrador autorizado, revocando las sesiones anteriores. |
| RF17 | El sistema debe permitir al administrador consultar el historial de operaciones de su negocio por fecha, usuario, sucursal y tipo de movimiento. |
| RF18 | El sistema debe permitir identificar lotes de productos perecibles, registrar su vencimiento, consultar los próximos a vencer y bloquear la venta de unidades vencidas. |

## Relación entre historias de usuario y requisitos funcionales

| Historia de usuario | Requisitos funcionales relacionados |
|---|---|
| HU01 Registrar negocios | RF01 |
| HU02 Gestionar sucursales, personal y turnos | RF02, RF03 |
| HU03 Gestionar catálogo | RF04, RF05 |
| HU04 Controlar inventario | RF05, RF06 |
| HU05 Gestionar traslados | RF07 |
| HU06 Operar caja y ventas | RF08, RF09, RF10, RF11 |
| HU07 Registrar entregas de efectivo | RF12 |
| HU08 Consultar reportes | RF13 |
| HU09 Fraccionar tortas | RF14 |
| HU10 Anular ventas | RF15 |
| HU11 Acceder de forma segura | RF16 |
| HU12 Revisar historial | RF17 |
| HU13 Controlar vencimientos | RF18 |