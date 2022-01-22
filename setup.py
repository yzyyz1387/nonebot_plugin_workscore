import setuptools
import sys,io
with open("README.md", "r",encoding="utf-8",errors="ignore") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nonebot_plugin_workscore",
    version="0.0.6",
    author="yzyyz1387",
    author_email="youzyyz1384@qq.com",
    keywords=("pip", "nonebot2", "nonebot", "itnews", "nonebot_plugin"),
    description="""nonebot2 plugin work-score""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yzyyz1387/nonebot_plugin_workscore",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    platforms="any",
    install_requires=["requests",'nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0', 'nonebot2>=2.0.0-beta.1,<3.0.0']
)




