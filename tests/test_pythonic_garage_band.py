from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Band, Guitarist, Drummer, Bassist


def test_version():
    assert __version__=='0.1.0'

sam1=Guitarist("sam1") 
sam2=Drummer("sam2")
sam3=Bassist("sam3")    
samBand=Band("samBand")

samBand.insert(sam1)
samBand.insert(sam2)
samBand.insert(sam3)

def test_to_list():
    expected = [sam1,sam2,sam3]
    actual = samBand.to_list()
    assert  actual == expected

def test_play_solo():
    expected="sam2"
    actual=sam2.play_solo()
    assert actual==expected

def test_play_solos():
    expected="sam1\nsam2\nsam3\n"
    actual=samBand.play_solos()
    assert actual==expected

def test_str():
    expected="Guitarist--->sam1"
    actual=sam1.__str__()
    assert actual==expected

def test_rper():
    expected="sam3"
    actual=sam3.__repr__()
    assert actual==expected
    
def test_get_instrument():
    expected="Drummer"
    actual=sam2.get_instrument()
    assert actual==expected