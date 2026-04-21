import pytest
import sys
sys.path.insert(0, 'src')
from inventario.gestion_inventario import GestionInventario

class TestGestionInventario:

    def setup_method(self):
        self.inv = GestionInventario()

    def test_agregar_producto_exitoso(self):
        self.inv.agregar_producto("Leche", 1.5, 10)
        assert "Leche" in self.inv.inventario

    def test_agregar_producto_precio_invalido(self):
        with pytest.raises(ValueError):
            self.inv.agregar_producto("Leche", -1, 10)

    def test_agregar_producto_stock_negativo(self):
        with pytest.raises(ValueError):
            self.inv.agregar_producto("Leche", 1.5, -1)

    def test_eliminar_producto_existente(self):
        self.inv.agregar_producto("Pan", 0.8, 20)
        resultado = self.inv.eliminar_producto("Pan")
        assert resultado == True
        assert "Pan" not in self.inv.inventario

    def test_eliminar_producto_inexistente(self):
        resultado = self.inv.eliminar_producto("NoExiste")
        assert resultado == False

    def test_actualizar_stock(self):
        self.inv.agregar_producto("Arroz", 2.0, 10)
        self.inv.actualizar_stock("Arroz", 5)
        assert self.inv.inventario["Arroz"]["stock"] == 15

    def test_actualizar_stock_negativo(self):
        self.inv.agregar_producto("Arroz", 2.0, 5)
        with pytest.raises(ValueError):
            self.inv.actualizar_stock("Arroz", -10)

    def test_buscar_producto_existente(self):
        self.inv.agregar_producto("Leche Entera", 3.0, 8)
        resultado = self.inv.buscar_producto("Leche Entera")
        assert resultado is not None
        assert resultado["precio"] == 3.0

    def test_buscar_producto_inexistente(self):
        resultado = self.inv.buscar_producto("NoExiste")
        assert resultado is None

    def test_listar_productos(self):
        self.inv.agregar_producto("Leche", 1.5, 10)
        self.inv.agregar_producto("Pan", 0.8, 20)
        lista = self.inv.listar_productos()
        assert len(lista) == 2