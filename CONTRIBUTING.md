# Guía de Contribución — Tienda Barrio 🏪

## 📋 Descripción del Proyecto
Sistema de gestión para tienda de barrio desarrollado en Python.
Incluye módulos de inventario, ventas y reportes.

## 🌿 Estrategia de Ramas (GitHub Flow)
- `main` → código estable y aprobado
- `feature/inventario` → módulo de inventario
- `feature/ventas` → módulo de ventas

## 📝 Convenciones de Nombres
### Archivos y carpetas
- Usar **snake_case**: `gestion_inventario.py`
- Carpetas en minúsculas: `src/inventario/`

### Variables y funciones
- **snake_case**: `precio_producto`, `calcular_total()`

### Clases
- **PascalCase**: `GestionInventario`, `RegistroVenta`

### Constantes
- **MAYÚSCULAS**: `PRECIO_MAXIMO`, `IVA_PORCENTAJE`

## 📁 Estructura de Carpetas
tienda-barrio/
├── src/
│   ├── inventario/    # Gestión de productos
│   ├── ventas/        # Registro de ventas
│   └── reportes/      # Generación de reportes
├── tests/             # Pruebas unitarias
├── docs/              # Documentación
└── requirements.txt   # Dependencias

## ✅ Pasos para Contribuir
1. Trabaja siempre en tu rama asignada
2. Haz commits pequeños y descriptivos
3. Antes de hacer Push, verifica que el código funcione
4. Crea un Pull Request hacia `main`
5. Espera revisión del compañero antes de hacer merge

## 💬 Formato de Commits
tipo: descripción corta
Ejemplos:
feat: agregar función de registro de producto
fix: corregir cálculo de total en ventas
test: agregar pruebas para módulo inventario
docs: actualizar guía de contribución

## 🚫 Reglas del Equipo
- No hacer push directo a `main`
- Todo código debe tener al menos un comentario explicativo
- Los nombres de variables deben estar en español
- Cada función debe tener su docstring explicando qué hace