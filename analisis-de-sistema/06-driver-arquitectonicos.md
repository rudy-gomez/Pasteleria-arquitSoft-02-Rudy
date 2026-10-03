# 🧭 Drivers Arquitectónicos

## Objetivo
Integrar los requisitos, atributos de calidad y restricciones
identificados, y determinar cuáles tienen una influencia significativa
en las decisiones de arquitectura.

---

| ID | Driver arquitectónico | Origen | ¿Por qué influye en la arquitectura? |
|---|---|---|---|
| **DA01** | El sistema debe evitar que dos solicitudes comprometan el mismo producto simultáneamente. | AC02 – Concurrencia | Exige mecanismos de bloqueo transaccional (SELECT FOR UPDATE) y reserva temporal con TTL. |
| **DA02** | El sistema debe resolver consultas de stock en menos de 2 segundos bajo carga pico. | AC01 – Rendimiento | Justifica la incorporación de una capa de caché (Redis) entre la aplicación y la base de datos. |
| **DA03** | El sistema debe escalar horizontalmente al incorporar nuevas pastelerías. | AC04 – Escalabilidad | Condiciona el uso de un balanceador de carga y múltiples instancias de servidores de aplicación. |
| **DA04** | El sistema debe garantizar aislamiento lógico de datos entre cuentas distintas. | AC06 – Seguridad multi-tenant | Condiciona el modelo de datos (tenant_id en tablas principales) y la capa de autorización. |
| **DA05** | La base de datos no debe agotar conexiones bajo picos de escritura simultánea. | RC06 – Pool de conexiones | Justifica la incorporación de PgBouncer entre la aplicación y PostgreSQL. |
| **DA06** | Los reportes no deben afectar el rendimiento de las operaciones transaccionales. | RC04 – Réplica de lectura | Justifica separar la carga de reportes en una réplica de lectura independiente. |