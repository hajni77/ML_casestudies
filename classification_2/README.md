1. Supervised learning 
    data preprocessing
        - delete unnecesarry columns
        - create dummy columns from categorical data
                for col in cat_variables:
                    one_hot = pd.get_dummies(df[col], prefix = col, drop_first = True)
                    
                    df = df.drop(col, axis = 1)
                    df = df.merge(one_hot, left_index = True, right_index = True)
        - standardscaler() for numeric values
        - missing values = mean value
    clustering
        optimal clustnumber
        kmeans and then decisiontree
            dct = DecisionTreeClassifier(max_depth = 2)
            dct.fit(df.loc[:, X_cols], df['cluster_kmeans'])