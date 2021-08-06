import pandas as pd
import streamlit as st

def load_data():
    df_train = pd.read_csv("../data/train.csv")
    df_store = pd.read_csv("../data/store.csv")

    df_new_train = df_train.drop(['Open','Promo','StateHoliday','SchoolHoliday'], axis=1)
    df_new_store = df_store.drop(['CompetitionOpenSinceMonth','CompetitionOpenSinceYear','Promo2','Promo2SinceWeek','Promo2SinceYear','PromoInterval'], axis=1)
    df_train_store = pd.merge(df_new_train, df_new_store, how='left', on='Store')
    st.write(df_train_store)

def app():
    st.title('Pharmaceutical Sales Info')
    load_data()
