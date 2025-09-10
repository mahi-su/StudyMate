from setuptools import setup, find_packages

setup(
    name='studymate',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='An AI-powered PDF Based Q&A System for Students',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/studymate',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'streamlit',
        'PyMuPDF',
        'sentence-transformers',
        'faiss-cpu',
        'ibm-watson'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)