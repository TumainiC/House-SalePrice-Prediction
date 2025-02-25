def plot_distributions_grid(df):
    # Calculate grid dimensions
    n_cols = int(np.ceil(np.sqrt(len(df.columns))))
    n_rows = int(np.ceil(len(df.columns) / n_cols))
    
    # Create figure with specified size
    fig = plt.figure(figsize=(15, 15))
    
    # Create subplots for each column
    for idx, col_name in enumerate(df.columns, 1):
        ax = fig.add_subplot(n_rows, n_cols, idx)
        
        # Create distribution plot
        sns.histplot(data=df, x=col_name, ax=ax, kde=True)
        
        # Rotate x-axis labels if they're too long
        ax.tick_params(axis='x', rotation=45)
        
        # Set title for each subplot
        ax.set_title(col_name, fontsize=10)
        
        # Make y-axis labels smaller
        ax.tick_params(axis='both', which='major', labelsize=8)
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    return fig

def plot_outliers(
    df,
    figsize=(15, 15),
    fontsize=10,
    showfliers=True,
    title="Boxplot of Numeric Columns",
):
    fig = plt.figure(figsize=figsize)
    sns.boxplot(data=df, showfliers=showfliers)
    plt.title(title, fontsize=fontsize)
    plt.xticks(rotation=45)
    plt.show();