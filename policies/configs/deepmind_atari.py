"""
deepmind_atari.py

A set of configuration schemas for the different types of policies, utilizing the Deepmind-tested configurations for
their Atari 2600 experiments.
"""

deepmind_atari = {
    "mlp": [["In", None], ["Linear", 64], ["Activation"], ["Linear", 64], ["Activation"], ["Out", None]]
}