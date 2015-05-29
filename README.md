# indi-flask
A template for building flask apps that use indico

This is a barebones example that can be used to build a proof of concept from an idea. It's intended for those who'd rather not deal with setting up a web server and would like to bring something to life as painlessly as possible. That said, it's great for anybody who wants to move quickly.

To use, clone this repository by taking the link on the right and running

`git clone https://github.com/IndicoDataSolutions/indi-flask`

Then `cd indi-flask` and you're home. For those of you who use [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) (recommended), go ahead and create a the `venv` folder by running `virtualenv venv` and then activating by running:

`source venv/bin/activate`

Then to get all the necessary python dependencies (only `Flask` and `indicoio` right now), run

`pip install -r requirements.txt`

If you haven't seen pip before, [install here](https://pip.pypa.io/en/latest/installing.html)

Hope this helps! For any questions, please [contact me](mailto:aidan@indico.io?subject=About%20that%20tutorial). My name is Aidan and I love to help :)
