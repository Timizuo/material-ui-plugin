
__version__ = '0.1.0'
from nautobot.extras.plugins import PluginConfig


class MaterialUIPluginConfig(PluginConfig):
    name = "material_ui_plugin"
    verbose_name = "Material UI Plugin"
    version = __version__
    description = "For testing purposes only"
    nautobot_ui="material_ui_plugin_ui"
    base_url = "material-ui-plugin"


config = MaterialUIPluginConfig
