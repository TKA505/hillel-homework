input_data = input("Введите числа через пробел: ")

numbers = list(map(int, input_data.split()))

max_value = max(numbers)

max_index = numbers.index(max_value)

print(f"Наибольший элемент: {max_value} Номер индекса: {max_index}")