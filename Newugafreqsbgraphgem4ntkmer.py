
import pandas as pd
import numpy as np
import itertools
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns; sns.set()
kmerlist =[]
#Figure out how to get strand orientation of each gene. 
kmerdf  = pd.DataFrame()
cmap=plt.cm.get_cmap(plt.cm.viridis,143)

df = pd.read_csv('gemanalysis2018.all.GPS_events.u.fa', sep='\t',names='s')

df = df[~df['s'].astype(str).str.startswith('>')]

df['s'] = df['s'].str.upper()
listofzeros = [0] * 201
bases = ['A','C','T','G']
xaxis = np.arange(-100,101)

kmers = [p for p in itertools.product(bases, repeat=4)]
for x in kmers:
	kmerlist.append(''.join(x))
kmerdf  = pd.DataFrame()
for x in kmerlist:
	loopdf  = pd.DataFrame({0: listofzeros})
	print(loopdf)
	
	for index, row in df.iterrows():
		word = row[0]
		idx = 0
		while idx < len(word):
			idx = word.find(x, idx)
			print(idx)
			if idx >= 197:
				break
			if idx == -1:
				break
			loopdf.loc[idx] = loopdf.loc[idx] + 1
			idx += 3
			print(x)
			print(loopdf)
	kmerdf = pd.concat([kmerdf, loopdf], axis=1)
kmerdf = kmerdf.dropna(axis=0, how='all')
print(kmerlist)
kmerdf.columns = kmerlist
kmerdf.index = xaxis
kmerdf = kmerdf[:-4]
print(kmerdf)
print(kmers)
colors1 = plt.cm.tab20(np.linspace(0., 1, 128))
colors2 = plt.cm.Dark2(np.linspace(0, 1, 128))
colors = np.vstack((colors1, colors2))
mymap = mcolors.LinearSegmentedColormap.from_list('my_colormap', colors)
kmerdf.to_csv(r'pandasnewGEM.txt', header=True, index=True, sep=' ', mode='a')
plt.figure(figsize=(90,27))
#kmerdf.drop(['TGA'], axis=1).plot(kind='line',color='Gray',lw=.5)
#plt.plot(kmerdf['TGA'],color='black')
plt.legend(fontsize=4, loc='upper right',ncol=5)
plt.xlabel('K-mer Position Relative to Binding Event')
plt.ylabel('K-mer Occurrences')
plt.savefig('UGAplotgraynewGPS4ntKmer.pdf')



