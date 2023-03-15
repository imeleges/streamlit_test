
# import pandas as pd
# import numpy as np
# import streamlit as st

# st.title ("this is the app title")
# st.header("this is the markdown")
# st.markdown("this is the header")
# st.subheader("this is the subheader")
# st.caption("this is the caption")
# st.code("x=2021")
# st.latex(r''' a+a r^1+a r^2+a r^3 ''')


# df= pd.DataFrame(np.random.randn(10, 2),columns=['x', 'y'])
# st.line_chart(df)

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set page title
st.set_page_config(page_title="My Streamlit App")

# Set sidebar options
st.sidebar.title("Menu")
option = st.sidebar.selectbox("Select an option", ("Option 1", "Option 2", "Option 3"))

# Create some sample data
data = pd.DataFrame({
    "x": np.random.rand(100),
    "y": np.random.rand(100)
})

# Create some charts
if option == "Option 1":
    st.title("Option 1")
    st.write("This is option 1.")
    st.line_chart(data)
elif option == "Option 2":
    st.title("Option 2")
    st.write("This is option 2.")
    st.bar_chart(data)
elif option == "Option 3":
    st.title("Option 3")
    st.write("This is option 3.")
    fig = px.scatter(data, x="x", y="y")
    st.plotly_chart(fig)
