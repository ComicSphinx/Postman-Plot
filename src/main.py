# @Author: Daniil Maslov (ComicSphinx)

import json
import matplotlib as mpl
import matplotlib.pyplot as plt

with open('Get.postman_test_run.json', 'r') as file:
    text = json.load(file)

passed = text['totalPass']
failed = text['totalFail']
tests_labels = ['passed', 'failed']
yticks = [passed, failed]
tests = [passed, failed]

mpl.rcParams['toolbar'] = 'none'
plt.ylabel("Quantity")
plt.yticks(yticks)
plt.bar(tests_labels, tests, align='center', width=0.3)
plt.subplots_adjust(bottom = 0.1, top = 0.95)

plt.show()
