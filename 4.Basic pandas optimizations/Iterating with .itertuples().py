"""Use .itertuples() to loop over rangers_df and print each row."""
# Loop over the DataFrame and print each row
for row in rangers_df.itertuples():
  print(row)
  

"""Loop over rangers_df with .itertuples() and save each row's Index, Year, and Wins (W) attribute as i, year, and wins."""
# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
  i = row.Index
  year = row.Year
  wins = row.W
  print(i, year, wins)
  

""Now, loop over rangers_df and print these values only for those rows where the Rangers made the playoffs."""
  # Check if rangers made Playoffs (1 means yes; 0 means no)
  if row.Playoffs == 1:
    print(i, year, wins)
