import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np

DEFAULT_ZOOM = 1.2

_bbox_l = 0.0-(DEFAULT_ZOOM-1.0)
_bbox_r = 1.0+(DEFAULT_ZOOM-1.0)
_bbox_t = 1.0+(DEFAULT_ZOOM-1.0)
_bbox_b = 0.0-(DEFAULT_ZOOM-1.0)

def set_bounding_box(left: float = 0.0, right: float = 1.0, top: float = 1.0, bottom: float = 0.0):
    global _bbox_l, _bbox_r, _bbox_t, _bbox_b
    _bbox_l = left
    _bbox_r = right
    _bbox_t = top
    _bbox_b = bottom

def plot_farfield_lin(e_mag, theta_vec_deg, phi_vec_deg, units=None, colormap='turbo'):
    r = e_mag - e_mag.min()
    ax = plt.axes(projection='3d')
    _draw_circles(ax)
    _draw_x_y_z_labels(ax)
    _draw_3d_plot(e_mag, theta_vec_deg, phi_vec_deg, r, ax, units, colormap)

def plot_farfield_log(ff, theta_vec_deg, phi_vec_deg, dyn_range, units=None, colormap='turbo'):
    ff = np.abs(ff)
    ff = _get_field_in_db(ff, dyn_range)
    plot_farfield_lin(ff, theta_vec_deg, phi_vec_deg, units=units, colormap=colormap)

def new_figure(*args, **kwargs):
    return plt.figure(*args, **kwargs)

def show():
    plt.show()

def _sph2cart(theta_rad, phi_rad, r):
    x = r * np.sin(theta_rad) * np.cos(phi_rad)
    y = r * np.sin(theta_rad) * np.sin(phi_rad)
    z = r * np.cos(theta_rad)
    return x, y, z

def _draw_3d_plot(e_mag, theta_vec_deg, phi_vec_deg, r, ax: plt.Axes, units=None, colormap='turbo'):
    vals_phi, vals_theta = np.meshgrid(phi_vec_deg, theta_vec_deg)
    theta_rad = np.deg2rad(vals_theta)
    phi_rad = np.deg2rad(vals_phi)
    x, y, z = _sph2cart(theta_rad, phi_rad, r/r.max())
    surf = ax.plot_surface(
        x, y, z, cmap=colormap, edgecolor='none', rstride=1, cstride=1, alpha=None,
        antialiased=True, zorder=0.5, linewidth=0)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.grid(visible=False)
    ax.get_figure().tight_layout()
    ax.get_figure().subplots_adjust(left=_bbox_l, right=_bbox_r, top=_bbox_t, bottom=_bbox_b)
    cmap = plt.get_cmap(colormap, 10)
    norm = matplotlib.colors.Normalize(vmin=e_mag.min(), vmax=e_mag.max())
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cb = ax.get_figure().colorbar(
        mappable=sm, ax=ax, ticks=np.linspace(e_mag.min(), e_mag.max(), 10), shrink=0.55, pad=0.0, anchor=(-1.0, 0.5))
    if units is not None:
        cb.ax.set_title(units, y=1.02)
    return surf

def _draw_circles(ax: plt.Axes, radius=1.05):
    angles = np.linspace(0, 2*np.pi, 360)
    a = radius*np.cos(angles)
    b = radius*np.sin(angles)
    c = np.zeros(len(angles))
    ax.plot(a, b, c, linewidth=2, color='b', zorder=0) # z
    ax.plot(c, a, b, linewidth=2, color='r', zorder=0) # x
    ax.plot(b, c, a, linewidth=2, color='g', zorder=0) # y

def _draw_x_y_z_labels(ax: plt.Axes, radius=1.2):
    ax.plot([0, radius], [0, 0], [0, 0], color='r', linewidth=1.5, zorder=0)
    ax.plot([0, 0], [0, radius], [0, 0], color='g', linewidth=1.5, zorder=0)
    ax.plot([0, 0], [0, 0], [0, radius], color='b', linewidth=1.5, zorder=0)
    ax.text(1.1*radius, 0, 0, s='x', zdir=None, zorder=0, weight='bold', color='k')
    ax.text(0, 1.05*radius, 0, s='y', zdir=None, zorder=0, weight='bold', color='k')
    ax.text(0, 0, 1.05*radius, s='z', zdir=None, zorder=0, weight='bold', color='k')

def _get_field_in_db(f, dyn_range):
    f[f < 0.0000001] = 0.0000001
    f_db = 20*np.log10(f)
    threshold = f_db.max()-dyn_range
    f_db[f_db < threshold] = threshold
    return f_db