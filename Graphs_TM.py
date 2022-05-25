import numpy as np
from scipy.integrate import solve_ivp, odeint


def stop_condition(x, y, a, b, h, Bc_sq):
    return y[0]


def paint(plt, sol, color):
    dot = len(sol.t) / 2
    i = 0
    if color == "red":
        while i < len(sol.y):
            plt.axes.plot(sol.t, sol.y[i, :], 'r')
            plt.draw()
            i += 1
    else:
        while i < len(sol.y):
            plt.axes.plot(sol.t[int(dot)], sol.y[i, :][int(dot)], 'b->', sol.t, sol.y[i, :], 'b', markersize=4)
            plt.draw()
            i += 1


def f_e(x, y, a, b, m, n):
    return ((a * m) / (b * n)) * (np.tan(np.pi * n * x / a) / np.tan(np.pi * m * y / b))


def f_m(y, x, a, b, m, n):
    return -((b * n) / (a * m) * (np.tan(np.pi * m * y / b) / np.tan(np.pi * n * x / a)))


def f_e_z(z, x, a, m, h, Bc_sq):
    return (h * np.pi * np.tan(h * z)) / (-a * m * Bc_sq * np.tan(np.pi * m * x / a))


class Graphs_TM:

    def findE(self, a, b, n, m, plt, shift=0.06):
        iterat_m = 0
        while iterat_m < m:
            iterat_n = 0
            y0 = (iterat_m * 2 + 1) * b / (m * 2)
            while iterat_n < n:
                start = iterat_n * (a / n)
                stop = (iterat_n * 2 + 1) * a / (2 * n)
                t_span = (start, stop)
                sol = solve_ivp(f_e, t_span, [y0 + shift, y0 - shift], args=(a, b, m, n), method='BDF')
                paint(plt, sol, "blue")
                start = (iterat_n + 1) * a / (n)
                t_span = (start, stop)
                sol = solve_ivp(f_e, t_span, [y0 + shift, y0 - shift], args=(a, b, m, n), method='BDF')
                paint(plt, sol, "blue")
                iterat_n += 1
            iterat_m += 1

    def findH(self, a, b, n, m, plt, shift=0.1):
        iterat_n = 0
        while iterat_n < n:
            iterat_m = 0
            x0 = iterat_n * (a / n) + shift
            x_stop = (iterat_n + 1) * a / n - shift
            t = np.linspace(x0, x_stop, 41)
            while iterat_m < m:
                y0 = (iterat_m * 2 + 1) * b / (m * 2)
                sol = odeint(f_m, [y0 + 0.005, y0 - 0.005], t, args=(a, b, m, n))
                plt.axes.plot(t[20], sol[20][0], 'r->', t[20], sol[20][1], 'r-<', t, sol, 'r')
                plt.draw()
                iterat_m += 1
            iterat_n += 1

    def findz(self, a, m, h, Bc_sq, plt, shift=0.01):
        iterat_m = 0
        i = 0
        start = -1 + shift
        stop = 1 - shift
        t_span = (start, stop)
        while iterat_m < m:
            y0_1 = iterat_m * a / m + shift
            y0_2 = (iterat_m + 1) * a / m - shift
            sol = solve_ivp(f_e_z, t_span, [y0_1, y0_2], events=stop_condition, args=(a, m, h, Bc_sq), method='BDF')
            paint(plt, sol, "blue")
            iterat_m += 1

    def findz_doted(self, a, plt, shift=0.01):
        start = -1 + shift
        stop = 1 - shift
        x = np.arange(start, stop, 0.6)
        y = np.arange(shift, a - shift, 0.3)
        X, Y = np.meshgrid(x, y)
        plt.axes.plot(X, Y, 'o', color='red', markersize=4)
        plt.draw()
