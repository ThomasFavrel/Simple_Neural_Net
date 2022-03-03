import numpy as np
import matplotlib.pyplot as plt
    
    
def plot_train_test_size(m_train, m_test):
    fig, ax = plt.subplots()
    ax.bar(x=['Train', 'Test'],
           height=[m_train, m_test],
           width=1,
           edgecolor="white",
           linewidth=0.7)

    ax.set_frame_on(False)
    ax.axes.get_yaxis().set_visible(False)

    ax.set_xticks(['Train', 'Test'])
    ax.set_xticklabels(['Train', 'Test'], size=20)

    ax.set_title(label='Train size vs Test size',
                 size=38,
                 fontname='Times New Roman',
                 fontweight='normal',
                 pad=25,
                 loc='right')

    ax.text(x=-.20,
            y=m_train//2,
            s=f"{m_train}",
            color='white',
            size=35,
            fontname='Times New Roman',
            fontweight='bold')

    ax.text(x=.88,
            y=m_test//2 - 12,
            s=f"{m_test}",
            color='white',
            size=35,
            fontname='Times New Roman',
            fontweight='bold')

def plot_cate_distrib_train_test(train, test):
    
    count_label_train = list(np.unique(train, return_counts=True)[1])
    count_label_test = list(np.unique(test, return_counts=True)[1])

    fig, ax = plt.subplots(ncols=2, figsize=(12.8, 4.8))

    ax[0].bar(x=['Not cat', 'Cat'],
           height=count_label_train,
           width=1,
           edgecolor="white",
           linewidth=0.7,
           color=['indianred', 'tab:blue'])

    ax[0].set_frame_on(False)
    ax[0].axes.get_yaxis().set_visible(False)

    ax[0].set_xticks(['Not cat', 'Cat'])
    ax[0].set_xticklabels(['Not cat', 'Cat'], size=20)

    ax[0].set_title(label='Training distribution',
                 size=38,
                 fontname='Times New Roman',
                 fontweight='normal',
                 pad=25,
                 loc='right')

    ax[0].text(x=-.20,
            y=count_label_train[0]//2,
            s=f"{count_label_train[0]}",
            color='white',
            size=35,
            fontname='Times New Roman',
            fontweight='bold')

    ax[0].text(x=.88,
            y=count_label_train[1]//2 - 12,
            s=f"{count_label_train[1]}",
            color='white',
            size=35,
            fontname='Times New Roman',
            fontweight='bold')

    ax[1].bar(x=['Not cat', 'Cat'],
           height=count_label_test,
           width=1,
           edgecolor="white",
           linewidth=0.7,
           color=['indianred', 'tab:blue'])

    ax[1].set_frame_on(False)
    ax[1].axes.get_yaxis().set_visible(False)

    ax[1].set_xticks(['Not cat', 'Cat'])
    ax[1].set_xticklabels(['Not cat', 'Cat'], size=20)

    ax[1].set_title(label='Testing distribution',
                 size=38,
                 fontname='Times New Roman',
                 fontweight='normal',
                 pad=25,
                 loc='right')

    ax[1].text(x=-.16,
            y=count_label_test[0]//2 - 2,
            s=f"{count_label_test[0]}",
            color='white',
            size=35,
            fontname='Times New Roman',
            fontweight='bold')

    ax[1].text(x=.88,
            y=count_label_test[1]//2,
            s=f"{count_label_test[1]}",
            color='white',
            size=35,
            fontname='Times New Roman',
            fontweight='bold');
