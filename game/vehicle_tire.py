"""第 55 批：赛车过弯时轮胎像冰面、漂移突然回正、悬挂过坎弹飞..."""

def slip_angle(steer, velocity_angle):
    """返回轮胎侧偏角。"""
    raise NotImplementedError("TODO: slip_angle")

def lateral_force(angle, stiffness):
    """返回侧向力。"""
    raise NotImplementedError("TODO: lateral_force")

def load_transfer(load, accel):
    """返回载荷转移量。"""
    raise NotImplementedError("TODO: load_transfer")

def slip_ratio(wheel_speed, ground_speed):
    """返回滑移率。"""
    raise NotImplementedError("TODO: slip_ratio")

def drift_angle(velocity, heading):
    """返回车身漂移角。"""
    raise NotImplementedError("TODO: drift_angle")

def spring_force(stiffness, compression):
    """返回悬挂弹簧力。"""
    raise NotImplementedError("TODO: spring_force")

def damping_force(damping, velocity):
    """返回悬挂阻尼力。"""
    raise NotImplementedError("TODO: damping_force")

def cg_inertia(mass, wheelbase):
    """返回车身重心惯量。"""
    raise NotImplementedError("TODO: cg_inertia")

def abs_torque(engine_torque, brake):
    """协调 ABS 与引擎扭矩。"""
    raise NotImplementedError("TODO: abs_torque")

def road_friction(surface):
    """按路面返回摩擦系数。"""
    raise NotImplementedError("TODO: road_friction")
