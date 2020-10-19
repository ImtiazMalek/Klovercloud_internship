# The problem has been solve in python as I am good at this....
#please call this Solution.solution(A, x)
#here A is a list and x is an Integer value
def solution(A,x):
    verify_a = list()
    new_a = list()

    for i in range(x):
        new_a.append(i+1)
    total = sum(new_a)

    for i in range(len(A)):
        if A[i] not in verify_a and A[i] <= x:
            verify_a.append(A[i])
            if sum(verify_a) == total:
                return i
            else:
                continue
