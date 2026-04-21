from typing import Dict, List, Optional, Tuple, Union
import re


class GestionInventario:
    """
    Clase para gestionar el inventario de una tienda de barrio.
    Usa un diccionario para almacenar productos: {nombre: {'precio': float, 'stock': int}}
    """
    
    def __init__(self) -> None:
        self.inventario: Dict[str, Dict[str, Union[float, int]]] = {}
    
    def agregar_producto(self, nombre: str, precio: float, stock: int) -> None:
        """
        Agrega o actualiza un producto en el inventario.
        
        :param nombre: Nombre del producto (str, no vacío)
        :param precio: Precio del producto (> 0.0)
        :param stock: Stock inicial (>= 0)
        :raises ValueError: Si parámetros inválidos
        """
        nombre = nombre.strip()
        if not nombre or not re.match(r"^[a-zA-ZÁÉÍÓÚÑÜ \-\_\.]+$", nombre):
            raise ValueError("Nombre debe ser no vacío y solo caracteres alfanuméricos válidos (incluye acentos)")
        precio = float(precio)
        stock = int(stock)
        if precio <= 0:
            raise ValueError("Precio debe ser mayor a 0")
        if stock < 0:
            raise ValueError("Stock debe ser >= 0")
        
        self.inventario[nombre] = {'precio': precio, 'stock': stock}
    
    def eliminar_producto(self, nombre: str) -> bool:
        """
        Elimina un producto del inventario.
        
        :param nombre: Nombre del producto
        :return: True si eliminado, False si no existía
        """
        if nombre in self.inventario:
            del self.inventario[nombre]
            return True
        return False
    
    def actualizar_stock(self, nombre: str, cantidad: int) -> None:
        """
        Actualiza el stock de un producto (suma cantidad).
        
        :param nombre: Nombre del producto
        :param cantidad: Cantidad a sumar (puede ser negativa para restar)
        :raises KeyError: Si producto no existe
        :raises ValueError: Si stock quedaría negativo
        """
        if nombre not in self.inventario:
            raise KeyError(f"Producto '{nombre}' no encontrado")
        
        nuevo_stock = self.inventario[nombre]['stock'] + cantidad
        if nuevo_stock < 0:
            raise ValueError("Stock no puede ser negativo")
        
        self.inventario[nombre]['stock'] = nuevo_stock
    
    def buscar_producto(self, nombre: str) -> Optional[Dict[str, Union[float, int]]]:
        """
        Busca un producto por nombre exacto.
        
        :param nombre: Nombre del producto
        :return: Dict del producto o None si no encontrado
        """
        nombre = nombre.strip()
        return self.inventario.get(nombre)

    def buscar_productos(self, patron: str) -> List[Tuple[str, Dict[str, Union[float, int]]]]:
        """
        Busca productos por patrón (coincidencia parcial, case-insensitive).
        
        :param patron: Patrón de búsqueda
        :return: Lista de (nombre, info) que coincidan
        """
        if not patron:
            return []
        patron_lower = patron.lower().strip()
        return [(n, info) for n, info in self.inventario.items() 
                if patron_lower in n.lower()]
    
    def listar_productos(self) -> List[Tuple[str, float, int]]:
        """
        Lista todos los productos ordenados por nombre.
        
        :return: Lista de tuplas (nombre, precio, stock)
        """
        productos = [(nombre, info['precio'], info['stock']) 
                    for nombre, info in sorted(self.inventario.items())]
        return productos
    
    def __str__(self) -> str:
        if not self.inventario:
            return "Inventario vacío"
        
        lines = ["Inventario:"]
        for nombre, info in sorted(self.inventario.items()):
            lines.append(f"  - {nombre}: ${info['precio']:.2f}, stock: {info['stock']}")
        return "\n".join(lines)


# Ejemplo de uso (opcional, para pruebas)
if __name__ == "__main__":
    gi = GestionInventario()
    gi.agregar_producto("Leche", 1.5, 10)
    gi.agregar_producto("Pan", 0.8, 20)
    print(gi)
    print("Buscar Leche:", gi.buscar_producto("Leche"))
    print("Lista:", gi.listar_productos())

