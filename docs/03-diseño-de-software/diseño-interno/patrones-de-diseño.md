# Patrones de diseño

## Objetivo

Definir cómo se separan la persistencia, las transacciones y el almacenamiento de fotografías.

## Contexto

- **Estilo:** monolito modular con Node.js, Express y TypeScript.
- **Enfoque:** Clean Architecture.
- **Referencia:** Ventas y Catálogo.

## Patrones aplicados al diseño

| Patrón | Dónde se usa | Problema que resuelve | Se implementa con | Archivos previstos |
|---|---|---|---|---|
| Repository | Ventas → PostgreSQL | Guardar ventas sin SQL en el caso de uso. | Prisma y PostgreSQL | `venta-repository.ts`, `venta-repository-prisma.ts` |
| Unit of Work | Ventas + Inventario + Caja | Evitar que una operación quede guardada parcialmente. | Una transacción Prisma | `unidad-de-trabajo.ts`, `unidad-de-trabajo-prisma.ts` |
| Adapter | Catálogo → fotografías | Separar el caso de uso de la API del proveedor. | API compatible con S3 de R2 | `almacen-imagenes.ts`, `almacen-imagenes-r2.ts` |

## Cómo funciona cada patrón

| Patrón | En pocas palabras |
|---|---|
| Repository | `guardar(venta)` conserva cabecera y detalles mediante el adaptador. |
| Unit of Work | Confirma venta, stock, cobros e historial juntos; ante un error revierte todo. |
| Adapter | Traduce `guardar(clave, contenido, tipo)` a la operación de R2. |

## Composición

| Técnica | Aplicación |
|---|---|
| Inyección de dependencias | `composition.ts` conecta adaptadores; `ventas.module.ts` construye el caso de uso y controlador. |

## Beneficios

- Probar reglas sin conectar servicios externos.
- Sustituir el proveedor de imágenes conservando su contrato.
- Mantener consistentes Ventas, Inventario y Caja.

## Reglas de implementación

| Operación | Regla |
|---|---|
| Confirmar venta | Todos los adaptadores reciben el mismo cliente transaccional. |
| Reintentar | Misma clave y contenido: mismo resultado; contenido distinto: conflicto. |
| Subir imagen | Validar permiso, tamaño y formato; guardar clave y metadatos. |
| Fallar al guardar metadatos | Eliminar el objeto cargado o registrar limpieza pendiente. |
| Llamar a R2 | Fuera de una transacción SQL abierta. |
