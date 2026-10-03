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

---

## Justificación
La separación en capas aísla responsabilidades: presentación gestiona la
interacción multi-tenant por sub-ruta, la lógica de negocio concentra las
reglas de los 5 módulos funcionales, y la capa de datos combina caché
(rendimiento), pool de conexiones (estabilidad bajo carga) y réplica de
lectura (aislar reportes). Esta organización responde directamente a los
drivers de **concurrencia** (DA01), **rendimiento** (DA02) y
**escalabilidad** (DA03).