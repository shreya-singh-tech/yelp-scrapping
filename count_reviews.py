import pandas as pd

df = pd.read_csv("C:/Users/user/Desktop/task-bart/TaskJan27-Feb5/all-Reviews/combined_reviews_info.csv")
n_by_reviews = df.groupby("restaurant name")["reviewer_name"].count()
#g1 = pd.concat([n_by_reviews.head(1)]).reset_index(drop=True)
n_by_reviews.to_csv( "C:/Users/user/Desktop/task-bart/TaskJan27-Feb5/all-Reviews/reviews_info.csv", index=False, encoding='utf-8-sig')
g = df.groupby('restaurant name')
g_1 = pd.concat([g.head(1)]).drop_duplicates().sort_values('restaurant name').reset_index(drop=True)
g_1.to_csv( "C:/Users/user/Desktop/task-bart/TaskJan27-Feb5/all-Reviews/resname_info.csv", index=False, encoding='utf-8-sig')