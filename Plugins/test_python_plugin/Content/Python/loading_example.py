import unreal
import time

total_frames = 100
text_label = "doing work"

with unreal.ScopedSlowTask(total_frames, text_label) as slow_task:
    slow_task.make_dialog(True)
    for i in range(100):
        if slow_task.should_cancel():
            break
        slow_task.enter_progress_frame(1)
        time.sleep(0.1)


