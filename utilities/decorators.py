from functools import wraps
from datetime import datetime

# Usage
# @execution_timer()
def execution_timer():
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            time_start = datetime.now()
            print "Function {0} start at {1}".format(f.__name__, time_start)
            result_wapped = f(*args, **kwargs)
            time_end = datetime.now()
            time_spend = time_end - time_start
            print "Function {0} ended at {1}, spend time {2}".format(f.__name__, time_end, time_spend)
            return result_wapped
        return wrapped
    return wrapper


# decorator demo 1
# @log cause log(func)
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

# The decorator need parameter
# @log('text') cause log('text')(func)
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator