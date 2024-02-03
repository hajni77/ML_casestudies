1. analyse of customers's behaviour 
    1.1 Segmentation by number of purchases and average spending

    customer_df = df.groupby('customer_id')['visit_spend'].agg(['count', 'mean'])
        - új df: group by customer_id 
        - .agg: count and sum of visit spend cfor each ID
        - customer_df.loc[:, X_cols] -> minden sor és az X_cols oszlopok

    Simply cluster analysis, KMeans
        The transform() : method allows you to execute a function for each value of the DataFrame. 
                        dataframe.transform(func, axis, raw, result_type, args, kwds)
                    This function does NOT make changes to the original DataFrame object.
        KMeans: The K-means algorithm aims to choose centroids that minimize the inertia, or within-cluster sum-of-squares criterion. Inertia can be recognized as a measure of how internally coherent clusters are.
        centroids = scaler.inverse_transform(centroids_scaled)

    1.2 Segmentation by shopping on different days of the week

        customer_df.groupby('cluster')[X.columns].mean().T.plot(marker='o')
                - 'cluster' based on the result of kmeans, 
                - group by 'cluster' and count the mean in every column based on x.columns
                - T transpose
        
        1.2.2 What percentage of your total expenditure is spent on a given day
            - count the sum
    
    1.3 Segmentation by number of visits per month
        customer_df = df.groupby(['customer_id', 'year_month'])['visit_spend'].count().unstack()
        customer_df.groupby('cluster_month')[X_cols].mean().T.plot(marker='o', legend = None)
            - plots the average spending per month for each cluster (result of 2. kmeans)
