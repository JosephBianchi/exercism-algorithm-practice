def distance(strand_a, strand_b):
    total = 0
    strand_a = strand_a.upper()
    for j in range(len(strand_a)):
        if strand_a[j] != strand_b[j]:
            total += 1
    return total
