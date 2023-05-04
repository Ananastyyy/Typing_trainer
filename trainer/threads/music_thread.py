import threading

from PyQt5.QtCore import QUrl, pyqtSignal
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent

from config.conf_parser import ConfParser


class MusicThread(threading.Thread):
    finished = pyqtSignal()

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.player = QMediaPlayer()
        config = ConfParser()
        self.constants = config.music_thread

    def start(self, **kwargs):
        playlist = QMediaPlaylist(self.player)
        media = QMediaContent(
            QUrl.fromLocalFile(self.constants["path_to_music"]))
        playlist.addMedia(media)
        playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.player.setPlaylist(playlist)
        self.player.play()
