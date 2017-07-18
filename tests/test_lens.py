############
# Standard #
############

###############
# Third Party #
###############
import pytest
import numpy as np

##########
# Module #
##########

def test_lens_properties(lens):
    assert np.isclose(500.0, lens.radius, atol=0.1)
    assert np.isclose(100.0, lens.z,      atol=0.1)
    assert np.isclose(50.0,  lens.focus,  atol=0.1)

def test_image_from_obj(lens):
    #Real image
    assert np.isclose(lens.image_from_obj(0.0),  200.0, atol=0.1)
    #Imaginary image
    assert np.isclose(lens.image_from_obj(75.0), 50.0, atol=0.1)

def test_lens_connect_effective_radius(array):
    assert np.isclose(array.effective_radius, 250, atol=0.1)

def test_lens_connect_image(array):
    assert np.isclose(array.image(0.0),  312.5,   atol=0.1)
    assert np.isclose(array.image(75.0), 303.125, atol=0.1)
    assert np.isclose(array.image(80.0), 303.409, atol=0.1)
    assert np.isclose(array.image(125.0), 304.6875, atol=0.1)


def test_number_of_lenses(array):
    assert array.nlens()== 2
