# Multithreading brute force

This script is a python brute forcer that allow us to use all disponible thread in our pc to send request to a specified url.
This will use a world list that should be provided by the user to test all possible endpoint.

# Me
- :smiley: RAMANANTSIRESY Amour Bien Aimé
- :email: hei.amour.2@gmail.com
- :clipboard: STD21052

# Installation

To run this project, you should install [python](https://www.python.org/downloads/).

# Specify variables

In the file brute_force.py change the following variables :

- **url** : The base url to test
- **world_list_file** : Path to the word list
- **thread_count_to_use** : Number of thread that you want to use

# Run

```sh
python brute_force.py
```

# Code

### Function count_word_list

This function will open the word list and will count all line in.

### Function brute_force_words:

This function get list of words and for each, send request with `requests` lib to the path `url+word`.
If the request do not return `404`, the current url will be saved in iterable `result`.

### Function main

This function will use the count_word_list and the `thread_count` to get word for each thread and will open the world list and iterate it. For each `word_count_for_each_thread`, it will use `brute_force_words` and put it in one thread and in iterable `threads`

    thread.start() // start the function in the thread
    threads.append(thread) // store the thread into an iterable `threads`

After that, this will iterate all thread in the iterable `threads` join theme,

    join(), It will be used to wait for all thread process to finish before showing the result
