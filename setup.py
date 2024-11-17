import versioneer
from setuptools import setup

setup(
    name="guanpu_diffusion2d",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=["guanpu_diffusion2d"],
    install_requires=["numpy", "matplotlib"],
)
