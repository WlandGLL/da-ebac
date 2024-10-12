
  import pandas as pd
  gasolina_df = pd.read_csv("gasolina.csv", sep=",")
  gasolina_df.head()
  import seaborn as sns
  import matplotlib.pyplot as plt
  sns.lineplot(data= gasolina_df, x = 'dia', y = 'venda')
  plt.savefig('gasolina.png')
  