import time
from threading import Thread

from requests import post


def apply_load(url, requested_rps=1, body='"""""""""""""""""lelelele"""""""""""""@yandex.ru'):
    def _apply_load(url, rps=1, body='lelelelele'):
        try:
            request_ts = time.monotonic()
            while True:
                _ = post(url, json={'body': body})
                request_ts += (1 / rps)  # Works o
                now = time.monotonic()
                if now < request_ts:
                    time.sleep(request_ts - now)
        except KeyboardInterrupt:
            exit(1)

    threads = []
    for _ in range(requested_rps):
        thread = Thread(target=_apply_load, args=(url, 1, body))
        thread.start()
        threads.append(thread)


if __name__ == '__main__':
    apply_load(
        'http://localhost:4567/send',
        requested_rps=2,
        body='"""""""""""""""""lelelele"""""""""""""@yandex.ru'
    )
