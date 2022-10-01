def timestamp_to_string(seconds: int | float):
    rest = 0
    if isinstance(seconds, float):
        base = int(seconds)
        rest = round((seconds - base) * 10**7)
        seconds = base

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    hours %= 24
    return f"{hours:02}:{minutes:02}:{seconds:02}{f':{rest:07}' if rest else ''} {'pm' if hours > 12 else 'am'}"

if __name__ == "__main__":
    import time
    from utils import get_number

    own = input("Own timestamp? [y|n]: ")
    if own == "y":
        timestamp = get_number("the timestamp")
    else:
        timestamp = time.time()

    res = timestamp_to_string(timestamp)
    print(res)
