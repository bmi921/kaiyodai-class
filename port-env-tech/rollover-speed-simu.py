import math
import matplotlib.pyplot as plt
import numpy as np

def calculate_rollover_speed(R, g, b, a):
    """
    車両の横転限界速度を計算する関数。

    Args:
        R (float): カーブ半径 (m)
        g (float): 重力加速度 (m/s^2)
        b (float): 重心高さ (m)
        a (float): トレッドの半分または重心から横転軸までの水平距離 (m)

    Returns:
        float: 横転限界速度 (m/s)
    """
    if R < 0 or g < 0 or b < 0 or a <= 0:
        raise ValueError("入力値は正である必要があります (aは0でないこと)。")
    return math.sqrt(R * g * b / a)

# 定数
G = 9.81  # 重力加速度 (m/s^2)
B = 0.768  # 重心高さ (m)
A = 2.452  # トレッドの半分または重心から横転軸までの水平距離 (m)

# 事故現場のカーブ半径
R_ACCIDENT = 70.5  # m

# --- 横転限界速度の計算と表示 ---
print("--- 横転限界速度の計算結果 ---")

# 事故現場での横転限界速度
try:
    v_rollover_accident = calculate_rollover_speed(R_ACCIDENT, G, B, A)
    print(f"事故現場 (R = {R_ACCIDENT} m) での横転限界速度:")
    print(f"  約 {v_rollover_accident:.2f} m/s")
    print(f"  約 {v_rollover_accident * 3.6:.2f} km/h")
except ValueError as e:
    print(f"エラー: {e}")

# 任意のRのサンプル値とそれに対応する横転限界速度
R_sample = [0.5 * R_ACCIDENT, 0.75 * R_ACCIDENT, 1.0 * R_ACCIDENT, 1.25 * R_ACCIDENT]
print("\n任意のRのサンプル値とそれに対応する横転限界速度:")
for R in R_sample:
    try:
        v_rollover = calculate_rollover_speed(R, G, B, A)
        print(f"  R = {R:.2f} m: 約 {v_rollover:.2f} m/s (約 {v_rollover * 3.6:.2f} km/h)")
    except ValueError as e:
        print(f"  R = {R:.2f} m: エラー: {e}")

# --- グラフの作成 ---
print("\n--- 横転限界速度グラフの作成 ---")

# グラフ用のR値の範囲
R_values = np.linspace(0.1 * R_ACCIDENT, 1.5 * R_ACCIDENT, 200) # より滑らかな曲線のために点を増やす
v_rollover_values = []
for R_val in R_values:
    try:
        v_rollover_values.append(calculate_rollover_speed(R_val, G, B, A))
    except ValueError:
        v_rollover_values.append(np.nan) # 無効な値はプロットしない

plt.figure(figsize=(12, 7))
plt.plot(R_values, v_rollover_values, label=r'$v = \sqrt{R \cdot g \cdot b/a}$', color='blue', linewidth=2)

# 事故現場の点をプロット
plt.scatter(R_ACCIDENT, v_rollover_accident, color='red', s=150, zorder=5,
            label=f'($R={R_ACCIDENT:.1f}$ m)\n({v_rollover_accident*3.6:.1f} km/h)')

# サンプル点をプロット
for R_s in R_sample:
    try:
        v_s = calculate_rollover_speed(R_s, G, B, A)
        plt.scatter(R_s, v_s, color='green', marker='X', s=120, zorder=5)
        plt.text(R_s, v_s + 0.5, f'{v_s*3.6:.1f} km/h', fontsize=9, ha='center', va='bottom', color='green')
    except ValueError:
        pass # エラーの場合はプロットしない

plt.title('rollover-speed vs courner-radius', fontsize=16)
plt.xlabel('courner-radius R (m)', fontsize=14)
plt.ylabel('rollover-speed v (m/s)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tight_layout()
plt.savefig('rollover-speed.png')
plt.show()

print("\nコードの実行が完了しました。")