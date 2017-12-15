from time import sleep
from functools import wraps
import logging

logging.basicConfig()
log = logging.getLogger('retry')


def retry(f):
    @wraps(f)
    def wrap_f(*args, **kargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                return f(*args, **kargs)
            except:
                log.exception("Attempt %s/%s failed : %s", attempt, MAX_ATTEMPTS, (args, kargs))
                sleep(10 * attempt)
        log.critical("All %s attempts failed : %s", MAX_ATTEMPTS, (args, kargs))
    return wrap_f


counter = 0


@retry
def save_to_database(arg):
    print('Write to a database or make a network call or etc.')
    print('This will be automatically retried if exception is thrown.')

    global counter
    counter += 1

    if counter < 2:
        raise ValueError(arg)


if __name__ == '__main__':
    save_to_database('Some bad value')
