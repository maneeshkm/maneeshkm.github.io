from sklearn import linear_model
import matplotlib.pyplot as plt


def plot_linear_regression(X, y, regr):
    """
    Attributes: X (pandas.DataFrame),
                y (pandas.DataFrame),
                regr (sklearn.linear_model.LinearRegression)
    Function to scatter plot 2D data with fitted linear model.
    """

    plt.scatter(X, y, color='black')
    plt.plot(X, regr.predict(X), color='blue',
             linewidth=3)
    plt.xlabel('SEM')
    plt.ylabel('SEO')
    plt.show()


def linear_regression(X, y, plot_flag=False):
    """
    Attributes: X (pandas.DataFrame),
                y (pandas.DataFrame),
                plot_flag (boolean)
    Function to fit linear regression model.
    Returns linear model built from sklearn.linear_model.LinearRegression
    """
    regressor = linear_model.LinearRegression()
    regressor.fit(X, y)
    if plot_flag:
        plot_linear_regression(X, y, regressor)
    return regressor
