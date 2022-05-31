import os.path


class GameStats:
    """Отслеживание статистики дял игры Alien Invasion."""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False

        # Рекорд не должен сбрасываться.
        self.high_score = 0
        self._set_high_score()

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _set_high_score(self):
        """Устанавливаем максимальный результат из файла."""
        if os.path.exists('high_score.txt'):
            with open("high_score.txt") as f:
                for line in f:
                    self.high_score = int(line)
