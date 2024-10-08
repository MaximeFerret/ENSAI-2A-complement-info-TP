from business_object.pokemon.attacker import Attacker
from business_object.statistic import Statistic


class TestAttacker:
    def test_get_coef_damage_type(self):
        # GIVEN
        snorlax = Attacker(stat_current=Statistic(speed=100, attack=100))

        # WHEN
        multiplier = snorlax.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 2


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
