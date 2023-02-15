import pandas as pd
import streamlit as st
import seaborn as sns

from st_aggrid import GridOptionsBuilder,AgGrid,JsCode

st.title('Streamlit aggrid table formatting')

iris = sns.load_dataset('iris')
iris_df = iris.head(10)


st.write("It is a original raw table:", iris_df)


st.write('##')
st.write("It is transformed DF:")



# Set CSS properties for th elements in dataframe
td_props = [
        ('front-size', '15px')
        ]

th_props = [
        ('font-size', '15px'),
        ('text-align', 'center'),
        ('font-weight', 'bold'),
        ('color', '#6d6d6d'),
        ('backgroud-color', '#f7ffff')
        ]

#Set table styles
styles = [
        dict(selector="th", props=th_props),
        dict(selector="td", props=td_props)
        ]

#Set colormap equal to seaborn light green color palette
cm = sns.light_palette('green', as_cmap=True)


table_to_render = (iris_df.style
        .background_gradient(cmap=cm, axis=1)
        .set_caption('This is custom caption.')
        .format(na_rep = 'No data', precision=2, thousands=',')
        .highlight_null(null_color='white')
        .set_table_styles(styles))
        

st.table(table_to_render)

