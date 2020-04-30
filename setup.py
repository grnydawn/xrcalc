"xrcalc setup module."

def main():

    from setuptools import setup
    from xrcalc import XarrayCalculator as calc

    install_requires = ["microapp>=0.1.12", "xarray", "matplotlib"]

    setup(
        name=calc._name_,
        version=calc._version_,
        description=calc._description_,
        long_description=calc._long_description_,
        author=calc._author_,
        author_email=calc._author_email_,
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Science/Research",
            "Topic :: Scientific/Engineering",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
        keywords="microapp xrcalc",
        include_package_data=True,
        install_requires=install_requires,
        packages=["xrcalc"],
        entry_points={"microapp.apps": "xrcalc = xrcalc"},
        project_urls={
            "Bug Reports": "https://github.com/grnydawn/xrcalc/issues",
            "Source": "https://github.com/grnydawn/xrcalc",
        }
    )

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    main()
