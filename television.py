class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        self.__status = self.__status == False


    def mute(self):
        if not self.__status:
            return
        self.__muted = self.__muted == False


    def channel_up(self):
        self.__channel = self.__set_channel(self.__channel + 1)


    def channel_down(self):
        self.__channel = self.__set_channel(self.__channel - 1)


    def __set_channel(self, channel):
        if not self.__status:
            return self.__channel
        if channel < Television.MIN_CHANNEL:
            channel = Television.MAX_CHANNEL
        if channel > Television.MAX_CHANNEL:
             channel = Television.MIN_CHANNEL
        return channel

    def volume_up(self):
        self.__muted = False
        self.__volume = self.__set_volume(self.__volume + 1)


    def volume_down(self):
        self.__muted = False
        self.__volume = self.__set_volume(self.__volume - 1)

    def __set_volume(self, volume):
        if not self.__status:
            return self.__volume
        if volume < Television.MIN_VOLUME:
            volume = Television.MIN_VOLUME
        if volume > Television.MAX_VOLUME:
            volume = Television.MAX_VOLUME
        return volume


    def __str__(self):
        current_volume = self.__volume
        if self.__muted:
            current_volume = Television.MIN_VOLUME
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {current_volume}"