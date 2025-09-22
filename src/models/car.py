class Car:
    def __init__(self, battery:int = 0, road_size:tuple[int, int] = (0, 0), velocity:float = 5):
        # sprite -> img
        # Velocity -> float
        # battery -> int|float
        # collition_with_obstacle -> bool
        self.velocity = velocity
        self.battery = battery
        self.collition_with_obstacle = False
        self.pos_x = 100
        self.pos_y = road_size[1] // 2

    def run(self):
        # # Todo: SOLID
        # if self.pos_x < screen.get_size()[0] - 200:
        #     # The car never mmove, just is a example!
        #     # Who really move is the road
        #     self.pos_x += self.velocity
        # else:
        #     self.pos_x = 50
        # self.draw(screen)
        # # self._check_colide()
        pass

    def up(self):
        pass

    def down(self):
        pass