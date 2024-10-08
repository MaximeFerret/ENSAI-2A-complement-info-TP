from business_object.pokemon.all_rounder import AllRounder
from business_object.statistic import Statistic


class TestAllRounder:
    def test_get_coef_damage_type(self):
        # GIVEN
        snorlax = AllRounder(stat_current=Statistic(sp_atk=100, sp_def=100))

        # WHEN
        multiplier = snorlax.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 2


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
