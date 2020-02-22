text = input('text for 20-end-loop:\n')
def _20endloop(loop_text):
    count = 0
    while count < 20:
        print(loop_text)
        count += 1
if text == '':
    del text
try:
    _20endloop(text)
except:
    _20endloop('this is the message that will repeat itself for 20 times.')
