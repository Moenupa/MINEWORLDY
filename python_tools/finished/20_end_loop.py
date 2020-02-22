loop_text = input('text for 20-end-loop: _\b')

def _20endloop(loop_text):
    count = 0
    if not loop_text:
        loop_text = "Message being repeated for 20 times."
    while count < 20:
        print(loop_text)
        count += 1

_20endloop(loop_text)