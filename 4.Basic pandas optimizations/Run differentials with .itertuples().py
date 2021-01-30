# --Use .itertuples() to loop over yankees_df and grab each row's runs scored and runs allowed values.--
run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():
    
    runs_scored = row.RS
    runs_allowed = row.RA
    
  
# "--Now, calculate each row's run differential using calc_run_diff(). Be sure to append each row's run differential to run_diffs.--
    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    run_diffs.append(run_diff)
    
    
# --Append a new column called 'RD' to the yankees_df DataFrame that contains the run differentials you calculated.--
# Append new column
yankees_df['RD'] = run_diffs
print(yankees_df)
