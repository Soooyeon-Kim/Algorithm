def factorial(num):
    # 재귀함수를 세울 때는 탈출 조건부터 찾는다.
    if num <= 1:
        return 1

    return factorial(num - 1) * num

def main():
    print(factorial(5)) 
    # return 120

if __name__ == "__main__":
    main()