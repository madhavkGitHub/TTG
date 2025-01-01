import matplotlib.pyplot as plt

latex_expression = r"$\frac{\cos{\left(B \right)}}{a + h_{C}}$"
fig = plt.figure(figsize=(3, 0.5))  # Dimensions of figsize are in inches
text = fig.text(
    x=0.5,  # x-coordinate to place the text
    y=0.5,  # y-coordinate to place the text
    s=latex_expression,
    horizontalalignment="center",
    verticalalignment="center",
    fontsize=16,
)

plt.savefig("equations/equation.png")