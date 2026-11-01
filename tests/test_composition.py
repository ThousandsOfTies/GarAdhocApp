import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'sources/gar-tools/composition'))
from product import Product
from python_app import package


class CompositionTests(unittest.TestCase):
    def test_shared_board_data_validates_gpio_spi_and_i2c_without_claiming_a_port(self):
        product = Product(ROOT).validate()
        self.assertEqual('raspberry-pi-5', product.board['id'])
        self.assertEqual(4, len(product.gpio))
        self.assertEqual(1, len(product.spi))
        self.assertEqual(2, len(product.i2c))
        self.assertEqual('planned', product.describe()['status'])

    def test_unfinished_physical_target_still_refuses_build_and_package(self):
        product = Product(ROOT)
        with self.assertRaisesRegex(ValueError, 'planned'):
            product.build()
        with self.assertRaisesRegex(ValueError, 'planned'):
            package(product, 'artifacts/must-not-build')


if __name__ == '__main__':
    unittest.main()
