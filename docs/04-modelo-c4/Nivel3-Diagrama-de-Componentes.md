# Nivel 3 · Diagrama de componentes

> **Proyecto:** Plataforma SaaS de pastelerías  
> **Estado:** Diseño propuesto; pendiente de implementación.

## 1. Objetivo

Mostrar los módulos de la API y su colaboración dentro del monolito.

| Aspecto | Descripción |
|---|---|
| Pregunta que responde | ¿Cómo se divide el backend y qué hace cada parte? |
| Audiencia | Arquitectos y desarrolladores |
| Qué es un componente | Conjunto de funcionalidades con responsabilidad y contrato definidos. |
| Nivel anterior | [Nivel 2](Nivel2-DiagramadeContenedores.md) |
| Siguiente nivel | [Nivel 4](Nivel4-DiagramadeCodigo.md) |

## 2. Diagrama

![nivel3 componentes](../../img/nivel3-componentes.png)

Las flechas muestran colaboración en ejecución. Los adaptadores implementan puertos del núcleo; el diagrama no representa la dirección de imports del código.

## 3. Componentes

| Componente | Responsabilidad | Funcionalidades principales | Carpeta en el código |
|---|---|---|---|
| **API REST** | Entrada HTTP | Validación, autorización y respuesta de errores. | presentacion/ de cada módulo |
| **Plataforma** | Negocios y estructura | Alta, límites, sucursales y estado de cuenta. | modules/plataforma/ |
| **Acceso** | Identidad y permisos | Membresías, permisos, sesiones de acceso, asignaciones y turnos de trabajo. | modules/acceso/ |
| **Catálogo** | Información comercial | Productos, presentaciones, imágenes y precios. | modules/catalogo/ |
| **Inventario** | Existencias | Lotes, vencimientos, ingresos, mermas, traslados y fraccionamiento. | modules/inventario/ |
| **Ventas** | Operación comercial | Confirmación, cobro y anulación. | modules/ventas/ |
| **Caja** | Responsabilidad sobre efectivo | Sesiones de caja vinculadas al empleado y turno, cierre, retiros y custodia. | modules/caja/ |
| **Reportes** | Consulta de resultados | Ventas, cobros, inventario, historial y exportación Excel. | modules/reportes/ |

Las rutas son propuestas para la implementación, no archivos existentes.

## 4. Relaciones entre componentes

| Origen | Destino | Descripción | Tipo de comunicación |
|---|---|---|---|
| Aplicación web | API REST | Solicita operaciones. | HTTPS/JSON |
| API REST | Acceso | Valida sesión, negocio y sucursal. | Llamada interna |
| API REST | Casos de uso | Ejecuta operaciones autorizadas. | Llamada interna |
| Ventas | Catálogo | Obtiene productos y precios válidos. | Contrato público |
| Ventas | Inventario | Descuenta stock dentro de la transacción. | Contrato público |
| Ventas | Caja | Comprueba sesión y registra efectivo. | Contrato público |

## 5. Relaciones con contenedores y sistemas externos

| Componente | Destino | Descripción | Protocolo | Patrón aplicado |
|---|---|---|---|---|
| Módulos operativos | PostgreSQL | Persistencia mediante adaptadores por módulo. | SQL sobre conexión PostgreSQL | Repository |
| Ventas, Inventario y Caja | PostgreSQL | Confirmación conjunta de una venta. | Transacción compartida | Unit of Work |
| Catálogo | Almacenamiento de imágenes | Guarda y consulta fotografías. | HTTPS | Adapter |
| Reportes | PostgreSQL | Lee proyecciones autorizadas de varios módulos. | SQL | Consulta de lectura |

## 6. Reglas del monolito modular

| # | Regla | Motivo |
|---|---|---|
| 1 | Los módulos del backend se despliegan juntos. | Mantener una única unidad de operación inicial. |
| 2 | Un módulo usa contratos públicos de otro, sin escribir directamente sus tablas. | Conservar responsabilidades y evitar acoplamiento. |
| 3 | Los participantes de una venta comparten una transacción y conexión. | Evitar commits parciales. |
| 4 | Reportes puede leer proyecciones documentadas entre módulos, sin modificar datos. | Producir resultados consolidados sin romper propiedad de escritura. |
| 5 | Dominio no importa Express ni Prisma. | Mantener las reglas independientes. |
| 6 | Toda operación valida negocio y sucursal; los límites del plan se comprueban también ante concurrencia. | Evitar accesos cruzados y altas simultáneas fuera del límite. |

## Trazabilidad de los componentes

| Componente | Requisitos de origen |
|---|---|
| Plataforma | RF01, RF02 |
| Acceso y turnos | RF03, RF16; AC04 |
| Catálogo y adaptador R2 | RF04, RF05; R2 almacena las fotos de RF04 |
| Inventario | RF05, RF06, RF07, RF14, RF18 |
| Ventas | RF09, RF10, RF15 |
| Caja | RF08, RF11, RF12 |
| Reportes | RF13, RF17 |
| Unidad de trabajo | RF10; AC06 |
