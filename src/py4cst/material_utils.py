from .cst.wrappers import Material
from .cst import units
from typing import Optional

def set_normal_type_general_properties(
        material: Material,
        rel_permitivity: float, rel_permeability: float,
        name: Optional[str] = None, folder: Optional[str] = None):
    material.set_type(Material.Type.NORMAL)
    material.set_rel_permitivity(rel_permitivity)
    material.set_rel_permeability(rel_permeability)
    if name is not None:
        material.set_name(name)
    if folder is not None:
        material.set_folder_name(folder)

def set_appearance(
        material: Material,
        color_rgba: tuple[float, float, float, float] = (0.6, 0.6, 0.6, 1.0),
        wireframe: bool = False, allow_outlines: bool = True,
        reflection: bool = False, transparent_solid_outlines: bool = False):
    material.set_color_rgb(*color_rgba[0:3])
    material.set_color_alpha(color_rgba[3])
    material.set_wireframe(wireframe)
    material.set_allow_outlines(allow_outlines)
    material.set_reflection(reflection)
    material.set_transparent_solid_outlines(transparent_solid_outlines)

def set_units(
        material: Material,
        freq_unit: str = units.FREQUENCY_HERTZ, geom_unit: str = units.GEOMETRY_METER,
        time_unit: str = units.TIME_SECOND, temp_unit: str = units.TEMPERATURE_KELVIN):
    material.set_frequency_unit(freq_unit)
    material.set_geometry_unit(geom_unit)
    material.set_time_unit(time_unit)
    material.set_temperature_unit(temp_unit)

def set_simple_el_conductivity(material: Material, conductivity: float):
    material.set_el_conductivity(conductivity)
    material.set_el_tangent_delta_given(False)
    material.set_el_parametric_conductivity(False)

def set_simple_mag_conductivity(material: Material, conductivity: float):
    material.set_mag_conductivity(conductivity)
    material.set_mag_tangent_delta_given(False)
    material.set_mag_parametric_conductivity(False)

def set_const_el_tangent_delta(material: Material, tand: float, tand_freq: float):
    material.set_el_tangent_delta(tand)
    material.set_el_tangent_delta_frequency(tand_freq)
    material.set_el_tangent_delta_given(True)
    material.set_el_tangent_delta_model(Material.TangentDeltaModel.CONST_TAN_D)
    material.set_el_const_tangent_delta_strategy_eps(
        Material.ConstTangentDeltaStrategy.AUTOMATIC_ORDER)

def set_const_mag_tangent_delta(material: Material, tand: float, tand_freq: float):
    material.set_mag_tangent_delta(tand)
    material.set_mag_tangent_delta_frequency(tand_freq)
    material.set_mag_tangent_delta_given(True)
    material.set_mag_tangent_delta_model(Material.TangentDeltaModel.CONST_TAN_D)
    material.set_mag_const_tangent_delta_strategy_mu(
        Material.ConstTangentDeltaStrategy.AUTOMATIC_ORDER)

def prepare_simple_material(
        material: Material,
        rel_permitivity: float = 1.0, rel_permeability: float = 1.0,
        el_conductivity: float = 0.0, mag_conductivity: float = 0.0) -> None:
    material.reset()
    material.set_material_density(0)
    material.set_reference_coord_system(Material.RefCoordSystem.GLOBAL)
    material.set_coord_system_type(Material.CoordSystem.CARTESIAN)
    set_units(material)
    set_normal_type_general_properties(material, rel_permitivity, rel_permeability)
    set_simple_el_conductivity(material, el_conductivity)
    set_simple_mag_conductivity(material, mag_conductivity)

def prepare_simple_material_tand(
        material: Material,
        rel_permitivity: float = 1.0, rel_permeability: float = 1.0,
        el_tan_delta: float = 0.0, mag_tan_delta: float = 0.0,
        el_tan_delta_freq: float = 0.0, mag_tan_delta_freq: float = 0.0) -> None:
    material.reset()
    material.set_material_density(0)
    material.set_reference_coord_system(Material.RefCoordSystem.GLOBAL)
    material.set_coord_system_type(Material.CoordSystem.CARTESIAN)
    set_units(material)
    set_normal_type_general_properties(material, rel_permitivity, rel_permeability)
    set_const_el_tangent_delta(material, el_tan_delta, el_tan_delta_freq)
    set_const_mag_tangent_delta(material, mag_tan_delta, mag_tan_delta_freq)

def prepare_vacuum(material: Material) -> None:
    prepare_simple_material(
        material,
        rel_permitivity=1.0, rel_permeability=1.0,
        el_conductivity=0.0, mag_conductivity=0.0)

def prepare_surface_impedance_table(
        material: Material,
        frq_imp_weight: list[tuple[float, complex, float]],
        max_order: int = 10,
        error_limit: float = 0.1,
        transparent_model: bool = False):
    # frq_imp_weight: list of tuples: [(freq, impdance, weight), ...]
    material.reset()
    material.set_material_density(0)
    material.set_reference_coord_system(Material.RefCoordSystem.GLOBAL)
    material.set_coord_system_type(Material.CoordSystem.CARTESIAN)
    set_units(material)
    material.set_type(Material.Type.LOSSY_METAL)
    material.set_tabulated_surface_impedance_model(
        Material.TabSurfImpModel.TRANSPARENT\
            if transparent_model else Material.TabSurfImpModel.OPAQUE)
    for freq, imp, weight in frq_imp_weight:
        material.add_tabulated_surface_impedance_fitting_value(freq, imp, weight)
    material.set_dispersive_fitting_scheme_tab_surf_imp(Material.DispFitSchemeTabSI.NTH_ORDER)
    material.set_max_order_nth_model_fit_tab_surf_imp(max_order)
    material.set_use_only_data_in_sim_freq_range_nth_model_tab_surf_imp(True)
    material.set_error_limit_nth_model_fit_tab_surf_imp(error_limit)
