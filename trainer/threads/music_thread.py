from PyQt5.QtCore import QThread, QUrl, pyqtSignal
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent


class MusicThread(QThread):
    finished = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.player = QMediaPlayer()

    def start(self):
        playlist = QMediaPlaylist(self.player)
        media = QMediaContent(QUrl.fromLocalFile("resources/music1.mp3"))
        playlist.addMedia(media)
        playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.player.setPlaylist(playlist)
        self.player.play()
