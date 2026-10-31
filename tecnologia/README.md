# Tecnologías de Sweetly

El código se mantiene en un proyecto aparte (`Sweetly`), fuera de este repositorio de documentación. Frontend y backend son proyectos separados que se comunican solo por la API REST documentada con OpenAPI.

| Elemento | Tecnología seleccionada | Responsabilidad y motivo |
|---|---|---|
| Frontend | **Next.js + TypeScript + Tailwind CSS** | Vista de escritorio y aplicación móvil instalable (PWA). Next.js organiza rutas y componentes; Tailwind define estilos. |
| Animación | **Motion** | Hojas inferiores, paneles, indicadores y cifras. |
| Gráficos | **Recharts** | Tendencia de stock, salud del inventario y pagos por mes, con datos reales de la API. |
| 3D | **Three.js + React Three Fiber** | Torta de la pantalla de ingreso; se descarga después del formulario. |
| Escaneo | **BarcodeDetector + ZXing** | Lectura de códigos de barras con la cámara del celular; lector USB en caja como teclado. |
| Backend | **Node.js + Express + TypeScript** | API REST por módulos. Express atiende HTTP; los casos de uso contienen la coordinación. |
| Datos | **PostgreSQL** | Relaciones, restricciones, transacciones y aislamiento por negocio. |
| Persistencia | **Prisma + SQL parametrizado** | Tipos y migraciones; SQL explícito para bloqueos e índices parciales. |
| Autenticación | **Sesiones opacas + Argon2id** | Sesiones revocables guardadas en PostgreSQL; cookie HttpOnly, Secure y SameSite. |
| Validación | **Zod** | Esquemas de entrada HTTP; las reglas del dominio se validan en el servidor. |
| API | **OpenAPI + Swagger UI** | Contrato de cada módulo, visible en `/api/docs`. |
| Excel | **ExcelJS** | Reportes XLSX (sprint de Reportes). |
| Desarrollo | **Node.js, npm, VS Code y Docker Compose** | Entorno de trabajo y PostgreSQL local reproducible. |
| Pruebas | **Vitest, Supertest, Playwright y k6** | Reglas, API con PostgreSQL real, navegador y carga. |
| Versionado | **Git y GitHub** | Documentación, especificaciones, código e historial. |

## Estructura del código

Ambos proyectos se organizan **por módulo** (lo que hace el negocio) y, dentro de cada módulo del backend, **por capas de Clean Architecture**.

```text
sweetly/
├── docker-compose.yml               PostgreSQL local
├── backend/
│   ├── prisma/schema.prisma         Modelo de datos
│   ├── openapi/                     Contrato publicado en /api/docs
│   ├── src/
│   │   ├── modules/
│   │   │   ├── plataforma/          Negocios, sucursales y ubicaciones
│   │   │   ├── acceso/              Sesiones, personal, permisos y turnos
│   │   │   ├── catalogo/            Categorías y productos
│   │   │   └── inventario/          Existencias, lotes y movimientos
│   │   │       ├── dominio/         Reglas puras (sin Express ni Prisma)
│   │   │       ├── aplicacion/      Casos de uso y puertos
│   │   │       ├── infraestructura/ Adaptadores Prisma
│   │   │       └── presentacion/    Rutas, controladores y esquemas Zod
│   │   ├── shared/                  Errores, middleware y sesión
│   │   ├── composition.ts           Une casos de uso con adaptadores
│   │   ├── app.ts                   Configuración de Express
│   │   └── server.ts                Punto de arranque
│   ├── tests/                       Pruebas de dominio y de API
│   └── Dockerfile
└── frontend/
    ├── public/                      Manifiesto PWA, íconos y service worker
    └── src/
        ├── app/                     Rutas (páginas)
        ├── modules/                 Pantallas y llamadas por módulo
        └── shared/                  Diseño, componentes y cliente HTTP
```

## Diseño de la interfaz

| Aspecto | Decisión |
|---|---|
| Identidad | Nace del logo: chocolate profundo para la estructura (barra lateral, bandas de resumen), cereza como único acento de acción y crema del merengue sobre fondos oscuros. Superficies de datos blancas sobre un fondo neutro "harina". |
| Recurso propio | Borde de chocolate derretido que cierra las bandas oscuras (resumen de Inicio, panel del servicio, hoja de ingreso en el celular). |
| Tipografía | *Bricolage Grotesque* en títulos y cifras grandes; *Geist* en lectura y datos; cifras tabulares en tablas. |
| Estados | Pistacho (correcto o entra), caramelo (aviso), cereza (alerta o sale), arándano (ajustes). Los mismos colores en insignias, gráficos e historial. |
| Ingreso | Escena de chocolate con una torta 3D que gira despacio y se inclina con el cursor. Sin WebGL o mientras carga, una ilustración equivalente; con "reducir movimiento", la torta queda quieta. |
| Escritorio | Barra lateral, tablas numeradas con encabezado fijo, columnas ordenables, filtros combinables, selección múltiple y cajón lateral para editar. |
| Celular (PWA) | Barra de navegación flotante con "Registrar stock" al centro, listas en lugar de tablas, hojas que suben desde abajo y se cierran deslizando. Sin zoom con los dedos; el texto respeta el tamaño configurado en el teléfono. |
| Productos | Búsqueda por nombre, categoría o código de barras; los envasados se escanean con la cámara o el lector USB. |
| Animación | Corta (160–340 ms) y con propósito: hojas, paneles, indicadores que se deslizan y cifras que cuentan al aparecer. Se desactiva si el sistema pide reducir movimiento. |
| Accesibilidad | Contraste AA, áreas táctiles de 44 px, foco visible, etiquetas en todos los campos y estados vacíos que explican qué hacer. |

