from caproto import ChannelData, ChannelType
from caproto.server import AsyncLibraryLayer, PVGroup, pvproperty


class {{cookiecutter.import_name.capitalize()}}(PVGroup):
    """
    {{ cookiecutter.description }}.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Init here

    sample = pvproperty(
        value=0.0,
        name='SampleValue',
        record='ai',
        lower_ctrl_limit=0.0,
        lower_alarm_limit=0.1,
        upper_alarm_limit=0.9,
        upper_ctrl_limit=1.0,
        read_only=False,
        doc='Sample value for the cookiecutter',
        precision=3,
    )

    @sample.startup
    async def sample(self,
                     instance: ChannelData,
                     async_lib: AsyncLibraryLayer):
        """
        Startup hook for sample.
        """
        print('This happens at IOC boot!')
        print(f'Initial value was: {instance.value}')
        await instance.write(value=0.1, verify_value=False)
        print(f'Now it is: {instance.value}')

    @sample.putter
    async def sample(self, instance: ChannelData, value: float):
        """Data was written over channel access."""
        if value >= 0.9:
            raise ValueError('Invalid value')

        print(f'They wrote: {value}, but {value/2} is better')
        value /= 2.0
        return value

    scanned = pvproperty(
        value=0.0,
        name='SampleScanned',
        record='mbbi',
        read_only=True,
        doc='Scanned enum',
        enum_strings=['One', 'Two', 'Three'],
        dtype=ChannelType.ENUM,
    )

    @scanned.scan(period=1.0, stop_on_error=False, use_scan_field=True)
    async def scanned(self, instance: ChannelData, async_lib: AsyncLibraryLayer):
        """
        Scan hook for scanned.

        This updates at a rate of 1Hz, unless the user changes .SCAN.
        """
        await self.scanned.write(value=(self.scanned.value + 1) % 3)
