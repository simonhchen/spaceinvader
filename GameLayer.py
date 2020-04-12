import cocos.layer
import cocos.collision_model as cm

import PlayerCannon

class GameLayer(cocos.layer.Layer):
    is is_event_handler = True

    def on_key_press(self, k, _):
        PlayerCannon.KEYS_PRESSED[k] = 1

    def on_key_release(self, k, _):
        PlayerCannon.KEYS_PRESSED[k] = 0

    def __init__(self):
        super(GameLayer, self).__init__()
        w, h = cocos.director.director.get_window_size()
        self.width = w
        self.height = h
        self.lives= 3
        self.score = 0
        self.update_score()
        self.create_player()
        self.create_alien_group(100, 300)
        cell = 1.25 * 50
        self.collman= cm.CollisionManagerGrid(0, w , 0, h,
                                              cell, cell)
        self.schedule(self.update)

    def create_player(self):
        self.player = PlayerCannon(self.width * 0.5, 50)
        self.add(self.player)

    def update_score(self, score=0):
        self.score += score

    def create_alien_group(self, x, y):
        pass

    def update(self, dt):
        self.collman.clear()
        for _, node in self.children:
            self.collman.add(node)
            if not self.collman.knows(node):
                self.remove(node)
        for _, node in self.children:
            node.update(dt)

    def collide(self, node):
        if node is not None:
            for other in self.collman.iter_colliding(node):
                node.collide(other)
                return True
        return False

if __name__ == '__main__':
    cocos.director.director.init(captions="Space Invaders",
                                 width=800, height=650)
    game_layer = GameLayer()
    main_scene = cocos.scene.Scene(game_layer)
    cocos.director.director.run(main_scene)
