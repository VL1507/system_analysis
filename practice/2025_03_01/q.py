def P_up_n(p: float, m: float, n: float) -> float:
    return 1 - (1 - p**m) ** n


def n_up_star(m: int, delta: float, p: float) -> float:
    return min(n for n in range(1, 500) if P_up_n(p, m, n) >= 1 - delta)


def P_down_n(p: float, m: float, n: float) -> float:
    return (1 - (1 - p) ** n) ** m


def n_down_star(m: int, delta: float, p: float) -> float:
    return min(n for n in range(1, 500) if P_down_n(p, m, n) >= 1 - delta)


def get_all(m_start: int, m_end: int, delta: float, p: float, func) -> list[float]:
    return [func(m, delta, p) for m in range(m_start, m_end + 1)]


def main():
    delta = 0.1
    p = 0.7
    m_start = 1
    m_end = 15

    all_n_up_star = get_all(m_start, m_end, delta, p, n_up_star)
    print("n_up_star", all_n_up_star)

    all_n_down_star = get_all(m_start, m_end, delta, p, n_down_star)
    print("n_down_star", all_n_down_star)


if __name__ == "__main__":
    main()
