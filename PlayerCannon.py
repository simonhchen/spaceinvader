from collections import defaultdict
from pyglet.window import key

class PlayerCannon(Actor):
    KEYS_PRESSED = defaultdict(int)

    def __init__(self, x, y):
        super(PlayerCannon, self).__init__('img/cannon.png', x, y)
        self.speed = eu.Vector2(200, 0)

    def update(self, elapsed):
        pressed = PlayerCannon.KEYS_PRESSED
        movement = pressed[key.RIGHT] - pressed[key.LEFT]
        w = self.width * 0.5
        if movement != 0 and w <= self.x <= self.parent.width - w:
            self.move(self.speed * movement * elapsed)

    def collide(self, other):
        other.kill()
        self.kill()