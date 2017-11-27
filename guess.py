from random import randint


def guess(nmin=1, nmax=100, debug=False, sim_list=[]):
    """
    Have user guess a number from nmin to nmax
    :param nmin: minimum number
    :param nmax: max number
    :param debug: debug option to show the number
    :param sim_list: List to simulate
    :return: number of guesses
    """
    number = randint(nmin, nmax)
    if debug:
        print('The number is {}'.format(number))
    if sim_list:
        return simulate_guess(number, sim_list, nmin, nmax)
    else:
        return guess_until_user(number, nmin, nmax)


def guess_until_user(number, nmin=1, nmax=100):
    """
    Guess with user input
    :param number: Number that was picked
    :param nmin: min number
    :param nmax: max number
    :return: number of tries
    """
    guesses = 0
    attempt = number - 1
    while attempt != number:
        attempt = int(input("Guess a number from {} to {}: ".format(nmin, nmax)))
        if attempt > number:
            print('Too high!')
        if attempt < number:
            print('Too low!')
        guesses += 1
    return guesses


def simulate_guess(number, attempts, nmin=1, nmax=100):
    """
    Simulate user guesses
    :param number: target number
    :param attempts: attempts to make in a list format (Number gets appended)
    :param nmin: minimum number
    :param nmax: max number
    :return: number of tries
    """
    guesses = 0
    attempts += [number]
    for attempt in attempts:
        print("Guess a number from {} to {}: {}".format(nmin, nmax, attempt))
        if attempt > number:
            print('Too high!')
        if attempt < number:
            print('Too low!')
        guesses += 1
    if guesses == 1:
        print('You took 1 try')
    else:
        print('You took {} tries'.format(guesses))
    return guesses

if __name__ == '__main__':
    print('Time to play a guessing game!')
    tries = guess()
    if tries == 1:
        print('You took 1 try')
    else:
        print('You took {} tries'.format(tries))
