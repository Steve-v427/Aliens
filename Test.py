import unittest

from alien_invasion import AlienInvasion
from settings import Settings
from scoreboard import Scoreboard

class TestSpeedUPSettings(unittest.TestCase):
    def setUp(self):
        self.maxspeedup_scale = Settings()

    def test_speedup_scale(self):
        self.assertNotEqual(self.maxspeedup_scale.speedup_scale, 1.8)
        if True:
            print("Test 1 Sucess!")

class TestShipSetting(unittest.TestCase):
    def setUp(self):
        self.starting_ship_speed = Settings()

    def test_starting_ship_speed(self):
        self.assertNotEqual(self.starting_ship_speed.ship_speed, 6)
        if True:
            print("Test 2 Sucess!")

class TestBulletAmmount(unittest.TestCase):
    def setUp(self):
        self.maxbulletamount = Settings()

    def test_bullet_amount(self):
        self.assertNotEqual(self.maxbulletamount.bullets_allowed, 11)
        if True:
            print("Test 3 Sucess!")

class TestBulletColor(unittest.TestCase):
    def setUp(self):
        self.wrongbulletcolor = Settings()

    def test_bullet_colort(self):
        self.assertNotEqual(self.wrongbulletcolor.bullet_color, (211, 211, 211))
        if True:
            print("Test 4 Sucess!")

class TestNumberofLives(unittest.TestCase):
    def setUp(self):
        self.maxamountoflives = Settings()

    def test_bullet_colort(self):
        self.assertNotEqual(self.maxamountoflives.ship_limit, 4)
        if True:
            print("Test 5 Sucess!")

if __name__ == '__main__':
    unittest.main()