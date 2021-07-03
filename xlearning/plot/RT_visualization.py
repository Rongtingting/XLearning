## Publication format setting





## confusion matrix heatmap
def confuse_heatmap(confuse_mat_df, cmap = "Blues", version1 = True, version2 =True, plot_xlabel = None,
                    plot_ylabel = None, plt_title = None, save_file_name = None):
    """
    Function:
    confusion matrix heatmap
    
    confuse_mat_df: count- confusion matrix in pd.DataFrame
    
    Example：
    confuse_heatmap(confuse_mat_df, version1 = False, save_pdf = True)
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    ## setting
    font = {'family' : 'DejaVu Sans',
            'size'   : 15}
    plt.rc('font', **font)
    if version1:
        sns.heatmap(confuse_mat_df, annot=True, fmt="d", cmap=cmap)
    if version2:
        ## data normalization
        plot_df = (confuse_mat_df.T/confuse_mat_df.sum(axis=1).values).T
        ## plot percentage
        plt.figure(figsize=[8,6])
        ax = sns.heatmap(plot_df, cmap=cmap) # annot=True,
        ## annot original count
        height, width = np.array(confuse_mat_df).shape
        text_colors = ['black', 'white']
        for x in range(width):
            for y in range(height):
                ax.annotate(str(np.array(confuse_mat_df)[y][x]), xy=(x+0.5, y+0.5), 
                            horizontalalignment='center',
                            verticalalignment='center', color=text_colors[int(np.array(plot_df)[y][x] > 0.5)], fontsize = 15)
        if plot_xlabel is None:
            pass
        else:
            plt.xlabel(plot_xlabel)
        if plot_ylabel is None:
            pass
        else:
            plt.ylabel(plot_ylabel)
        # plt.yticks(rotation=45)
        # plt.xticks(rotation=45)
        # plt.xticks(range(3), confusion_matrix.columns) #, rotation=315)
        # plt.yticks(range(len(norm_conf)), set(clone_id))
        plt.tight_layout()
        if plt.title is None:
            pass
        else:
            plt.title(plt_title, fontsize = 18)#             plt.title('Concordance in subclone identification', fontsize = 18)
        if save_file_name is None:
            pass
        else:
            plt.savefig(save_file_name, dpi=300, bbox_inches='tight') 
                        #plt.savefig('CopyKAT_vs_Groudtruth.pdf', dpi=300, bbox_inches='tight')
              
# usage              
confuse_mat, ids1_uniq, ids2_uniq = get_confusion(CopyKAT_lst, expression_lst)

confuse_mat_df = get_confuse_mat_df(confuse_mat,index_names=["cloneA", "cloneB","Normal"],clolums_names=["cloneA", "cloneB","Normal"])
confuse_heatmap(confuse_mat_df,  plot_xlabel = "CopyKAT",
                    plot_ylabel = "Ground Truth", plt_title = "Concordance in subclone identification", save_file_name = 'CopyKAT_vs_Groudtruth1.pdf')
