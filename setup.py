from setuptools import setup, find_packages
setup(
    name='colabdesign',
    version='1.1.2',
    description='Making Protein Design accessible to all via Google Colab!',
    long_description="Making Protein Design accessible to all via Google Colab!",
    long_description_content_type='text/markdown',
    packages=find_packages(include=['colabdesign*']),
    install_requires=['py3Dmol','absl-py','biopython',
                      'dm-haiku','dm-tree',
                      'jax','ml-collections',
                      'numpy','pandas','scipy','optax','joblib',
                      'matplotlib'],
    include_package_data=True
)
