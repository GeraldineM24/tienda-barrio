class GestionVentas:
    """
    Clase para gestionar las ventas de una tienda de barrio.
    Usa una lista de diccionarios para almacenar las ventas.
    """

    def __init__(self):
        self.ventas = []
        self.contador_id = 1

    def registrar_venta(self, producto, cantidad, precio_unitario):
        """
        Registra una nueva venta.
        """
        if not producto:
            raise ValueError("El nombre del producto no puede estar vacío")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        if precio_unitario <= 0:
            raise ValueError("El precio debe ser mayor a 0")

        venta = {
            'id': self.contador_id,
            'producto': producto,
            'cantidad': cantidad,
            'precio_unitario': precio_unitario,
            'total': cantidad * precio_unitario
        }
        self.ventas.append(venta)
        self.contador_id += 1
        return venta

    def ver_historial(self):
        """
        Retorna el historial completo de ventas.
        """
        if not self.ventas:
            return "No hay ventas registradas"
        return self.ventas

    def calcular_total_dia(self):
        """
        Calcula el total de todas las ventas del día.
        """
        return sum(venta['total'] for venta in self.ventas)

    def cancelar_venta(self, id_venta):
        """
        Cancela una venta por su ID.
        """
        for venta in self.ventas:
            if venta['id'] == id_venta:
                self.ventas.remove(venta)
                return True
        return False

    def __str__(self):
        if not self.ventas:
            return "No hay ventas registradas"
        lines = ["Historial de Ventas:"]
        for venta in self.ventas:
            lines.append(
                f"  ID {venta['id']}: {venta['producto']} "
                f"x{venta['cantidad']} = ${venta['total']:.2f}"
            )
        lines.append(f"  TOTAL DÍA: ${self.calcular_total_dia():.2f}")
        return "\n".join(lines)


# Prueba
if __name__ == "__main__":
    gv = GestionVentas()
    gv.registrar_venta("Arroz", 3, 1.50)
    gv.registrar_venta("Aceite", 1, 3.00)
    print(gv)
    print("Total del día:", gv.calcular_total_dia())
