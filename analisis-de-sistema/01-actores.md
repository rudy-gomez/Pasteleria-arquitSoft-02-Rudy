# 👥 Actores del Sistema

## Objetivo
Identificar a las personas, organizaciones y sistemas externos que
interactúan con la plataforma SaaS de gestión de pastelerías.

---

## 🙋 Actores humanos

| Actor | ¿Qué necesita realizar? |
|---|---|
| **Superadministrador** | Registrar cuentas de pastelería/cadena, visualizar el listado de cuentas y su estado (activa/inactiva), administrar la plataforma en general. |
| **Administrador de Cadena** | Registrar sucursales, gestionar inventario y empleados de sus sucursales, activar el sitio web público, visualizar reportes consolidados de todas sus sucursales. |
| **Administrador de Pastelería** | Registrar empleados, asignar turnos, gestionar el catálogo e inventario de su sucursal. |
| **Empleado** | Registrar ventas en mostrador, registrar pedidos anticipados, realizar cierre de caja por turno. |
| **Cliente (sitio web)** | Consultar el catálogo público, generar pedidos anticipados desde el sitio web de su pastelería. |

## 🌐 Sistemas externos

| Sistema externo | ¿Qué necesita realizar? |
|---|---|
| **Redis (caché)** | Resolver consultas de stock y catálogo sin sobrecargar la base de datos principal. |
| **PgBouncer (pool de conexiones)** | Evitar el agotamiento de conexiones a PostgreSQL bajo picos de carga. |
| **PostgreSQL (réplica de lectura)** | Atender consultas de reportes sin afectar la carga transaccional. |
| **Impresora térmica (opcional)** | Imprimir el ticket de venta en el punto de venta. |

---

## 📌 Resumen
El sistema cuenta con **5 actores humanos** organizados jerárquicamente
(Superadministrador → Administrador de Cadena → Administrador de Pastelería
→ Empleado, además del Cliente externo) y **4 sistemas externos** de
soporte (caché, pool de conexiones, réplica de BD, impresora).