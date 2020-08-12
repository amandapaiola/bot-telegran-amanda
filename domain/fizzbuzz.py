def fizz_buzz(number):
    """
    Função do FizzBuzz.
    Números diviziveis por 3 retorna fizz
    Números diviziveis por 5 retorna buzz
    Números diviziveis pos ambos (3 e 5) retorna fizz-buzz
    :param number: número para o teste
    :return:
    """
    """
    :param number: Número que será testado se é divisor de 3, 5 ou dos dois.
    :return: Fizz, Buzz ou FizzBuzz
    """
    if number % 5 == 0 and number % 3 == 0:
        return 'fizz-buzz'
    elif number % 3 == 0:
        return 'fizz'
    elif number % 5 == 0:
        return 'buzz'
    else:
        return number
