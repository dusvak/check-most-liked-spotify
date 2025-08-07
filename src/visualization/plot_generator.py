import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

plt.switch_backend('Agg')

def create_bar_chart(data, title, xlabel, ylabel):
    if not data:
        return None
    
    data.reverse()

    labels = [item[0] for item in data]
    values = [item[1] for item in data]

    sns.set_theme(style="whitegrid", rc={"axes.facecolor":"#282828", "figure.facecolor":"#282828"})
    plt.figure(figsize=(6, 4))

    barplot = sns.barplot(x=labels, y=values, palette="viridis", order=labels)

    plt.title(title, fontsize=16, color='white')
    plt.xlabel(xlabel, fontsize=12, color='white')
    plt.ylabel(ylabel, fontsize=12, color='white')

    plt.xticks(rotation=45, ha='right', color='white')
    plt.yticks(color='white')

    for bar in barplot.patches:
        barplot.annotate(format(bar.get_height(), '.0f'),
                         (bar.get_x() + bar.get_width() / 2,
                          bar.get_height()),ha='center', va='center',
                          size=10, xytext=(0, 8),
                          textcoords='offset points', color='white')

    plt.tight_layout()

    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)

    base64_img = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

    plt.close()

    return base64_img
