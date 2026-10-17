# Tecnologías del proyecto

La implementación se ubicará en `pasteleria-saas`. Este Sprint documenta el diseño; todavía no existe una aplicación completa ejecutable.

| Elemento | Tecnología seleccionada | Responsabilidad y motivo |
|---|---|---|
| Frontend | **Next.js + TypeScript + Tailwind CSS** | Pantallas internas, formularios, catálogo visual y punto de venta. Next.js organiza rutas y componentes; Tailwind define estilos. |
| Backend | **Node.js + Express + TypeScript** | API REST y siete módulos del negocio. Express atiende HTTP; los casos de uso contienen la coordinación. |
| Datos | **PostgreSQL** | Relaciones, restricciones, transacciones y aislamiento por filas (RLS). |
| Persistencia | **Prisma + SQL parametrizado** | Tipos y migraciones; SQL explícito para bloqueos, políticas RLS e índices parciales. |
| Autenticación | **Sesiones opacas + Argon2id** | Sesiones revocables guardadas en PostgreSQL; hash de contraseñas; cookie HttpOnly, Secure y SameSite. |
| Validación | **Zod** | Esquemas de entrada HTTP; las reglas del dominio siguen validándose en el servidor. |
| API | **OpenAPI** | Documentar rutas, contratos, errores y autenticación. |
| Excel | **ExcelJS** | Generar archivos XLSX con los filtros y permisos del reporte. |
| Desarrollo | **Node.js, npm, VS Code y Docker Compose** | Entorno de trabajo y PostgreSQL local reproducible. |
| Pruebas | **Vitest, Supertest, Playwright y k6** | Reglas/contratos, API con PostgreSQL real, navegador y carga. |
| Versionado | **Git y GitHub** | Documentación, código e historial de cambios. |

Se fijarán versiones compatibles y con soporte en `package.json`, archivo de bloqueo e imagen Docker al iniciar la implementación; no se inventan versiones ya instaladas ni resultados de pruebas de un producto inexistente.

## Despliegue inicial

| Servicio | Uso | Condición operativa |
|---|---|---|
| **Render Web Service** | Una instancia Node.js ejecuta Express y sirve la exportación estática de Next.js. | HTTPS, secretos en entorno, comprobación de salud y logs estructurados. |
| **Render Postgres** | Datos de negocio y sesiones. | Plan con recuperación a un punto en el tiempo (PITR), red protegida, rol de aplicación limitado y migraciones separadas. |
| **Cloudflare R2** | Fotografías privadas de productos. | Claves y metadatos por negocio; acceso autorizado desde la API. |

Next.js utilizará `output: "export"`. Las pantallas se generan sin datos privados; en el navegador consultan `/api/v1`. Se emplean rutas estáticas y parámetros para seleccionar registros. No se requieren Server Actions, SSR ni un servidor Next.js adicional. Las fotografías se sirven mediante la API autorizada y un elemento de imagen estándar, sin depender del optimizador de imágenes de un servidor Next.js.

No se añaden Redis/Upstash, PgBouncer ni réplica de lectura inicialmente. Se limita el pool, se optimizan consultas y se mide. La instancia inicial no constituye alta disponibilidad. Las metas de recuperación se verifican con un ensayo; seleccionar un proveedor no demuestra su cumplimiento.

## Seguridad y operación

- Autorización por negocio, sucursal y permiso en cada caso de uso. El superadministrador administra cuentas; no obtiene acceso operativo global por defecto.
- RLS y claves compuestas complementan la autorización. El rol de aplicación no es propietario ni tiene BYPASSRLS; el tenant se establece localmente dentro de la transacción.
- Inicio de sesión con limitación de intentos, respuestas sin revelar cuentas existentes, rotación de sesión y protección CSRF. Credencial temporal de un uso para recuperación autorizada; no se exige un proveedor de correo.
- Fotografías con límite de 5 MB, validación de contenido JPEG/PNG/WebP, eliminación de metadatos y nombre generado en servidor. El fallo de imagen muestra un reemplazo y no impide una venta válida.
- Logs con identificador de solicitud, sin contraseñas, cookies o secretos. Auditoría de cambios junto a la operación. Reportes de hasta 31 días; detalle paginado y exportaciones limitadas a 10 000 filas para evitar agotamiento de memoria.
- Respaldo, restauración, migraciones y monitoreo antes del piloto. Los datos reales no se utilizan en pruebas de carga.

## Primera demostración funcional

Dos negocios aislados; administrador crea empleado y turno; empleado abre caja, vende productos y cierra. Se prueban ventas simultáneas en distintas sucursales o negocios, con un responsable por sucursal; cada reintento conserva una sola venta y sus movimientos.