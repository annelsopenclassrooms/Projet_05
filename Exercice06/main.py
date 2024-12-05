import statistics

def calculate_average(numbers):
    average = statistics.mean(numbers)

    return(average)

if __name__ == '__main__':

    numbers = [10, 20, 30, 40, 50]
    average = calculate_average(numbers)
    print("La moyenne est :", average)