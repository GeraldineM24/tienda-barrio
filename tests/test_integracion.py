import pytest
import sys
sys.path.insert(0, 'src')
from inventario.gestion_inventario import GestionInventario
from ventas.gestion_ventas import GestionVentas


class TestIntegracion:
    """
    Pruebas de integración entre módulo de inventario y ventas.
    """

    def setup_method(self):
        self.inv = GestionInventario()
        self.ventas = GestionVentas()

    def test_venta_descuenta_inventario(self):
        """Al registrar una venta, el stock del inventario debe reducirse."""
        self.inv.agregar_producto("Arroz", 2.0, 20)
        self.ventas.registrar_venta("Arroz", 5, 2.0)
        self.inv.actualizar_stock("Arroz", -5)
        assert self.inv.inventario["Arroz"]["stock"] == 15

    def test_venta_producto_sin_stock(self):
        """No se puede vender más de lo que hay en stock."""
        self.inv.agregar_producto("Aceite", 3.0, 2)
        with pytest.raises(ValueError):
            self.inv.actualizar_stock("Aceite", -5)

    def test_total_ventas_coincide_con_inventario(self):
        """El total del día debe calcularse correctamente."""
        self.inv.agregar_producto("Pan", 0.8, 50)
        self.ventas.registrar_venta("Pan", 10, 0.8)
        self.ventas.registrar_venta("Pan", 5, 0.8)
        total = self.ventas.calcular_total_dia()
        assert total == 12.0