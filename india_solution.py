import pandas

with open('indian_states.csv') as india_file:
    india_df = pandas.read_csv(india_file)
    for index, state in india_df.iterrows():
        if state['Population']/state['Area'] > 800:
            print(f'{state["State Name"]:15s}{state["Population"]:15d}')
