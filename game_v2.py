"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def predict(number: int = 1) -> int:
    
    """Угадываем число по алгоритму

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    def next_guess(previous_guess: int,  count: int, less_than: bool) -> int:
        
        """Предполагаем следующее число. Для этого прибавляем или вычитаем 
        из последней догадки шаг, зависящий от числа сделанных попыток.

        Args:
            number (int): Предыдущая догадка
            count (int): Число совершенных попыток
            less_than (bool): Была ли предыдущая догадка меньше искомого числа

        Returns:
            int: Следующая догадка
        """
        #Вычисляем шаг, который уменьшается с каждой сделанной попыткой
        step = np.maximum(round(50 / 2 ** (count - 1)), 1)
        return previous_guess - step if less_than else previous_guess + step
            
    count = 0
    less_than = True
    predict_number = 100

    while True:
        count += 1
        predict_number = next_guess(predict_number, count, less_than)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла, если угадали
        else:
            less_than = number < predict_number #определяем, меньше ли предположенное число искомого
    return count


def score_game(predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(predict)
