from trainer.threads.gui_thread import GUIThread
from trainer.threads.music_thread import MusicThread


def main():
    gui_thread = GUIThread()
    music_thread = MusicThread()

    music_thread.start()
    gui_thread.start()

    gui_thread.join()
    music_thread.join()


if __name__ == "__main__":
    main()
