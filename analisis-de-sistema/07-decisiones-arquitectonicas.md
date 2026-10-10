# 📋 Decisiones Arquitectónicas (ADR)

## Objetivo
Documentar las decisiones arquitectónicas importantes tomadas para responder
a los drivers identificados, junto con su justificación.

**ADR (Architecture Decision Record)** = Registro de Decisión Arquitectónica.

---

| ID | Decisión arquitectónica | Driver relacionado | Justificación | Resultado |
|---|---|---|---|---|
| **ADR-001** | Monolito modular con escalamiento horizontal | DA03 – Escalabilidad, DA07 – Mantenibilidad | Organizar las funcionalidades en módulos independientes dentro de una misma aplicación desplegable, permitiendo agregar instancias detrás de un balanceador de carga a medida que se incorporan nuevas pastelerías. | Módulos de Cuentas y Sucursales, Catálogo e Inventario, Traslados, Empleados/Turnos/Caja, Ventas y Pedidos, y Reportes. |
| **ADR-002** | Clean Architecture | DA07 – Mantenibilidad | Separar las reglas del negocio (control de stock, cierre de caja, traslados) de los detalles tecnológicos (BD, framework, impresora), evitando que cambios externos afecten el núcleo del sistema. | Capas de Dominio, Aplicación, Infraestructura y Presentación. |
| **ADR-003** | Estrategia de caché (Redis) | DA02 – Rendimiento | Reducir consultas repetitivas a la base de datos en la verificación de stock y catálogo, que se consultan desde el mostrador y el sitio web al mismo tiempo. | Consultas de stock en menos de 2 segundos bajo carga pico. |
| **ADR-004** | Bloqueo transaccional con reserva temporal (TTL) | DA01 – Concurrencia | Garantizar que un mismo producto no se comprometa en dos ventas o pedidos simultáneos (mostrador y web), usando `SELECT ... FOR UPDATE` y liberación automática de reservas abandonadas. | Consistencia del stock entre ambos canales de venta. |
| **ADR-005** | Aislamiento multi-tenant por `tenant_id` | DA04 – Seguridad multi-tenant | Mantener los datos de cada pastelería o cadena lógicamente aislados dentro de la misma base de datos, sin duplicar infraestructura por cliente. | Separación de datos entre cuentas, sin visibilidad cruzada. |
| **ADR-006** | Pool de conexiones (PgBouncer) | DA05 – Pool de conexiones | Evitar el agotamiento de conexiones a PostgreSQL bajo picos de escritura simultánea, administrando las conexiones entre la aplicación y la base de datos. | Base de datos estable bajo carga de ventas concurrentes. |
| **ADR-007** | Réplica de lectura para reportes | DA06 – Separación de reportes | Aislar las consultas pesadas de reportes de la carga transaccional (ventas, caja), para que no afecten la operación diaria. | Reportes consolidados sin impactar las transacciones. |