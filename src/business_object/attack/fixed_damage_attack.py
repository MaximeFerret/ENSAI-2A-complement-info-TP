from business_object.attack.abstract_attack import AbstractAttack


class FixedDamageAttack(AbstractAttack):
    def __init__(self, power=0, name=None, description=None):
        super().__init__(power, name, description)

    def compute_damage(self):
        return self._power
