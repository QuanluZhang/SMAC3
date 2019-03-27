from ConfigSpaceNNI.configuration_space import ConfigurationSpace
from ConfigSpaceNNI.hyperparameters import UniformFloatHyperparameter


def get_branin_config_space():
    """TODO"""
    cs = ConfigurationSpace()
    cs.add_hyperparameter(UniformFloatHyperparameter('x', -5, 10))
    cs.add_hyperparameter(UniformFloatHyperparameter('y', 0, 15))
    return cs