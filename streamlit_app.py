# Import libraries
import pandas as pd
import numpy as np
import streamlit as st


# st.header("this is the markdown")
# st.markdown("this is the header")
# st.subheader("this is the subheader")
# st.caption("this is the caption")


df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y']
    )
# st.line_chart(df)

# Set page title
# st.set_page_config(page_title="My Streamlit App")
st.title ("My Streamlit App")

# Set sidebar options
st.sidebar.title("Menu")
option = st.sidebar.selectbox("Select an option", ("Line Chart", "Bar Chart", "Code"))

# Create some charts
if option == "Line Chart":
    st.title("Line Chart")
    # st.header("this is the markdown")
    # st.markdown("this is the header")
    # st.subheader("this is the subheader")
    st.write("This is Line Chart")
    st.line_chart(df)
elif option == "Bar Chart":
    st.title("Bar Chart")
    st.write("This is Bar Chart")
    st.bar_chart(df)
elif option == "Code":
    st.title("Code and LaTeX")
    st.write("This is Code and LaTeX")
    st.code("""
                import pandas as pd
                import numpy as np
                import streamlit as st
            """)
    st.latex(r''' a+a r^1+a r^2+a r^3 ''')