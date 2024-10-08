from business_object.pokemon.defender import Defender
from business_object.statistic import Statistic


class TestDefender:
    def test_get_coef_damage_type(self):
        # GIVEN
        snorlax = Defender(stat_current=Statistic(attack=100, defense=100))

        # WHEN
        multiplier = snorlax.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 2


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
