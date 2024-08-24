import matplotlib as plt
import seaborn as sns
def timeSeriesAnalysis(data):
    fig, ax = plt.subplots(figsize=(14, 6))
    data.plot(x='Timestamp', y=['GHI', 'DNI', 'DHI'], ax=ax)
    plt.title('Time Series of GHI, DNI, and DHI')
    plt.ylabel('Radiance (W/m²)')
    plt.xlabel('Timestamp')
    plt.legend(['GHI', 'DNI', 'DHI'])
    plt.show()




#Evaluate the impact of cleaning
# Plot ModA and ModB with cleaning status
def impactOfCleaning(data,column):
    fig, ax = plt.subplots(figsize=(14, 6))
    sns.boxplot(x='Cleaning', y='ModA', data=data, ax=ax)
    plt.title(f'Impact of Cleaning on {column}')
    plt.ylabel(f'{column} (W/m²)')
    plt.xlabel('Cleaning')
    plt.show()





# def 
# fig, ax = plt.subplots(figsize=(14, 6))
# sns.boxplot(x='Cleaning', y='ModB', data=df, ax=ax)
# plt.title('Impact of Cleaning on ModB')
# plt.ylabel('ModB (W/m²)')
# plt.xlabel('Cleaning')
# plt.show()



def correlationAnalysis():
    correlation_matrix = df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()





# Polar plot of wind direction and speed
def windAnalysis():
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, polar=True)
    ax.scatter(df['WD'] * (np.pi / 180), df['WS'], c=df['WS'], cmap='viridis', alpha=0.75)
    ax.set_title('Wind Direction and Speed')
    plt.show()




#Temprature analysis
# Scatter plot of RH vs. TModA
def tempratureAnalysis():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='RH', y='TModA', data=df)
    plt.title('Relative Humidity vs. Temperature of Module A')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Temperature of Module A (°C)')
    plt.show()




# Plot histograms for GHI, DNI, DHI, WS
def histograms():
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    df['GHI'].hist(ax=axs[0, 0], bins=20)
    axs[0, 0].set_title('Histogram of GHI')
    df['DNI'].hist(ax=axs[0, 1], bins=20)
    axs[0, 1].set_title('Histogram of DNI')
    df['DHI'].hist(ax=axs[1, 0], bins=20)
    axs[1, 0].set_title('Histogram of DHI')
    df['WS'].hist(ax=axs[1, 1], bins=20)
    axs[1, 1].set_title('Histogram of Wind Speed')
    plt.tight_layout()
    plt.show()




from scipy import stats

# Calculate Z-scores
z_scores = stats.zscore(df[['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS']].dropna())
df_z_scores = pd.DataFrame(z_scores, columns=['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS'])

# Identify outliers
outliers = (df_z_scores > 3) | (df_z_scores < -3)
print(df[outliers.any(axis=1)])





# Bubble chart of GHI vs. Tamb vs. WS
plt.figure(figsize=(12, 8))
plt.scatter(df['GHI'], df['Tamb'], s=df['WS']*10, alpha=0.5)
plt.title('GHI vs. Tamb with Wind Speed as Bubble Size')
plt.xlabel('GHI (W/m²)')
plt.ylabel('Tamb (°C)')
plt.show()





plt.figure(figsize=(10, 6))
sns.boxplot(data=df)
plt.show()



plt.figure(figsize=(10, 6))
sns.boxplot(x=df['ModA'])
plt.title('Boxplot of ModA With Handling Outliers')
plt.show()





def displayWithoutOutliers(column):
    fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the figure size if needed
    df_no_outliers = removeOutliers(column)  # Remove outliers from the column
    df_no_outliers.boxplot(column=column, ax=ax)

# Customize the plot as desired
    plt.title(f'Boxplot of {column} (Outliers Removed)')
    plt.ylabel(f'Values of {column}')

    plt.show()

displayWithoutOutliers('ModA')