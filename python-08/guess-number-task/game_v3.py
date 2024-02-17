""" 
Решение.
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low, high = 1, 100  # задаем нижнюю и верхнюю границы диапазона загаданного числа
    
    while True:
        count += 1
        
        if high - low == 1:
            # если верхняя и нижняя границы отличаются на единицу,
            # то новое предсказание выбираем случайно из этих двух чисел
            predict = np.random.choice([low, high]) 
        else:
            # для предсказания выбираем середину диапазона
            predict = low + (high - low) // 2
        
        if number == predict:
            break
        
        if number < predict:
            # если загаданное число меньше предсказания, то сдвигаем верхнюю границу диапазона на текущее предсказание
            high = predict
        else:
            # иначе - сдвигаем нижнюю границу на текущее предсказание
            low = predict
        
    return count
