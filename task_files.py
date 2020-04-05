#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import random

#This is for when the pages need to be randomized
'''
pages = ['find_max_grad_2.html','find_max_instructions.html', 'goal_prompt.html', 'train_instructions.html']

grad_tasks = random.sample([0,1,2,3,4,5], 3)

no_grads = ['find_max_1.html','find_max_2.html','find_max_3.html','find_max_4.html','find_max_5.html','find_max_6.html']
with_grads = ['find_max_grad_1.html','find_max_grad_2.html','find_max_grad_3.html', 'find_max_grad_4.html','find_max_grad_5.html','find_max_grad_6.html']

for i in range(6):
       if i in grad_tasks:
              pages.append('gradient_page.html')
              pages.append(with_grads[i])
       else:
              pages.append('no_gradient_page.html')
              pages.append(no_grads[i])

pages.append('goal_describe_prompt.html')


task_files={
       'find_max': pages
       }
'''

task_files={
       'find_max': ['goal_prompt.html', 'train_instructions.html','find_max_1.html','find_max_2.html','find_max_3.html','find_max_4.html','find_max_5.html','find_max_6.html','goal_describe_prompt.html'],
       'find_max_grad': ['goal_prompt.html', 'train_instructions.html','find_max_grad_1.html','find_max_grad_2.html','find_max_grad_3.html', 'find_max_grad_4.html','find_max_grad_5.html','find_max_grad_6.html','goal_describe_prompt.html']
}