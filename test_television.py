import pytest
from television import *

class Test:

    def setup_method(self):
        self.television = Television()


    def teardown_method(self):
        del self.television


    def test_init(self):
        assert self.television.__str__() == 'Power = False, Channel = 0, Volume = 0'


    def test_power(self):
        self.television.power()
        assert self.television.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.television.power()
        assert self.television.__str__() == 'Power = False, Channel = 0, Volume = 0'


    def test_mute(self):
        self.television.power()
        self.television.volume_up()
        self.television.mute()
        assert self.television.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.television.mute()
        assert self.television.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.television.mute()
        self.television.power()
        assert self.television.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.television.mute()
        assert self.television.__str__() == 'Power = False, Channel = 0, Volume = 0'


    def test_channel_up(self):
        self.television.channel_up()
        assert self.television.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.television.power()
        self.television.channel_up()
        assert self.television.__str__() == 'Power = True, Channel = 1, Volume = 0'

        self.television.channel_up()
        self.television.channel_up()
        self.television.channel_up()
        assert self.television.__str__() == 'Power = True, Channel = 0, Volume = 0'


    def test_channel_down(self):
        self.television.channel_down()
        assert self.television.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.television.power()
        self.television.channel_down()
        assert self.television.__str__() == 'Power = True, Channel = 3, Volume = 0'


    def test_volume_up(self):
        self.television.volume_up()
        assert self.television.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.television.power()
        self.television.volume_up()
        assert self.television.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.television.mute()
        self.television.volume_up()
        assert self.television.__str__() == 'Power = True, Channel = 0, Volume = 2'

        self.television.volume_up()
        assert self.television.__str__() == 'Power = True, Channel = 0, Volume = 2'


    def test_volume_down(self):
        self.television.volume_down()
        assert self.television.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.television.power()
        self.television.volume_up()
        self.television.volume_up()
        self.television.volume_down()
        assert self.television.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.television.mute()
        self.television.volume_down()
        assert self.television.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.television.volume_down()
        assert self.television.__str__() == 'Power = True, Channel = 0, Volume = 0'