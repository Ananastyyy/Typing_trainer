import configparser


class ConfParser:
    def __init__(self):
        self._add_parse_conf_file();

    def _add_parse_conf_file(self):
        self.window = self._init_config_file("config/window.ini", "WINDOW")
        self.login_dialog = self._init_config_file("config/dialogs.ini",
                                                   "LOGIN_DIALOG")
        self.statistic_dialog = self._init_config_file("config/dialogs.ini",
                                                       "STATISTICS_DIALOG")
        self.database_handler = self._init_config_file("config/logic.ini",
                                                       "DATABASE_HANDLER")
        self.line_handler = self._init_config_file("config/logic.ini",
                                                   "LINE_HANDLER")
        self.music_thread = self._init_config_file("config/threads.ini",
                                                   "MUSIC_THREAD")

    def _init_config_file(self, name_file: str, name_items: str) -> dict:
        config = configparser.ConfigParser()
        config.read(name_file, encoding="utf-8")
        constants = dict(config.items(name_items))
        return constants
