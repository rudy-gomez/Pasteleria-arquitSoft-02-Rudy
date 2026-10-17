# Drivers arquitectónicos

Los **drivers arquitectónicos** identificados para el sistema son los siguientes:

| ID | Driver arquitectónico | Origen | ¿Por qué influye en la arquitectura? |
|---|---|---|---|
| DA01 | El sistema debe admitir el crecimiento de negocios y sucursales. | AC03 – Escalabilidad | Influye en la organización del servicio compartido y su despliegue. |
| DA02 | El sistema debe responder con rapidez durante la atención. | AC01 – Rendimiento | Influye en consultas, índices, límites de reportes y medición de carga. |
| DA03 | El sistema debe aislar los datos de cada negocio y controlar el acceso por sucursal. | AC04 – Seguridad; RC03 – Multi-tenant | Condiciona identidad, autorización y protección de datos. |
| DA04 | El sistema debe registrar venta, cobro y stock de forma consistente ante concurrencia. | AC06 – Integridad; RF10 – Venta | Condiciona transacciones, bloqueos e idempotencia. |
| DA05 | El sistema debe conservar y recuperar información operativa verificable. | AC02 – Disponibilidad; AC07 – Trazabilidad | Influye en movimientos, auditoría, copias y restauración. |
| DA06 | El sistema debe permitir cambiar reglas sin afectar innecesariamente otros módulos. | AC05 – Mantenibilidad | Influye en la modularidad y dirección de dependencias. |
