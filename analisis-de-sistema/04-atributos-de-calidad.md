# 🎯 Atributos de Calidad

## Objetivo
Determinar cómo debe comportarse el sistema, más allá de qué debe hacer.
Basado en los requisitos no funcionales (RNF) definidos en la propuesta.

**Escenario crítico:** dos solicitudes simultáneas (venta en mostrador y
pedido web) intentan comprometer el mismo producto; además, el sistema
debe sostener el crecimiento de la cadena en número de sucursales.

---

| ID | Atributo de calidad | Escenario de calidad |
|---|---|---|
| **AC01** | Rendimiento | Las consultas de disponibilidad de stock deben resolverse en menos de 2 segundos bajo condiciones de carga pico (fines de semana, fechas festivas). |
| **AC02** | Concurrencia | El sistema debe soportar múltiples ventas y pedidos simultáneos (panel interno y sitio web) sin comprometer dos veces el mismo stock. |
| **AC03** | Disponibilidad | El sistema debe mantener una disponibilidad mínima de 99%, dado que la operación es diaria y continua durante el horario de atención. |
| **AC04** | Escalabilidad | La arquitectura debe permitir incorporar servidores de aplicación adicionales a medida que se registran nuevas pastelerías, sin afectar la disponibilidad. |
| **AC05** | Integridad de datos | Toda operación de descuento de stock y cierre de turno debe ejecutarse dentro de una transacción atómica. |
| **AC06** | Seguridad multi-tenant | El sistema debe garantizar el aislamiento lógico de los datos entre cuentas distintas. |
| **AC07** | Seguridad de acceso | El acceso debe estar protegido mediante autenticación cifrada y permisos diferenciados por rol. |
| **AC08** | Usabilidad | La interfaz del panel interno debe ser utilizable desde tablet o celular en el punto de venta. |