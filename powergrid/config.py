from grid2op.Action import TopologyAndDispatchAction
from grid2op.Reward import RedispReward
from grid2op.Rules import DefaultRules
from grid2op.Chronics import Multifolder
from grid2op.Chronics import GridStateFromFileWithForecasts
from grid2op.Backend import PandaPowerBackend

# you need to define this dictionary.
config = {
    # type of backend to use, in this example the default PandaPowerBackend
    "backend": PandaPowerBackend,

    # type of action that the agent will be allowed to perform
    "action_class": TopologyAndDispatchAction,

    # use the default Observation class (CompleteObservation)
    "observation_class": None,
    "reward_class": RedispReward,  # which reward function to use

     # how to use the "parameters" of the environment, we don't recommend to change that
    "gamerules_class": DefaultRules,

    # type of chronics, if you used recommended method 1 of the "Organize the "chronics" folder" section
    # don't change that. Otherwise, put the name (and its proper import) of the
    # class you coded
    "chronics_class": Multifolder,

    # this is specific to the "MultiFolder" part. It says that inside each "scenario folder"
    # the data are represented as a format that can be understood by the GridStateFromFileWithForecasts
    # class. You might need to adapt it depending on the choice you made in "Organize the "chronics" folder"
    "grid_value_class": GridStateFromFileWithForecasts,

    # don't change that
    "volagecontroler_class": None,

    # this is used to map the names of the elements from the grid to the chronics data. Typically, the "load
    # connected to substation 1" might have a different name in the grid file (for example in the grid.json)
    # and in the chronics folder (header of the csv if using `GridStateFromFileWithForecasts`)
    "names_chronics_to_grid": None
}
