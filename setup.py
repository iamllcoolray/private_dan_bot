from setuptools import setup, find_packages

setup(
    name="private_dan_bot",  # Replace with your bot's name
    version="0.1.0",  # Start with a version number
    author="Oda Nobunaga",  # Your name or your team's name
    author_email="llcoolray24@gmail.com",  # Your email address
    description="A Discord Bot that responds to the server owner's messages ",
    long_description=open("README.md").read(),  # Reads your README file for long description
    long_description_content_type="text/markdown",
    url="https://github.com/iamllcoolray/private_dan_bot",  # Replace with your bot's GitHub repository URL
    packages=find_packages(),  # Automatically discovers your package
    install_requires=[
        "py-cord>=2.0",  # Minimum Pycord version (adjust to your needs)
        "aiohttp",  # Optional, if your bot uses aiohttp
        "requests",  # Optional, if your bot uses requests
        "python-dotenv",  # If you're using .env files for environment variables
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Adjust if you're using a different license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",  # Ensure the user has a compatible Python version
    entry_points={
        'console_scripts': [
            'private_dan_bot = private_dan_bot.bot:main',  # Replace with the appropriate entry point if applicable
        ],
    },
)
