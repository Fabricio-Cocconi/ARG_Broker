import unittest
from usuario import Usuario

class TestUsuario(unittest.TestCase):
    def test_crear_usuario(self):
        usuario = Usuario(1, 'Adriel', 'Delosanto', '20-12345678-9', 'adridelosanto.com', 'hola123')
        self.assertEqual(usuario.nombre, 'Adriel')
        self.assertEqual(usuario.saldo, 1000000.00)

if __name__ == '__main__':
    unittest.main()
