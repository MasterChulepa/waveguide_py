import numpy as np
from scipy.integrate import solve_ivp


def stop_condition(x, y, a, b, h, Bc_sq):
    return y[0]


def paint(plt, sol, color):
    i = 0
    if color == "red":
        while i < len(sol.y):
            plt.axes.plot(sol.t, sol.y[i, :], 'r')
            plt.draw()
            i += 1
    else:
        while i < len(sol.y):
            plt.axes.plot(sol.t, sol.y[i, :], 'b')
            plt.draw()
            i += 1


def f_e(x, y, a, b, m, n):
    return ((a * m) / (b * n)) * (np.tan(np.pi * n * x / a) / np.tan(np.pi * m * y / b))


def f_m(x, y, a, b, m, n):
    return -((b * n) / (a * m) * (np.tan(np.pi * m * y / b) / np.tan(np.pi * n * x / a)))


def f_e_z(z, x, a, m, h, Bc_sq):
    return (h * np.pi * np.tan(h * z)) / (-a * m * Bc_sq * np.tan(np.pi * m * x / a))


class Graphs_TM:

    def findE(self, a, b, m, n, plt, density, h=0.1):
        density *= 2
        iterat_m = 0
        while iterat_m < m:
            iterat_n = 0
            y0 = (iterat_m * 2 + 1) * b / (m * 2)
            while iterat_n < n:
                start1 = iterat_n * a / n
                start2 = (iterat_n + 1) * a / n
                stop = (iterat_n * 2 + 1) * a / (2 * n)
                i = 0
                while i < density:
                    sh = i * (b - 0.2) / (2 * m * density)
                    sol = solve_ivp(f_e, (start1, stop), [y0 + h + sh, y0 - h - sh], args=(a, b, m, n), method='BDF')
                    paint(plt, sol, "blue")
                    sol = solve_ivp(f_e, (start2, stop), [y0 + h + sh, y0 - h - sh], args=(a, b, m, n), method='BDF')
                    paint(plt, sol, "blue")
                    i += 1
                iterat_n += 1
            iterat_m += 1

    def findH(self, a, b, m, n, plt, density, h=0.1):
        density *= 2
        iterat_n = 0
        while iterat_n < n:
            iterat_m = 0
            start = iterat_n * (a / n) + h
            stop = (iterat_n + 1) * a / n - h
            while iterat_m < m:
                i = 1
                y0 = (iterat_m * 2 + 1) * b / (m * 2)
                while i < density:
                    sh = i ** 3 * a / (2 * n * density ** 3)
                    sol = solve_ivp(f_m, (start + sh, stop - sh), [y0 + 0.001, y0 - 0.001], args=(a, b, m, n),
                                    method='BDF')
                    paint(plt, sol, "red")
                    i += 1
                iterat_m += 1
            iterat_n += 1

    def findz(self, a, m, h, Bc_sq, plt, density, shift=0.0001):
        density *= 2
        iterat_m = 0
        start = -1
        stop = 0
        while iterat_m < m:
            y0_1 = iterat_m * a / m + shift
            y0_2 = (iterat_m + 1) * a / m - shift
            i = 0
            while i < density:
                sh = 1 / (density ** 2) * (i ** 2)
                sol = solve_ivp(f_e_z, (start + sh, stop), [y0_1, y0_2], events=stop_condition,
                                args=(a, m, h, Bc_sq), method='BDF')
                paint(plt, sol, "blue")
                sol = solve_ivp(f_e_z, (-start - sh, stop), [y0_1, y0_2], events=stop_condition,
                                args=(a, m, h, Bc_sq), method='BDF')
                paint(plt, sol, "blue")
                i += 1
            iterat_m += 1

    def findz_doted(self, a, plt, shift=0.01):
        start = -1 + shift
        stop = 1 - shift
        x = np.arange(start, stop, 0.6)
        y = np.arange(shift, a - shift, 0.3)
        X, Y = np.meshgrid(x, y)
        plt.axes.plot(X, Y, 'o', color='red', markersize=4)
        plt.draw()
