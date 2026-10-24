# Atributos de calidad

| ID | Atributo de calidad | Escenario de calidad |
|---|---|---|
| AC01 | **Rendimiento** | Las consultas de productos y confirmaciones de venta deben responder dentro del tiempo definido bajo una carga de prueba documentada. |
| AC02 | **Disponibilidad** | La plataforma debe permitir la operación durante el horario comercial y disponer de respaldo y recuperación ante fallos. |
| AC03 | **Escalabilidad** | La plataforma debe permitir incorporar negocios y sucursales y ampliar recursos según la carga medida. |
| AC04 | **Seguridad** | Cada usuario debe acceder únicamente a los datos de su negocio y a las operaciones y sucursales autorizadas. |
| AC05 | **Mantenibilidad** | Las reglas del negocio deben poder modificarse sin depender directamente de la interfaz, el framework o la base de datos. |
| AC06 | **Integridad y concurrencia** | Las ventas simultáneas y los reintentos no deben generar stock negativo, cobros duplicados ni registros parciales. |
| AC07 | **Trazabilidad** | Los cambios de inventario, cierres, anulaciones y entregas de efectivo deben conservar responsable, fecha y motivo. |

## Medición de los atributos

| ID | Atributo | Métrica y meta | Cómo se mide | Herramienta | Escenario |
|---|---|---|---|---|---|
| AC01 | Rendimiento | p95 ≤ 2 s y 0 errores 5xx. | Prueba de carga con 30 usuarios virtuales que buscan productos y confirman ventas. | k6 | [EQ-01](08-escenarios-atributos-calidad.md#eq-01-rendimiento-consulta-y-venta) |
| AC02 | Disponibilidad | 99% mensual; RPO ≤ 15 min; RTO ≤ 4 h. | Monitor externo que consulta `/health` cada minuto y calcula el porcentaje mensual; ensayo cronometrado de restauración a un punto en el tiempo. | UptimeRobot y PITR de Azure Database for PostgreSQL | [EQ-02](08-escenarios-atributos-calidad.md#eq-02-disponibilidad-recuperación-del-servicio) |
| AC03 | Escalabilidad | p95 ≤ 2 s y 0 errores 5xx al pasar de 10 a 30 usuarios virtuales. | Prueba de carga por etapas con el mismo dataset. | k6 | [EQ-03](08-escenarios-atributos-calidad.md#eq-03-escalabilidad-aumento-de-carga) |
| AC04 | Seguridad | 100% de accesos indebidos rechazados. | Solicitudes con sesión de otro negocio o sucursal e identificadores modificados. | Vitest y Supertest | [EQ-04](08-escenarios-atributos-calidad.md#eq-04-seguridad-aislamiento-entre-negocios) |
| AC05 | Mantenibilidad | Dominio sin imports de Express o Prisma; pruebas de regresión aprobadas. | Revisión de imports del dominio y ejecución de pruebas tras cambiar una regla. | Vitest | [EQ-05](08-escenarios-atributos-calidad.md#eq-05-mantenibilidad-cambio-de-reglas) |
| AC06 | Integridad y concurrencia | Una venta, un descuento y un cobro por operación; sin duplicados ni registros parciales. | Ventas simultáneas y reintento de la misma confirmación sobre PostgreSQL real. | Vitest, Supertest y PostgreSQL en Docker Compose | [EQ-06](08-escenarios-atributos-calidad.md#eq-06-integridad-ventas-entre-sucursales-y-reintento) |
| AC07 | Trazabilidad | 100% de operaciones de prueba reconstruidas. | Registrar merma, anulación y entrega de efectivo, y verificar responsable, fecha, motivo y referencia. | Vitest y Supertest | [EQ-07](08-escenarios-atributos-calidad.md#eq-07-trazabilidad-inventario-y-efectivo) |
