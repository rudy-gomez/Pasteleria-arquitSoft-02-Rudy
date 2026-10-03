# 🚧 Restricciones

## Objetivo
Identificar las condiciones, reglas o limitaciones que deben respetarse
durante el desarrollo del sistema.

---

| ID | Restricción | Descripción |
|---|---|---|
| **RC01** | Aplicación web responsiva | El sistema debe ser accesible desde navegador web, utilizable desde tablet o celular (no se contemplan apps móviles nativas). |
| **RC02** | Control de versiones | El código fuente debe gestionarse utilizando Git y mantenerse en un repositorio compartido. |
| **RC03** | API REST | La comunicación entre el frontend y los servicios del sistema debe realizarse mediante una API REST. |
| **RC04** | Base de datos PostgreSQL | La información transaccional debe almacenarse en PostgreSQL, con una réplica de lectura para reportes. |
| **RC05** | Caché Redis | Las consultas de stock y catálogo deben resolverse contra una capa de caché en memoria (Redis). |
| **RC06** | Pool de conexiones | El acceso a la base de datos debe gestionarse mediante PgBouncer para evitar agotamiento de conexiones. |
| **RC07** | Sin pasarela de pago en línea | El pago se realiza de forma presencial o contra entrega; no se integra pasarela de pago en esta fase. |
| **RC08** | Sin facturación electrónica | Queda fuera de alcance por requerir homologación con SUNAT; se plantea como fase posterior. |
| **RC09** | Multi-tenant por sub-ruta | El sitio web de cada pastelería opera bajo una sub-ruta del dominio de la plataforma (no dominios propios). |