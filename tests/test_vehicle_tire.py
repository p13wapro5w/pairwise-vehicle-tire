import pytest
from game import vehicle_tire as mod

CASES = [
    ("slip_simple", "m.slip_angle(0.5, 0.1) == approx(0.4)"),
    ("slip_zero", "m.slip_angle(0.1, 0.1) == approx(0.0)"),
    ("force_mid", "m.lateral_force(0.5, 2.0) == approx(1.0)"),
    ("transfer_mid", "m.load_transfer(100.0, 2.0) == approx(20.0)"),
    ("ratio_mid", "m.slip_ratio(10.0, 8.0) == approx(0.2)"),
    ("drift_ninety", "m.drift_angle((1.0, 0.0), (0.0, 1.0)) == approx(-90.0)"),
    ("drift_zero", "m.drift_angle((1.0, 0.0), (1.0, 0.0)) == approx(0.0)"),
    ("spring_mid", "m.spring_force(2.0, 3.0) == approx(6.0)"),
    ("damping_mid", "m.damping_force(2.0, 3.0) == approx(6.0)"),
    ("inertia_mid", "m.cg_inertia(100.0, 2.0) == approx(33.333333, abs=0.001)"),
    ("abs_reduce", "m.abs_torque(10.0, 2.0) == approx(8.0)"),
    ("friction_ice", "m.road_friction('ice') == approx(0.2)"),
    ("friction_road", "m.road_friction('road') == approx(1.0)"),
    ("force_zero", "m.lateral_force(0.0, 2.0) == approx(0.0)"),
    ("transfer_zero", "m.load_transfer(0.0, 2.0) == approx(0.0)")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
