# 导入所需库
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pandas as pd

# 步骤1: 生成模拟数据
np.random.seed(0)  # 设置随机种子以获得可复现的结果
X = np.random.rand(100, 2) * 10  # 特征数据，100个样本，两个特征
y = 1 + 2 * X[:, 0] + 3 * X[:, 1] + np.random.randn(100, 1)  # 目标变量，多特征线性关系加上一些噪声
y = y.reshape(-1, 1)  # 调整y的形状为(100, 1)

# 将数据封装到pandas DataFrame中
df = pd.DataFrame(np.hstack((X, y)), columns=['X1', 'X2', 'y'])

# 步骤2: 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(df[['X1', 'X2']], df['y'], test_size=0.2, random_state=42)

# 步骤3: 创建线性回归模型实例
model = LinearRegression()

# 步骤4: 训练模型
model.fit(X_train, y_train)

# 步骤5: 预测
y_pred = model.predict(X_test)

# 步骤6: 评估模型
# 计算均方误差 (Mean Squared Error, MSE)
mse = metrics.mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# 计算决定系数 R^2
r2 = metrics.r2_score(y_test, y_pred)
print(f"R^2 Score: {r2:.2f}")

# 步骤7: 查看模型参数
print(f"Coefficients: [{model.coef_[0][0]:.2f}, {model.coef_[0][1]:.2f}]")
print(f"Intercept: {model.intercept_[0]:.2f}")
