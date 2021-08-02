import json
import pytest
#import yaml
from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Band, Musician, Guitarist, Drummer, Bassist


def test_version():
    assert __version__=='0.1.0'

def test_guitarist_str():
    sam1 = Guitarist("sam1")
    actual = str(sam1)
    expected = "Guitarist--->sam1"
    assert actual == expected


def test_guitarist_repr():
    sam1 = Guitarist("sam1")
    actual = repr(sam1)
    expected = "{self.name}"
    assert actual == expected


def test_Drummer_repr():
    sam2 = Drummer("sam2")
    actual = str(sam2)
    expected = "Drummer--->sam2"
    assert actual == expected


def test_drummer_repr():
    sam2 = Drummer("sam2")
    actual = repr(sam2)
    expected = "sam2"
    assert actual == expected


def test_bassist_str():
    sam3 = Bassist("sam3")
    actual = str(sam3)
    expected = "Bassist--->sam3"
    assert actual == expected


def test_bassist_repr():
    sam3 = Bassist("sam3")
    actual = repr(sam3)
    expected = "sam3"
    assert actual == expected


def test_band_name():
    samBand = Band("samBand")

    assert samBand.name == "samBand"


def test_guitarist():
    jimi = Guitarist("sam1")
    assert jimi.name == "sam1"
    assert jimi.get_instrument() == "Guitarist"


def test_bassist():
    sam3 = Bassist("sam3")
    assert sam3.name == "sam3"
    assert sam3.get_instrument() == "Bassist"


def test_drummer():
    sam2 = Drummer("sam2 Baker")
    assert sam2.name == "sam2 Baker"
    assert sam2.get_instrument() == "Drummer"


def test_instruments(one_band):
    instruments = ["guitar", "bass", "drums"]
    for i, member in enumerate(one_band.members):
        # NOTE: see stretch goal where zip used
        assert member.get_instrument() == instruments[i]


def test_individual_solos(one_band):
    for member in one_band.members:
        if member.get_instrument() == "guitar":
            assert member.play_solo() == "face melting guitar solo"
        elif member.get_instrument() == "bass":
            assert member.play_solo() == "bom bom buh bom"
        elif member.get_instrument() == "drums":
            assert member.play_solo() == "rattle boom crash"


def test_band_members(one_band):

    assert len(one_band.members) == 3

    assert isinstance(one_band.members[0], Musician)
    assert isinstance(one_band.members[0], Guitarist)
    assert one_band.members[0].name == "sam1"

    assert isinstance(one_band.members[1], Musician)
    assert isinstance(one_band.members[1], Bassist)
    assert one_band.members[1].name == "sam3"

    assert isinstance(one_band.members[2], Musician)
    assert isinstance(one_band.members[2], Drummer)
    assert one_band.members[2].name == "sam2"


def test_play_solos_for_whole_band(one_band):
    solos = one_band.play_solos()
    assert len(solos) == 3
    assert solos[0] == "face melting guitar solo"
    assert solos[1] == "bom bom buh bom"
    assert solos[2] == "rattle boom crash"


def test_to_list():
    assert Band.to_list() == []
    Band("", [])
    assert len(Band.to_list()) == 1


#######################
# Fixtures
#######################


@pytest.fixture
def samBand_data():
    return {
        "name": "samBand",
        "members": [
            {"name": "sam1", "instrument": "Guitar"},
            {"name": "sam3", "instrument": "Bass"},
            {"name": "sam2", "instrument": "Drums"},
        ],
    }


@pytest.fixture
def one_band():
    some_band = Band(
        "samBand", 
        [Guitarist("sam1"), Bassist("sam3"), Drummer("sam2"),]
        )
    return some_band


@pytest.fixture(autouse=True)
def clean():
    """runs before each test automatically
    There's also a more advanced way to run code after each test as well
    Check the docs for that. Hint: it uses yield
    """
    Band.instances = []


#######################
# Stretch
#######################


@pytest.mark.skip("stretch")
def test_from_file():
    with open("") as f:
        bands = json.loads(f.read())

    assert len(bands) == 1

    samBand_data = bands[0]

    samBand = Band(samBand_data["name"], samBand_data["members"])

    assert samBand.name == "samBand"


@pytest.mark.skip("stretch")
def test_from_json():
    bands = json.safe_load(open(""))

    assert bands[0]["name"] == "samBand"

    assert bands[1]["name"] == "The Pixies"


@pytest.mark.skip("stretch")
def test_abstract_musician():
    with pytest.raises(TypeError):
        unacceptably_vague_musician = Musician()