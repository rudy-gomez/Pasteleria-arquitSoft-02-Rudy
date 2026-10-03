# 🏗️ Arquitectura Inicial del Sistema

## Descripción general
La arquitectura se organiza en **tres capas principales**, con
escalamiento horizontal en la capa de aplicación:

| Capa | Pregunta que responde |
|---|---|
| **Presentación** | ¿Cómo interactúa el usuario? |
| **Lógica de negocio** | ¿Qué hace el sistema? |
| **Datos** | ¿Dónde se almacena la información? |

El balanceador de carga resuelve además el ruteo multi-tenant por
sub-ruta. Se incorpora una capa de caché (Redis) para consultas de
stock/catálogo, un pool de conexiones (PgBouncer) y una réplica de
lectura para aislar la carga de reportes.

---

## Diagrama de arquitectura

```mermaid
flowchart TD

    subgraph ACTORES["👥 ACTORES"]
        Super["Superadministrador"]
        AdminCadena["Admin. de Cadena"]
        AdminPast["Admin. de Pastelería"]
        Empleado["Empleado"]
        Cliente["Cliente (web)"]
    end

    subgraph PRESENTACION["🖥️ PRESENTACIÓN"]
        LB["Balanceador de carga\n(ruteo multi-tenant)"]
        Web["Aplicación Web → API REST"]
    end

    subgraph NEGOCIO["⚙️ LÓGICA DE NEGOCIO"]
        Cuentas["Cuentas y Sucursales"]
        Catalogo["Catálogo e Inventario"]
        Traslados["Traslados"]
        Turnos["Empleados / Turnos / Caja"]
        Ventas["Ventas y Pedidos"]
        Reportes["Reportes"]
    end

    subgraph DATOS["🗄️ DATOS"]
        Cache["Redis (caché)"]
        Pool["PgBouncer"]
        BD["PostgreSQL (principal)"]
        Replica["PostgreSQL (réplica lectura)"]
    end

    ACTORES --> PRESENTACION
    PRESENTACION --> NEGOCIO
    NEGOCIO --> Cache
    NEGOCIO --> Pool
    Pool --> BD
    Reportes --> Replica
```
## Diagrama de arquitectura (Archify)

<p align="center">
  <a href="pasteleria-saas-blanco.svg">
    <img src="pasteleria-saas-blanco.svg" alt="Arquitectura SaaS de gestión de pastelerías: actores, balanceador multi-tenant, aplicación web, seis módulos de negocio, Redis, PgBouncer y PostgreSQL principal y réplica." width="100%">
  </a>
</p>

<p align="center">
  <a href="pasteleria-saas-blanco.svg">Ver imagen completa</a> ·
  <a href="pasteleria-saas.html">Diagrama interactivo</a>
</p>

Los seis módulos acceden a Redis (conexiones verdes) y a PgBouncer (conexiones grises). PgBouncer se conecta al PostgreSQL principal; Reportes dispone además de una conexión directa a la réplica de lectura. Los cruces de líneas no representan conexiones entre ellas.

La imagen mantiene el fondo blanco. Para cambiar de tema, ampliar o exportar, descarga el HTML y ábrelo en el navegador. El contenido está en español; los controles del visor y su idioma HTML usan inglés por defecto.

---

## Justificación
La separación en capas aísla responsabilidades: presentación gestiona la
interacción multi-tenant por sub-ruta, la lógica de negocio concentra las
reglas de los 5 módulos funcionales, y la capa de datos combina caché
(rendimiento), pool de conexiones (estabilidad bajo carga) y réplica de
lectura (aislar reportes). Esta organización responde directamente a los
drivers de **concurrencia** (DA01), **rendimiento** (DA02) y
**escalabilidad** (DA03).