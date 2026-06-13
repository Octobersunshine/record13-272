import sys
from prime_utils import analyze_number, is_prime, get_factors, prime_factors


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


def interactive_mode():
    print("=== 素数判断与因数分解服务 ===")
    print("输入正整数进行分析，输入 'q' 退出\n")
    while True:
        try:
            user_input = input("请输入一个正整数: ").strip()
            if user_input.lower() in ('q', 'quit', 'exit'):
                print("再见！")
                break
            if not user_input:
                continue
            n = int(user_input)
            print_analysis(n)
        except ValueError:
            print("错误: 请输入有效的正整数")
        except KeyboardInterrupt:
            print("\n再见！")
            break


def main():
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            try:
                n = int(arg)
                print_analysis(n)
            except ValueError:
                print(f"错误: '{arg}' 不是有效的整数")
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
