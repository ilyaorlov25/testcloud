def merge_sort(input_list):
    if len(input_list) == 1 or len(input_list) == 0:
        return input_list
    left = merge_sort(input_list[:len(input_list) // 2])
    right = merge_sort(input_list[len(input_list) // 2:])
    n = m = k = 0
    c = [0] * len(input_list)
    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            c[k] = left[n]
            n += 1
        else:
            c[k] = right[m]
            m += 1
        k += 1
    while n < len(left):
        c[k] = left[n]
        n += 1
        k += 1
    while m < len(right):
        c[k] = right[m]
        m += 1
        k += 1
    for i in range(len(input_list)):
        input_list[i] = c[i]
    return input_list


if __name__ == '__main__':
    input_line = input().split(' ')
    numbers = [int(el) for el in input_line]
    min_num = numbers[0]
    max_num = min_num
    evens = []
    for number in numbers:
        if number > max_num:
            max_num = number
        if number < min_num:
            min_num = number
        if number % 2 == 0:
            evens.append(number)
    print(f'Min mum: {min_num}')
    print(f'Max mum: {max_num}')
    print(f'Even mums: {evens}')
    print(f'Sorted: {merge_sort(numbers)}')
