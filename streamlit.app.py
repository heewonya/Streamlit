pip install streamlit
import subprocess
subprocess.run(['pip', 'install', 'module_name'])
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # 시각화 라이브러리
import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year' , y='pop')
fig.show()