## Navegación por rol

| Rol | Secciones |
|---|---|
| Superadministrador | Panel (salud del servicio) · Negocios (plan, vigencia, uso y pagos) · Pagos · Planes |
| Administrador | Inicio · Inventario (existencias, vencimientos e historial) · Catálogo · Equipo (personas y turnos) · Sucursales |
| Empleado | Inicio (con su turno del día) · Inventario · Catálogo, según sus permisos |

"Registrar stock" (ingreso, merma o ajuste) está disponible desde cualquier pantalla para quien tenga permiso. El historial de movimientos vive dentro de Inventario, con filtros por tipo, fechas, responsable y producto.

## Despliegue

| Servicio | Uso | Condición operativa |
|---|---|---|
| **Azure Static Web Apps** | Publica la exportación estática de Next.js en `app.sweetly.pe`. | CDN y certificado administrados. |
| **Azure Container Apps** | Ejecuta la imagen Docker de la API en `api.sweetly.pe`. | Sin estado; escala por réplicas; secretos en la configuración; comprobación de salud en `/health`. |
| **Azure Database for PostgreSQL (servidor flexible)** | Datos de negocio y sesiones. | Copias automáticas con recuperación a un punto en el tiempo (PITR, retención de 7 a 35 días), red protegida y rol de aplicación limitado. |
| **Cloudflare R2** | Fotografías de productos. | Claves por negocio; acceso autorizado desde la API. En desarrollo se usa una carpeta local. |
| **UptimeRobot** | Monitoreo externo. | Consulta `/health` cada minuto y calcula el porcentaje mensual de disponibilidad (AC02). |
| **GitHub Actions** | Integración continua. | Compila y ejecuta las pruebas en cada cambio. |

Interfaz y API comparten el dominio `sweetly.pe`: la cookie de sesión es del mismo sitio y CORS solo admite `app.sweetly.pe`. No se añaden Redis, PgBouncer ni réplica de lectura inicialmente; se mide antes.

## Ejecución local

```bash
cd Sweetly
docker compose up -d
```

```bash
cd Sweetly/backend
npm install
npm run db:setup
npm run dev
```

```bash
cd Sweetly/frontend
npm install
npm run dev
```

| Dirección | Contenido |
|---|---|
| `http://localhost:3000` | Interfaz web (en el celular, abrir con la IP de la PC en la misma red) |
| `http://localhost:4000/api/docs` | Documentación Swagger de la API |
| `http://localhost:4000/health` | Estado del servicio |

`npm run db:setup` aplica las migraciones y crea datos de demostración: dos negocios, dos sucursales, un taller, 16 productos con lotes y turnos. Las credenciales de prueba están al inicio de `backend/prisma/seed.ts`.

Para abrirlo en el celular: conecta el teléfono a la misma red Wi-Fi, abre `http://<IP-de-la-PC>:3000` y elige **Agregar a la pantalla de inicio** para instalarlo como app.

## Pruebas

```bash
cd Sweetly/backend
npm test
```

| Tipo | Cantidad | Qué verifican |
|---|---|---|
| Unitarias del dominio | 49 | Reglas de cada módulo sin base de datos ni Express (AC05), incluidas las de suscripción y pagos. |
| API con PostgreSQL real | 48 | Criterios de aceptación de cada módulo, aislamiento entre negocios (AC04), dos mermas simultáneas sobre el último stock (AC06), pagos y tendencia diaria. |

Cada prueba cita el criterio (CA-…) o atributo (AC…) que comprueba.

## Seguridad y operación

- Autorización por negocio, sucursal y permiso en cada caso de uso. El superadministrador administra cuentas; no obtiene acceso operativo a los negocios.
- Toda consulta filtra por el negocio de la sesión; los identificadores de otro negocio responden 404.
- Inicio de sesión con limitación de intentos, mensaje que no revela si la cuenta existe y revocación de sesiones al cambiar o restablecer la contraseña.
- Fotografías con límite de 5 MB y validación de contenido JPEG/PNG/WebP; nombre generado en el servidor.
- Logs con identificador de solicitud, sin contraseñas, cookies ni secretos.
