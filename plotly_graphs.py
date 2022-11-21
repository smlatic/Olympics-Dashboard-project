import pandas as pd
import plotly.express as px
from Load_data import Load_data as ld

class Finland:
    
    olympic_data_finland = None
    
    @classmethod
    def initialize(cls):
        cls.olympic_data_finland = ld.olympic_data.loc[ld.olympic_data['NOC'] == 'FIN']
    
    @staticmethod
    def graphfig():

        # Get all rows where a player managed to score a medal
        olympic_data_finland_with_medals = Finland.olympic_data_finland[Finland.olympic_data_finland['Medal'].notna()]

        # Filter the rows into groups of sports, than sum the "Medals" column for each given sport
        medals_per_finland_sport = olympic_data_finland_with_medals.groupby('Sport')['Medal'].count()

        medals_per_finland_sport = medals_per_finland_sport.sort_values(ascending=False)

        # Take the top 5 sports with most medals scored
        medals_per_sport_top5_finland = medals_per_finland_sport[:5]

        fig = px.bar(
            x=medals_per_sport_top5_finland.index,
            y=medals_per_sport_top5_finland,
            title="Medal distribution across the olympic sports in finland",
            labels={
                'x': '',
                'y': 'Medals'
            }
        )
        
        return fig
    
class General:
    pass