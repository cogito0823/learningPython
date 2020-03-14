#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File    :   survey.py
@Time    :   2020/03/14 22:24:34
@Author  :   cogito0823
@Contact :   754032908@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

class AnonymousSurvey():
    
    def __init__(self,question):
        self.question = question
        self.responses = []
        
    def show_question(self,question):
        print(question)
    
    def store_responses(self,response):
        self.responses.append(response)
        
    def show_result(self):
        print("Survey results:")
        for response in self.responses:
            print(f'- {response}')