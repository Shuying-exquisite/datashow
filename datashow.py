import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 设置页面标题
st.title("数据加载和可视化应用")

# 上传 CSV 文件
uploaded_file = st.file_uploader("上传一个 CSV 文件", type=["csv"])

if uploaded_file is not None:
    # 读取 CSV 文件
    df = pd.read_csv(uploaded_file)
    
    # 显示数据表
    st.write("数据表:")
    st.dataframe(df)
    
    # 显示数据统计信息
    st.write("数据统计信息:")
    st.write(df.describe())
    
    # 选择列进行可视化
    columns = df.columns.tolist()
    x_axis = st.selectbox("选择 X 轴:", columns)
    y_axis = st.selectbox("选择 Y 轴:", columns)
    
    if x_axis and y_axis:
        # 绘制散点图
        st.write("散点图:")
        fig, ax = plt.subplots()
        ax.scatter(df[x_axis], df[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f"{x_axis} vs {y_axis}")
        
        st.pyplot(fig)
        
        # 绘制柱状图
        st.write("柱状图:")
        fig, ax = plt.subplots()
        ax.bar(df[x_axis], df[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f"{x_axis} vs {y_axis}")
        
        st.pyplot(fig)
else:
    st.write("请上传一个 CSV 文件以继续")
