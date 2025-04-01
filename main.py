from web_backend import web
import multiprocessing
import time
from random import randint, uniform

if __name__ == '__main__':
    multiprocessing.freeze_support()
    
    manager = multiprocessing.Manager()
    button_flags = manager.dict()
    marks = manager.list() 


def main(button_flags, marks):
    while True:
        while not button_flags["start"]:
            pass
        for i in range(len(marks)):
            marks.pop()
        marks.append([0, 0, 1, 1])
        marks.append([1, 1, 1, 2])
        marks.append([1, 2, 3, 5])
        while button_flags["start"]:
            time.sleep(1)


if __name__ == '__main__':    
    button_flags["start"] = False
    button_flags["stop"] = True
    button_flags["pause"] = False
    button_flags["killswitch"] = False

    main_thread = multiprocessing.Process(target=main, args=(button_flags, marks))
    main_thread.start()

    try:
        web.button_flags = button_flags
        web.marks = marks
        web.app.run(host='127.0.0.1', port=5000, debug=True)
    except Exception as e:
        print(f'error: {e}')
    finally:
        main_thread.terminate()
        main_thread.join()
