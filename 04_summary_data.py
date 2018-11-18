# Show summary statistics for analytes data:
rmp_summary = rmp_df.groupby('analyte')['result']\
.agg([np.sum, np.median, np.mean, np.std, 'count'])\
.sort_values(by=['sum'], ascending=False)
print('** Summary Statistics for SF Bay RMP Monitoring Data **')
print(rmp_summary)

ax = rmp_summary[['count']].plot(kind='bar', title ="Sample Count (Each)", figsize=(12, 6), legend=True, fontsize=12)
plt.title('SFEI RMP Water Quality Monitoring - Sample Count by Analyte in SF Bay Area', fontsize=16)
ax.set_xlabel("Analyte Name", fontsize=12)
ax.set_ylabel("Sample Count (Each)", fontsize=12)
plt.show()
