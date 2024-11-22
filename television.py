class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """Turns the television either on or off depending on its current status"""
        self.__status = self.__status == False


    def mute(self) -> None:
        """Mutes or disables mute the television if it is on"""
        if not self.__status:
            return
        self.__muted = self.__muted == False


    def channel_up(self) -> None:
        """Increases channel by one if the television is on. If the channel goes above
        the max channel the channel will be set back to the minimum channel"""
        self.__channel = self.__set_channel(self.__channel + 1)


    def channel_down(self) -> None:
        """Decreases channel by one if the television is on. If the channel goes below
        the minimum channel the channel will be set back to the maximum channel"""
        self.__channel = self.__set_channel(self.__channel - 1)


    def __set_channel(self, channel:int) -> int:
        """Returns channel based on passed in desired channel if the television is on.
        If the channel goes above the maximum it will be set to the minimum,
        and if it goes below the minimum it will be set to the maximum"""
        if not self.__status:
            return self.__channel
        if channel < Television.MIN_CHANNEL:
            channel = Television.MAX_CHANNEL
        if channel > Television.MAX_CHANNEL:
             channel = Television.MIN_CHANNEL
        return channel

    def volume_up(self) -> None:
        """Increases the volume by one if the television is on. If the television is muted,
         disable mute. If the volume passes the max volume set the volume to max volume"""
        self.__volume = self.__set_volume(self.__volume + 1)


    def volume_down(self) -> None:
        """Decreases the volume by one if the television is on. If the television is muted,
        disable mute. If the volume passes the min volume set the volume to min volume"""
        self.__volume = self.__set_volume(self.__volume - 1)

    def __set_volume(self, volume:int) -> int:
        """Returns volume based on passed in desired volume if the television is on.
        If the television is muted, disable mute. If the volume passes maximum volume return
        the maximum volume. If the volume passes the minimum volume return the minimum volume"""
        if not self.__status:
            return self.__volume
        self.__muted = False
        if volume < Television.MIN_VOLUME:
            volume = Television.MIN_VOLUME
        if volume > Television.MAX_VOLUME:
            volume = Television.MAX_VOLUME
        return volume


    def __str__(self) -> str:
        """Returns representation of the television by its status, channel, and
         volume. If the television is muted volume will be the minimum volume"""
        current_volume = self.__volume
        if self.__muted:
            current_volume = Television.MIN_VOLUME
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {current_volume}"