# Decisiones arquitectónicas

| ID | Decisión arquitectónica | Driver relacionado | Justificación | Resultado |
|---|---|---|---|---|
| ADR-001 | Monolito modular | DA01 – Escalabilidad; DA06 – Mantenibilidad | Separar responsabilidades dentro de un backend desplegable como unidad. | Módulos de Plataforma, Acceso, Catálogo, Inventario, Ventas, Caja y Reportes. |
| ADR-002 | Clean Architecture | DA06 – Mantenibilidad | Aislar reglas y casos de uso de los detalles tecnológicos. | Dominio, Aplicación, Infraestructura y Presentación dentro de los módulos. |
| ADR-003 | PostgreSQL compartido con aislamiento por negocio | DA03 – Seguridad | Combinar tenant_id, autorización, claves compuestas y políticas de filas. | Datos separados lógicamente y permisos por sucursal. |
| ADR-004 | Transacciones e idempotencia | DA04 – Integridad | Confirmar venta, cobro y stock conjuntamente y evitar duplicados por reintentos. | Unidad de trabajo y control concurrente en PostgreSQL. |
| ADR-005 | Next.js, Tailwind CSS y API REST Node.js + Express con TypeScript | DA06 – Mantenibilidad | Next.js organiza las pantallas; Express expone HTTP sin imponer estructura al dominio. TypeScript permite contratos compartidos; Tailwind define la presentación visual. | Aplicación web y API REST; Prisma en los adaptadores de persistencia. |
| ADR-006 | Consultas directas optimizadas inicialmente | DA02 – Rendimiento | Evaluar índices y carga antes de introducir sincronización de caché. | PostgreSQL como fuente de stock; Redis, réplica y PgBouncer sujetos a medición. |
| ADR-007 | Movimientos trazables y restauración probada | DA05 – Recuperación y trazabilidad | Explicar cambios y recuperar información ante fallos. | Historial de operaciones, copias, monitoreo y pruebas de restauración. |

## Servicios seleccionados para el diseño

| ID | Decisión arquitectónica | Driver relacionado | Justificación | Resultado |
|---|---|---|---|---|
| ADR-008 | Cloudflare R2 para imágenes | DA01, DA02; RF04 | Almacenar fotos fuera de la instancia de aplicación mediante un adaptador. | Un sistema externo con credenciales en servidor y metadatos por negocio en PostgreSQL. |
| ADR-009 | Render para aplicación y PostgreSQL administrado | DA05 | Reducir la administración inicial del alojamiento y definir respaldo y recuperación. | Selección de diseño; plan, región y presupuesto pendientes, sin contratación ni despliegue realizados. |