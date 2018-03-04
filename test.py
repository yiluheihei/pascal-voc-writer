import os
from pascal_voc_writer import Writer as PascalWriter


def test_1(results_dir):
    pascal_writer = PascalWriter('test-image.png', 100, 100)
    pascal_writer.addObject(name='triangle', xy_coords=[5, 5, 95, 5, 50, 95])
    pascal_writer.save(os.path.join(results_dir,
                                    'test-annotation-triangle.xml'))


def test_2(results_dir):
    pascal_writer = PascalWriter('test-image.png', 100, 100)
    pascal_writer.addObject(name='bndbox',
                            xy_coords=[5, 5, 95, 5, 95, 95, 5, 95])
    pascal_writer.save(os.path.join(results_dir, 'test-annotation-bndbox.xml'))


if __name__ == '__main__':
    TEST_RESULTS_DIR = os.path.abspath('test-results')
    if not os.path.exists(TEST_RESULTS_DIR):
        os.makedirs(TEST_RESULTS_DIR)
    test_1(TEST_RESULTS_DIR)
    test_2(TEST_RESULTS_DIR)
