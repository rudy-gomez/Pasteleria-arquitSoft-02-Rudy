# Escenarios de atributos de calidad de la plataforma de pastelerías


## EQ-01. Rendimiento: consulta y venta

| Elemento | Descripción |
|---|---|
| **Fuente del estímulo** | Empleado / Cajero |
| **Estímulo** | Busca productos o confirma una venta. |
| **Artefacto** | Catálogo, Ventas y consultas a PostgreSQL. |
| **Entorno** | Prueba con 30 usuarios virtuales, datos sintéticos y recursos documentados. |
| **Respuesta** | La plataforma responde sin errores técnicos inesperados. |
| **Medida de la respuesta** | Objetivo de diseño: p95 de hasta 2 segundos y ningún error 5xx durante la carga objetivo. |

## EQ-02. Disponibilidad: recuperación del servicio

| Elemento | Descripción |
|---|---|
| **Fuente del estímulo** | Fallo de aplicación o base de datos |
| **Estímulo** | Se interrumpe el servicio o se requiere restaurar una copia. |
| **Artefacto** | API, PostgreSQL y procedimiento de restauración. |
| **Entorno** | Entorno de prueba aislado con copias disponibles. |
| **Respuesta** | El servicio se recupera y los datos restaurados son consistentes. |
| **Medida de la respuesta** | Objetivo de diseño: disponibilidad mensual de 99%, RPO de hasta 15 minutos y RTO de hasta 4 horas. |

## EQ-03. Escalabilidad: aumento de carga

| Elemento | Descripción |
|---|---|
| **Fuente del estímulo** | Incremento de actividad |
| **Estímulo** | Aumentan usuarios y sucursales activos. |
| **Artefacto** | API, consultas y pool de conexiones. |
| **Entorno** | Mismo dataset y mezcla de operaciones, con infraestructura registrada. |
| **Respuesta** | La plataforma atiende la carga creciente manteniendo la latencia objetivo y sin errores 5xx. |
| **Medida de la respuesta** | Objetivo de diseño: mantener p95 de hasta 2 segundos y cero errores 5xx al pasar de 10 a 30 usuarios virtuales. |

## EQ-04. Seguridad: aislamiento entre negocios

| Elemento | Descripción |
|---|---|
| **Fuente del estímulo** | Usuario sin permiso |
| **Estímulo** | Solicita una operación o un recurso de otro negocio o sucursal. |
| **Artefacto** | Acceso, repositorios y archivos por negocio. |
| **Entorno** | Sesiones válidas e inválidas; identificadores modificados en solicitudes. |
| **Respuesta** | Se rechaza el acceso sin revelar ni modificar datos ajenos. |
| **Medida de la respuesta** | Rechazar el 100% de los accesos indebidos de la matriz definida. |

## EQ-05. Mantenibilidad: cambio de reglas

| Elemento | Descripción |
|---|---|
| **Fuente del estímulo** | Equipo de desarrollo |
| **Estímulo** | Modifica una regla de venta o un adaptador de archivos. |
| **Artefacto** | Dominio, casos de uso y adaptadores. |
| **Entorno** | Código organizado por módulos y pruebas disponibles. |
| **Respuesta** | El cambio mantiene los contratos y no introduce dependencias de tecnología en el dominio. |
| **Medida de la respuesta** | Pruebas afectadas y de regresión aprobadas; dominio sin imports de Express o Prisma. |

## EQ-06. Integridad: ventas entre sucursales y reintento

| Elemento | Descripción |
|---|---|
| **Fuente del estímulo** | Empleados de distintas sucursales o pastelerías; un responsable de registro por sucursal. |
| **Estímulo** | Registran ventas simultáneas en sus locales; uno reenvía la misma confirmación. |
| **Artefacto** | Ventas, Inventario, Caja y registro idempotente. |
| **Entorno** | PostgreSQL real; sucursales A y B con una unidad disponible cada una y cajas abiertas. |
| **Respuesta** | Cada venta afecta solo a su negocio y sucursal; el reintento devuelve el resultado original. |
| **Medida de la respuesta** | Dos ventas únicas, un descuento y un registro de cobro por venta; stock final cero en A y B, sin duplicados ni operaciones parciales. |

## EQ-07. Trazabilidad: inventario y efectivo

| Elemento | Descripción |
|---|---|
| **Fuente del estímulo** | Empleado / Cajero y administrador de cadena |
| **Estímulo** | Registran una merma, una anulación y una entrega de efectivo. |
| **Artefacto** | Movimientos de inventario, caja y auditoría. |
| **Entorno** | Operaciones autorizadas con movimientos anteriores disponibles. |
| **Respuesta** | Cada operación conserva responsable, fecha, motivo y referencia. |
| **Medida de la respuesta** | El 100% de las operaciones de prueba se reconstruye sin duplicar stock ni efectivo. |

## Resumen de escenarios

| Código | Atributo de calidad | Qué se busca comprobar |
|---|---|---|
| EQ-01 | Rendimiento | consulta y venta |
| EQ-02 | Disponibilidad | recuperación del servicio |
| EQ-03 | Escalabilidad | aumento de carga |
| EQ-04 | Seguridad | aislamiento entre negocios |
| EQ-05 | Mantenibilidad | cambio de reglas |
| EQ-06 | Integridad y concurrencia | venta concurrente y reintento |
| EQ-07 | Trazabilidad | inventario y efectivo |