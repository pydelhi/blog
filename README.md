# PyDelhi Blog
Source code and published articles by PyDelhi Community. Blog made with [Pelican](https://github.com/getpelican/pelican).


## For content writers

- Clone this repo.
- Create a file in `content/`, see existing files as an example.
- Use `./devserver.sh start` to start a local preview server.
- Use `./devserver.sh stop` to stop the server.
- Send a pull request.


## For developers:

- Install python dependencies:
  ```
  mkvirtualenv -p /usr/bin/python3 taiga-blog
  workon taiga-blog
  pip install -r requirements.txt
  ```

- Install SASS:
  ```
  gem install sass scss-lint
  export PATH="/usr/bin/core_perl:$(ruby -e "print Gem.user_dir")/bin:$PATH"
  ```

- Run in devel mode
  ```
  make compile_styles
  make devserver
  ```

###### We thank [taiga-blog](https://github.com/taigaio/taiga-blog) for development of this theme our PyDelhi Blog is using.
