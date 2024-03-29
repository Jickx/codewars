def queue_time(customers, n):
    if not customers:
        return 0
    if n >= len(customers):
        return max(customers)
    tills = [i for i in customers[:n]]

    for customer in customers[n:]:
        for i in range(n):
            if tills[i] == min(tills):
                tills[i] += customer
                break
    return max(tills)


print(queue_time([10, 2, 3, 3], 2))  # 10
print(queue_time([5, 3, 4], 1))  # 12
print(queue_time([2, 2, 3, 3, 4, 4], 2))  # 9
