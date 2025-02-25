import unreal

class MyClass(object):
    def __init__(self) -> None:
        self.frame_count = 0
        self.max_count = 1000
    
    def start(self) -> None:
        self.slate_post_tick_handle = unreal.register_slate_post_tick_callback(self.tick)
        self.frame_count = 0

    def tick(self, delta_time: float) -> None:
        print(self.frame_count)
        self.frame_count += 1
        if self.frame_count >= self.max_count:
            unreal.unregister_slate_post_tick_callback(self.slate_post_tick_handle)

test = MyClass()
test.start()