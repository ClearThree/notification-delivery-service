import time

from requests import post


def apply_load(url, rps=1.0, body='lelelelele'):
    try:
        request_ts = time.monotonic()
        while True:
            _ = post(url, json={'body': body})
            request_ts += (1.0 / rps)
            now = time.monotonic()
            if now < request_ts:
                time.sleep(request_ts - now)
    except KeyboardInterrupt:
        exit(1)


if __name__ == '__main__':
    apply_load(
        'http://localhost:4567/send',
        rps=2,
        body='"""""""""""""""""lelelele"""""""""""""@yandex.ru'
    )
