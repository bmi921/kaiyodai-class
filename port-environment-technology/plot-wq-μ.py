import matplotlib.pyplot as plt

def plot_waiting_times(arrival_times, wait_times):
    plt.figure(figsize=(10, 6))
    plt.plot(arrival_times, wait_times, 'bo-', label='wait time')
    plt.xlabel('μ * const', fontsize=12)
    plt.ylabel('Waiting time', fontsize=12)
    plt.title('How change waiting time by μ * const ', fontsize=14)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graph.png")
    plt.show()

def wq_formula(l,m,times):
    return l/(m * times * (m*times -l)) 

def main():
    l = 50   # ゲート到着台数
    m = 50.5 # ゲート処理台数　
    
    m_times = [1 + c/10 for c in range(1,6)]
    Wq = [wq_formula(l,m,m_times[i]) * 60 for i in range(0,len(m_times))]
    print(m_times, Wq)

    # グラフ描画
    plot_waiting_times(m_times, Wq)

if __name__ == '__main__':
    main()