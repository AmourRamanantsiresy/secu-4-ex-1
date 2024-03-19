import requests
import threading
import math

result = []
url = "http://127.0.0.1:5000/"
world_list_file = "dir_list.txt"
thread_count_to_use = 4


def count_word_list():
    count = 0
    with open(world_list_file, "r") as wordList:
        for line in wordList:
            count += 1
    return count


def brute_force_words(words):
    for word in words:
        currentUrl = url + word
        response = requests.get(currentUrl)
        if response.status_code != 404:
            result.append(currentUrl)


def main():
    line_count = count_word_list()
    word_count_for_each_thread = math.ceil(line_count / thread_count_to_use)
    with open(world_list_file, "r") as wordList:
        words = []
        threads = []

        for line in wordList:
            if len(words) <= word_count_for_each_thread:
                words.append(line.strip())
            else:
                thread = threading.Thread(target=brute_force_words, args=[words])
                thread.start()
                threads.append(thread)
                words = []

        for thread in threads:
            thread.join()


main()
print(result)
