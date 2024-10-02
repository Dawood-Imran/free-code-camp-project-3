import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['BMI'] = df['weight']/(df['height'])**2

df['overweight'] = df['BMI'].apply(lambda x: 1 if x>25 else 0)

new_df = df.copy()

# 3
df['cholesterol'] = df['cholesterol'].map({1:0,2:1,3:1}) 
df['gluc'] = df['gluc'].map({1:0,2:1,3:1}) 



# 4
def draw_cat_plot():

    # 5
    categories = ['active','alco','cholesterol', 'gluc','overweight','smoke']

    # Melt the DataFrame to long format for easy plotting
    df_melted = df.melt(id_vars=['cardio'], value_vars=categories, 
                        var_name='variable', value_name='Value')

    # Create a catplot
    g = sns.catplot(data=df_melted, x='variable', hue='Value', col='cardio',
                    kind='count', height=5, aspect=1.2, palette='Set2')

    # Set titles and adjust layout
    g.set_titles('Cardio = {col_name}')
    g.set_axis_labels('variable', 'total')
    plt.subplots_adjust(top=0.85)
    g.fig.suptitle('Categories Separated by Cardio (0 and 1)')
    # 8
    fig = g.fig
    # 9
    fig.savefig('catplot.png')
    return fig


# Cleaning the data :
# new_df = df[df['ap_lo'] <= df['ap_hi']]


# new_df = new_df[new_df['height']>=new_df['height'].quantile(0.025)]
# new_df = new_df[new_df['height']<=new_df['height'].quantile(0.975)]

# new_df = new_df[new_df['weight']>=new_df['weight'].quantile(0.025)]
# new_df = new_df[new_df['weight']<=new_df['weight'].quantile(0.975)]


new_df = new_df.drop(columns = ['BMI'])
# 10
def draw_heat_map():
    # 11

    # 12
    corr = corr = new_df.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(23, 9))  # Create the figure
    
    # Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', vmin=-1, vmax=1, 
                square=True, linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)
    
    # Return the figure object for testing purposes
    
    # Save the figure to a file
    fig.savefig('heatmap.png')

    return fig
