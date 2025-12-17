import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from typing import Optional, Tuple

DEFAULT_ZOOM = 1.2
DEFAULT_COLORMAP = 'turbo'

_bbox_l = 0.0-(DEFAULT_ZOOM-1.0)
_bbox_r = 1.0+(DEFAULT_ZOOM-1.0)
_bbox_t = 1.0+(DEFAULT_ZOOM-1.0)
_bbox_b = 0.0-(DEFAULT_ZOOM-1.0)

def set_bounding_box(
    left: float = 0.0,
    right: float = 1.0,
    top: float = 1.0,
    bottom: float = 0.0,
) -> None:
    global _bbox_l, _bbox_r, _bbox_t, _bbox_b
    _bbox_l = left
    _bbox_r = right
    _bbox_t = top
    _bbox_b = bottom

def plot_farfield_lin(
    e_mag: np.ndarray,
    theta_vec_deg: np.ndarray,
    phi_vec_deg: np.ndarray,
    units: Optional[str] = None,
    colormap: str = DEFAULT_COLORMAP,
    axes: Optional[Axes] = None,
) -> None:
    e_mag = np.hstack((e_mag, e_mag[:, [0]]))
    phi_vec_deg = np.append(phi_vec_deg, 360)
    r = e_mag - e_mag.min()
    if axes is None:
        axes = plt.axes(projection='3d')
    _draw_circles(axes)
    _draw_x_y_z_labels(axes)
    _draw_3d_plot(e_mag, theta_vec_deg, phi_vec_deg, r, axes, units, colormap)

def plot_farfield_log(
    ff: np.ndarray,
    theta_vec_deg: np.ndarray,
    phi_vec_deg: np.ndarray,
    dyn_range: float,
    units: Optional[str] = None,
    colormap: str = DEFAULT_COLORMAP,
    axes: Optional[Axes] = None
) -> None:
    ff = np.abs(ff)
    ff = _get_field_in_db(ff, dyn_range)
    plot_farfield_lin(ff, theta_vec_deg, phi_vec_deg, units=units, colormap=colormap, axes=axes)

def new_figure(*args, **kwargs) -> Figure:
    return plt.figure(*args, **kwargs)

def show() -> None:
    plt.show()

def _sph2cart(
    theta_rad: np.ndarray,
    phi_rad: np.ndarray,
    r: np.ndarray
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    x = r * np.sin(theta_rad) * np.cos(phi_rad)
    y = r * np.sin(theta_rad) * np.sin(phi_rad)
    z = r * np.cos(theta_rad)
    return x, y, z

def _draw_3d_plot(
    e_mag: np.ndarray,
    theta_vec_deg: np.ndarray,
    phi_vec_deg: np.ndarray,
    r: np.ndarray,
    ax: plt.Axes,
    units: Optional[str] = None,
    colormap: str = DEFAULT_COLORMAP,
):
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
        mappable=sm, ax=ax, ticks=np.linspace(e_mag.min(), e_mag.max(), 10),
        shrink=0.55, pad=0.0, anchor=(-1.0, 0.5))
    if units is not None:
        cb.ax.set_title(units, y=1.02)
    return surf

def _draw_circles(ax: plt.Axes, radius: float = 1.05):
    angles = np.linspace(0, 2*np.pi, 360)
    a = radius*np.cos(angles)
    b = radius*np.sin(angles)
    c = np.zeros(len(angles))
    ax.plot(a, b, c, linewidth=2, color='b', zorder=0) # z
    ax.plot(c, a, b, linewidth=2, color='r', zorder=0) # x
    ax.plot(b, c, a, linewidth=2, color='g', zorder=0) # y

def _draw_x_y_z_labels(ax: plt.Axes, radius: float = 1.2) -> None:
    ax.plot([0, radius], [0, 0], [0, 0], color='r', linewidth=1.5, zorder=0)
    ax.plot([0, 0], [0, radius], [0, 0], color='g', linewidth=1.5, zorder=0)
    ax.plot([0, 0], [0, 0], [0, radius], color='b', linewidth=1.5, zorder=0)
    ax.text(1.1*radius, 0, 0, s='x', zdir=None, zorder=0, weight='bold', color='k')
    ax.text(0, 1.05*radius, 0, s='y', zdir=None, zorder=0, weight='bold', color='k')
    ax.text(0, 0, 1.05*radius, s='z', zdir=None, zorder=0, weight='bold', color='k')

def _get_field_in_db(f: np.ndarray, dyn_range: float) -> np.ndarray:
    f[f < 0.0000001] = 0.0000001
    f_db = 20.0*np.log10(f)
    threshold = f_db.max()-dyn_range
    f_db[f_db < threshold] = threshold
    return f_db
