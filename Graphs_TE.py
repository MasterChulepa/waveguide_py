import numpy as np
from scipy.integrate import solve_ivp


def paint(plt, sol, color):
    i = 0
    if color == "red":
        while i < len(sol.y):
            if i % 2 == 0:
                plt.axes.plot(sol.t, sol.y[i, :], 'r')
                plt.draw()
                i += 1
            else:
                plt.axes.plot(sol.t, sol.y[i, :], 'r')
                plt.draw()
                i += 1
    else:
        while i < len(sol.y):
            plt.axes.plot(sol.t, sol.y[i, :], 'b')
            plt.draw()
            i += 1


def f_e(x, y, a, b, m, n):
    return -((b * n) / (a * m)) * (np.tan(np.pi * n * x / a) / np.tan(np.pi * m * y / b))


def f_m(x, y, a, b, m, n):
    return ((b * n) / (a * m)) * (np.tan(np.pi * m * y / b) / np.tan(np.pi * n * x / a))


def f_mz(z, x, a, m, h, Bc_sq):
    return - a / m * Bc_sq * np.tan(np.pi * m * x / a) * (h * np.pi * np.tan(-h * z))


def paint_solution_for_find_TE_M(plt, start, stop, y0_1, y0_2, a, b, m, n):
    t_span = (start, stop)
    sol = solve_ivp(f_m, t_span, [y0_1, y0_2], args=(a, b, m, n), method='BDF')
    paint(plt, sol, "red")


class Graphs_TE:

    def findE(self, a, b, m, n, plt, density):
        density *= 2
        halfway = a / 2
        iterat_m = 0
        while iterat_m < m:
            iterat_n = 0
            y0 = (iterat_m * 2 + 1) * b / (m * 2)
            while iterat_n < n:
                i = 0
                start1 = 2 * iterat_n * halfway / n
                stop = (iterat_n * 2 + 1) * halfway / n
                strat2 = (iterat_n * 2 + 2) * halfway / n
                while i < density:
                    sh = i * (b - 0.2) / (2 * m * density)
                    sol1 = solve_ivp(f_e, (start1, stop), [y0 + 0.01 + sh, y0 - 0.01 - sh], args=(a, b, m, n),
                                     method='BDF')
                    sol2 = solve_ivp(f_e, (strat2, stop), [y0 + 0.01 + sh, y0 - 0.01 - sh], args=(a, b, m, n),
                                     method='BDF')
                    paint(plt, sol1, "blue")
                    paint(plt, sol2, "blue")
                    i += 1
                iterat_n += 1
            iterat_m += 1

    def findH(self, a, b, m, n, plt, density, h=0.005):
        density = 2
        iterat_m = 0
        while iterat_m < m:
            iterat_n = 0
            y0_1 = iterat_m * b / m + h
            y0_2 = (iterat_m + 1) * b / m - h
            while iterat_n < n:
                i = 0
                start = iterat_n * (a / n) + h / 2
                stop = (iterat_n + 1) * a / n - h / 2
                paint_solution_for_find_TE_M(plt, start + m * 2 * h, stop, y0_1, y0_2, a, b, m, n)
                while i < density:
                    shx = i * (a - 0.1) / (2 * n * density)
                    shy = i * (b - 0.1) / (2 * m * density)
                    paint_solution_for_find_TE_M(plt, start + shx, stop, y0_1 + shy, y0_2 - shy, a, b, m, n)
                    paint_solution_for_find_TE_M(plt, stop - shx, start, y0_1 + shy, y0_2 - shy, a, b, m, n)
                    i += 1
                iterat_n += 1
            iterat_m += 1

    def findz(self, a, m, h, Bc_sq, plt, density, shift=0.01):
        density *= 2
        iterat_m = 0
        start = -0.5
        stop = 0.5
        while iterat_m < m:
            y0 = (iterat_m * 2 + 1) * a / (2 * m)
            i = 0
            while i < density:
                sh = 0.45 / (density ** 2) * (i ** 2)
                sol = solve_ivp(f_mz, (start + sh, stop - sh), [y0 - shift, y0 + shift], args=(a, m, h, Bc_sq),
                                method='BDF')
                paint(plt, sol, "red")
                i += 1
            iterat_m += 1

    def TE(self, a, b, m, n, c, h, omega, plt, plane, density, rotate=False):
        if rotate:
            temp = a
            a = b
            b = temp
        val = m + n
        Bx = val * np.pi / a
        t = 1
        iterate = 0
        y = np.arange(0.01, b - 0.01, 0.1)
        while iterate < val:
            if iterate % 2 == 0:
                arrow = ' > '
            else:
                arrow = ' < '
            halfway = a / val
            x = np.arange(iterate * halfway + 0.1, (iterate + 1) * halfway - 0.01, 0.1)
            X, Y = np.meshgrid(x, y)
            if plane == 'xy':
                Z = (omega / (Bx * c)) * abs(np.cos(Bx * X / 2 - 1.9)) * np.cos(omega * t)
            elif plane == 'yz':
                Z = (omega / (Bx * c)) * abs(np.sin(omega * t - h * X / 2 - 2.4))
            if rotate:
                CS = plt.axes.contour(Y, X, Z, density * 2, colors=['blue'])
            else:
                CS = plt.axes.contour(X, Y, Z, density * 2, colors=['blue'])
            plt.axes.clabel(CS, inline=False, fontsize=14, fmt=arrow)
            iterate += 1

    def TEH(self, a, b, plt, rotate=False):
        if rotate:
            x = np.arange(0.2, b-0.2, 0.2)
            y = np.arange(0, a, 0.2)
            X, Y = np.meshgrid(x, y)
            plt.axes.plot(Y, X, 'r')
        else:
            x = np.arange(0.2, a-0.1, 0.2)
            y = np.arange(0, b, 0.2)
            X, Y = np.meshgrid(x, y)
            plt.axes.plot(X, Y, 'r')
