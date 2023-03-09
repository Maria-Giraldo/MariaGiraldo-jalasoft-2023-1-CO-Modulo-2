from dino_runner.components.power_ups.powe_up import PowerUp
from dino_runner.utils.constants import FIRE_TYPE, FIRE


class Fire(PowerUp):
    def __init__(self):
        super().__init__(FIRE, FIRE_TYPE)