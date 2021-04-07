import os
import glob
import pandas as pd
os.chdir("C:/Users/user/Desktop/task-bart/TaskJan27-Feb5/Reviewer-profile")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "C:/Users/user/Desktop/task-bart/TaskJan27-Feb5/all-Reviews/combined_reviewer-Profile.csv", index=False, encoding='utf-8-sig')
