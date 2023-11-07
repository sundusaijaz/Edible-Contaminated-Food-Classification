data = {'Apricot': 219,
 'Banana(C)': 187,
 'Blueberry': 198,
 'Cauliflower': 174,
 'Chestnut(C)': 200,
 'Clementine(C)': 238,
 'Coconut(C)': 105,
 'Dates(C)': 61,
 'Garlic(C)': 142,
 'Granadilla(C)': 180,
 'Grape Blue(C)': 118,
 'Lemon(C)': 273,
 'Lichi(C)': 120,
 'Papaya(C)': 159,
 'Potato(C)': 304,
 'Pumpkin(C)': 125,
 'Strawberry(C)': 202,
 'Tomato(C)': 171,
 'Watermelon(C)': 106,
 'cabbage': 175,
 'capsicum': 200,
 'carrot': 259,
 'cherry wax red': 200,
 'chilli pepper(C)': 154,
 'corn(C)': 270,
 'cucumber(C)': 160,
 'eggplant(C)': 258,
 'fig(C)': 175,
 'ginger(C)': 136,
 'lettuce(C)': 148,
 'mango(C)': 223,
 'onion(C)': 277,
 'peas(C)': 150,
 'rotten Apple granny smith': 190,
 'rotten Apple pink lady': 140,
 'rotten Avocado': 200,
 'spinach(C)': 56}
 
 
items = []
count = []
 
 
for i,c in data.items():
    items.append(i)
    count.append(c)

import matplotlib.pyplot as plt 
import seaborn as sns 



sns.barplot(y=count, x = items)
plt.title("Food Items Count For Contaminated Images")
plt.xticks(rotation=90)	
 
 
 
plt.show()
 
 
 
 
 
 
 
 
