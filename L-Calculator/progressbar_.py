"""Loading Progressbar"""
from time import sleep

from colorama import Fore


def bar(iteration, total, prefix='', suffix='', decimals=1,
        length=100, fill='/', printend="", data=False):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length: int = int(length * iteration // total)
    bar_str: str = Fore.GREEN + (fill * filled_length) + (Fore.WHITE + ' ' * (length - filled_length))
    if not data:
        print(f'\r{prefix} |{bar_str}| {percent}% {suffix}', end=printend)
    else:
        print(f'\r{prefix} |{bar_str}| {percent}% {round(iteration / 0.80, 1):<4}'
              f'/{round(total / 0.80, 1):<4}KB',
              end=printend)
    # Print New Line on Complete
    if iteration == total:
        print()


def selfbar(wait):
    """

    :param wait:
    """
    var: str = ''
    char: str = "#"
    for i in range(20):
        var += char
        print(f"\r|{var:-<20}|"
              f"{round(len(var) / 20, 2) * 100}% {round(len(var) / 0.80, 2)}"
              f" KB           ", end="")
        sleep(wait)
