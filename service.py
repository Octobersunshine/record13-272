import sys
from prime_utils import analyze_number, is_prime, get_factors, prime_factors, sieve_primes


def print_analysis(n):
    try:
        result = analyze_number(n)
        print(f"\n数字: {result['number']}")
        print(f"是否为素数: {'是' if result['is_prime'] else '否'}")
        print(f"所有因数: {result['factors']}")
        if result['prime_factors']:
            print(f"素因数分解: {' × '.join(map(str, result['prime_factors']))}")
    except (TypeError, ValueError) as e:
        print(f"错误: {e}")


def print_prime_range(start, end):
    try:
        primes = sieve_primes(start, end)
        print(f"\n范围 [{start}, {end}] 内的素数:")
        print(f"共 {len(primes)} 个素数")
        if len(primes) <= 100:
            print(primes)
        else:
            print(f"前50个: {primes[:50]}")
            print(f"后50个: {primes[-50:]}")
    except (TypeError, ValueError) as e:
        print(f"错误: {e}")


def interactive_mode():
    print("=== 素数判断与因数分解服务 ===")
    print("输入正整数进行分析")
    print("输入 'r 起始值 结束值' 生成范围内素数列表")
    print("输入 'q' 退出\n")
    while True:
        try:
            user_input = input("请输入: ").strip()
            if user_input.lower() in ('q', 'quit', 'exit'):
                print("再见！")
                break
            if not user_input:
                continue
            if user_input.lower().startswith('r '):
                parts = user_input.split()
                if len(parts) != 3:
                    print("错误: 格式为 'r 起始值 结束值'")
                    continue
                start = int(parts[1])
                end = int(parts[2])
                print_prime_range(start, end)
            else:
                n = int(user_input)
                print_analysis(n)
        except ValueError:
            print("错误: 请输入有效的正整数")
        except KeyboardInterrupt:
            print("\n再见！")
            break


def main():
    args = sys.argv[1:]
    if not args:
        interactive_mode()
    elif '--range' in args:
        idx = args.index('--range')
        if idx + 2 < len(args):
            try:
                start = int(args[idx + 1])
                end = int(args[idx + 2])
                print_prime_range(start, end)
            except ValueError:
                print("错误: --range 后需要两个整数参数")
        else:
            print("错误: --range 需要两个参数: --range 起始值 结束值")
    else:
        for arg in args:
            try:
                n = int(arg)
                print_analysis(n)
            except ValueError:
                print(f"错误: '{arg}' 不是有效的整数")


if __name__ == "__main__":
    main()
