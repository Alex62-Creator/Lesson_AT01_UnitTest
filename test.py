import unittest
from main import modulus

# Создаем класс производный от unittest.TestCase
class ModulusTest(unittest.TestCase):
    # Функция для проверки правильности вычислений
    def test_modulus_success(self):
        # Проверка на равенство
        self.assertEqual(modulus(10, 5), 0)
        self.assertEqual(modulus(65, 3), 0)
        self.assertEqual(modulus(70, 2), 3)

        # Проверка на неравенство
        self.assertNotEqual(modulus(10, 5), 0)
        self.assertNotEqual(modulus(65, 3), 0)
        self.assertNotEqual(modulus(70, 2), 3)

    # Функция для проверки условия деления на 0
    def test_modulus_by_zero(self):
        # Проверка возникновения исключения ValueError
        self.assertRaises(ValueError, modulus, 15, 0)
        # Проверка возникновения исключения TypeError
        self.assertRaises(TypeError, modulus, 15, 0)

# Запускаем проверку
if __name__ == '__main__':
    unittest.main()