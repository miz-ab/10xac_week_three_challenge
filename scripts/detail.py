import pandas as pd
import streamlit as st
import numpy as np
import altair as alt
#import plotly.express as px


def barChart(data, title, X, Y):
    title = title.title()
    st.title(f'{title} Chart')
    msgChart = (alt.Chart(data).mark_bar().encode(alt.X(f"{X}:N", sort=alt.EncodingSortField(field=f"{Y}", op="values",
                order='ascending')), y=f"{Y}:Q"))
    st.altair_chart(msgChart, use_container_width=True)

def load_data():
    df_train = pd.read_csv("../data/train.csv")
    df_store = pd.read_csv("../data/store.csv")

    df_new_train = df_train.drop(['Open','Promo','StateHoliday','SchoolHoliday'], axis=1)
    df_new_store = df_store.drop(['CompetitionOpenSinceMonth','CompetitionOpenSinceYear','Promo2','Promo2SinceWeek','Promo2SinceYear','PromoInterval'], axis=1)
    # Left-join the train to the store dataset since .Why?
    # Because you want to make sure you have all events even if some of them don't have their store information ( which shouldn't happen)
    df_train_store = pd.merge(df_new_train, df_new_store, how='left', on='Store')

    df_store_type = df_train_store.groupby(by="StoreType").count().Store.reset_index()

    #num = st.slider("Select number of Rankings", 0, 50, 21)
    title = f"Top Ranking By Number of tweets"
    barChart(df_store_type, title, "original_author", "Tweet_count")

def app():
    st.title('Pharmaceutical Sales Info')
    load_data()
