# Nivel 4 · Diagrama de código

> **Proyecto:** Plataforma SaaS de pastelerías · **Componente ampliado:** Ventas  
> **Estado:** Diseño de clases y contratos; implementación completa pendiente.

## 1. Objetivo

Ampliar Ventas de [C4 nivel 3](Nivel3-Diagrama-de-Componentes.md): confirmación de una venta presencial.

## 2. Diagrama de clases

![Clases y contratos de confirmación de venta](../../img/nivel4-clases.png)

| Elemento | Tipo y ubicación | Responsabilidad |
|---|---|---|
| VentasController | Clase de Presentación | Traduce HTTP y entrega contexto autorizado. |
| ConfirmarVenta | Caso de uso de Aplicación | Coordina la confirmación dentro de una unidad de trabajo. |
| UnidadDeTrabajo | Interfaz de Aplicación compartida | Garantiza commit conjunto o rollback completo. |
| ContextoTransaccional | Conjunto de puertos de Aplicación | Proporciona contratos de Catálogo, Inventario, Caja, Ventas e Idempotencia ligados a una transacción. |
| Venta | Entidad de Dominio | Valida detalles y calcula total en céntimos. |
| DetalleVenta | Valor del Dominio | Producto, cantidad y precio histórico de cada línea. |
| UnidadDeTrabajoPrisma | Adaptador de Infraestructura | Abre la transacción, establece tenant y conecta adaptadores. |
| VentaRepositoryPrisma | Adaptador de Infraestructura | Guarda venta y detalles mediante el mismo tx. |

Los puertos de Caja, Inventario y Catálogo se muestran como colaboradores del componente ampliado. Son contratos entre módulos, no servicios remotos.

## 3. Notación

| Símbolo | Significado |
|---|---|
| Flecha continua | Uso de una clase o contrato. |
| Línea discontinua con triángulo hueco | Implementación de una interfaz. |
| Rombo relleno | Composición de Venta con sus detalles. |
| `interface` | Contrato sin dependencia de tecnología. |
| `+` / `-` | Miembro público / privado. |

## 4. Secuencia de confirmación

![Secuencia de venta y rollback](../../img/secuencia-venta.png)

La secuencia es una vista dinámica complementaria; no reemplaza el diagrama de clases del nivel 4. Presenta el flujo exitoso y la alternativa de error antes del commit.

| Condición | Resultado esperado |
|---|---|
| Venta válida, caja abierta y stock apto | Venta, cobros y movimientos confirmados conjuntamente. |
| Stock insuficiente o lote vencido | Conflicto controlado; ninguna escritura parcial. |
| Caja cerrada o fuera del ámbito del usuario | Operación rechazada antes de confirmar. |
| Misma clave y mismo comando | Se devuelve el resultado original sin repetir movimientos. |
| Misma clave y contenido diferente | Conflicto de idempotencia. |
| Falla después del commit y antes de responder | El reintento recupera el resultado persistido. |

## 5. Relación con archivos y requisitos

- [Estructura y código TypeScript](../03-diseño-de-software/diseño-interno/diseño-interno-de-modulos.md).
- Confirmación: RF08–RF10, RF18. Autorización: RF03, RF16.
- Integridad y trazabilidad: AC06, AC07.

- Verificar con PostgreSQL: reintentos, aislamiento y rollback.
