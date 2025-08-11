import streamlit as st
import matplotlib.pyplot as plt

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

def compute_ratios(seq):
    return [round(seq[i + 1] / seq[i], 5) for i in range(1, len(seq) - 1) if seq[i] != 0]

st.set_page_config(page_title="Fibonacci Explorer", page_icon="🌿")
st.title("🌿 Exploring the Fibonacci Sequence")


n = st.slider("How many Fibonacci terms?", 5, 100, 15)
fib_seq = generate_fibonacci(n)
ratios = compute_ratios(fib_seq)

st.subheader("📜 Fibonacci Sequence:")
st.write(fib_seq)

st.subheader("📈 Golden Ratio Approximations:")
st.write(ratios)

st.subheader("🔢 Fibonacci Numbers Plot")
fig, ax = plt.subplots()
ax.plot(range(n), fib_seq, marker='o', color='mediumslateblue')
ax.set_title("Fibonacci Sequence Growth")
ax.set_xlabel("Index")
ax.set_ylabel("Value")
ax.grid(True)
st.pyplot(fig)
