import pytest
from _pytest.logging import LogCaptureFixture

from simulator import configuration
from simulator.configuration import ConfigurationError


def test_initialize_should_show_a_warning_with_default_value_when_road_median_line_color_is_missing(caplog:LogCaptureFixture):
    """
    Ce test sera invalide lors de l'abandon du support de la version 2019/02/23
    car l'option road_median_line_color sera obligatoire.
    :return:
    """

    if '2019/02/23' not in configuration.SUPPORTED_VERSIONS:
        pytest.fail('ce test est deprecated car l attribut est devenu obligatoire : road_median_line_color')

    mock_configuration = {
        'version' : '2019/02/23'
    }

    c = configuration._initialize(mock_configuration, configuration_path = 'configuration.json')

    assert c['road_median_line_color'] == (102, 236, 4)
    assert 'road_median_line_color is missing from configuration.json. default value : #66ec04' in caplog.messages


def test_initialize_raises_an_error_when_road_median_line_color_value_is_not_hexadecimal():
    wrong_color_value = 'red'
    mock_configuration = {
        'version' : '2019/02/23',
        'road_median_line_color': wrong_color_value
    }

    with pytest.raises(ConfigurationError, match='road_median_line_color should be an hexadecimal web value as #ffffff, instead : {}'.format(wrong_color_value)):
        configuration._initialize(mock_configuration, configuration_path = 'configuration.json')


def test_initialize_convert_road_median_line_color_from_hexadecimal_to_rgb_tuple_supported_by_cv2():
    road_median_line_color = '#ffffff'
    mock_configuration = {
        'version' : '2019/02/23',
        'road_median_line_color': road_median_line_color
    }

    c = configuration._initialize(mock_configuration, configuration_path = 'configuration.json')
    assert c['road_median_line_color'] == (255, 255, 255)


def test_hex2rgb255_should_convert_hexadecimal_webcolor_into_255_based_rgb_supported_by_cv2():
    color = '#ffffff'

    rgb_color = configuration.hex2rgb255(color)

    assert rgb_color == (255, 255, 255)
