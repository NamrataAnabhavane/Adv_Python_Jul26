import time

def download_file(url):
    print(f"Satrting download from {url}")
    time.sleep(2)

    return f"Downloaded: {url}"

def claculate_prime(n):
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count +=1

        num +=1

    return num - 1

if __name__ == "__main__":
    result_dounloaded = download_file("https://emample.com/file")
    print(result_dounloaded)

    nth = 1000
    print(f"calculating {nth}th prime...")
    prime_result = claculate_prime(nth)
    print(f" {nth}th prime is: {prime_result}")