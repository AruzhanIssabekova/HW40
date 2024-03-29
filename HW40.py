import numpy
import pandas as pd
import matplotlib.pyplot as plt
numpy.random.seed(0)
data = numpy.random.randint(100, 1000, 50)
print(data)

d = pd.date_range(start='2024-01-01', periods=len(data), freq='D')
df = pd.DataFrame({'Date': d, 'Sales': data})
df.set_index('Date', inplace=True)

print("Статистика по продажам:")
print(df.describe())

plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Sales'], marker='o', linestyle='-')
plt.title('Продажи товаров')
plt.xlabel('Дата')
plt.ylabel('Количество продаж')
plt.grid(True)
plt.show()