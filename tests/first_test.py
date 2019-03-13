import json
import os
from definitions import CONFIG_PATH
from simulator.pictures_generation import right_direction
from tests.fixtures import clone_template


def test_right_direction_should_save_twice_as_many_images_as_configuration():
    with clone_template(template_name='scenario_photo_simple') as path:
        # Given
        output_path = path + '/output'
        configuration = json.load(open(CONFIG_PATH))
        configuration['images_curve'] = 3

        # Where
        right_direction(configuration, execution_dir_path=path, output_dir=output_path)

        # Then
        image_number = count_png(output_path)
        assert image_number == 2 * configuration['images_curve']


def count_png(photos_path_test):
    images_produced_by_povray = [x for x in os.listdir(photos_path_test) if x.endswith('.png')]
    image_number_init = len(images_produced_by_povray)
    return image_number_init
