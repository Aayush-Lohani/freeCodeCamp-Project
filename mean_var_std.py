import numpy as np

numbers = []
print("Print Nine Numbers one by one.")

for i in range(9):
    number = float(input(f"Enter No.{i+1}:  "))
    numbers.append(number)


print(numbers)


def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError(" List must contain nine numbers.")

    arr = np.array(numbers).reshape(3, 3)

    calculations = {
        'mean': [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.mean().tolist()],
        'variance': [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.var().tolist()],
        'standard deviation': [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr.std().tolist()],
        'max': [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.max().tolist()],
        'min': [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.min().tolist()],
        'sum': [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.sum().tolist()]
    }

    return calculations


result = calculate(numbers)
print(result)