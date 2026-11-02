import pandas as pd
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

# 设置随机种子以保证可重复性
np.random.seed(42)

# 读取数据
df = pd.read_csv("detailed_info.csv")

# 提取并去 NaN
dates = df['numeric date'].values
rtt = df['root_to_tip'].values
mask = ~(np.isnan(dates) | np.isnan(rtt))
dates = dates[mask]
rtt = rtt[mask]

# 真实回归
real_slope, intercept, r_value, p_real, stderr = linregress(dates, rtt)
r_squared_real = r_value ** 2

print(f"真实斜率: {real_slope:.2e}")
print(f"真实 R²: {r_squared_real:.3f}")

# 随机化测试
n_perm = 1000
random_slopes = []
for i in range(n_perm):
    dates_shuffled = np.random.permutation(dates)
    slope, _, _, _, _ = linregress(dates_shuffled, rtt)
    random_slopes.append(slope)

random_slopes = np.array(random_slopes)

# 计算 p 值
p_value = np.mean(random_slopes >= real_slope)
p_lower_bound = 1 / n_perm
print(f"p 值 = {p_value:.6f} (实际 p < {p_lower_bound:.4f})")

# 最大随机斜率比较
max_random_slope = np.max(random_slopes)
ratio = real_slope / max_random_slope
print(f"真实斜率是最大随机斜率的 {ratio:.1f} 倍")

# 可视化
plt.figure(figsize=(8, 5))
plt.hist(random_slopes, bins=50, alpha=0.7, color='gray', edgecolor='black', label='Random slopes')
plt.axvline(real_slope, color='red', lw=2, label=f'Real_slope = {real_slope:.2e}')
plt.xlabel('Root-to-tip distance (substitutions/site)')
plt.ylabel('Frequency')
plt.title('Date Randomization Test')
plt.legend()

plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('date_randomization_test.pdf', dpi=300)
plt.show()

